import io

class MeteredFile(io.BufferedRandom):
    """Implement using a subclassing model."""

    def __init__(self, *args, **kwargs):
        super(MeteredFile, self).__init__(*args, **kwargs)
        self._read_ops = 0
        self._read_bytes = 0
        self._write_ops = 0
        self._write_bytes = 0
        
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        res = super(MeteredFile, self).__exit__(exc_type, exc_val, exc_tb)
        return res

    def __iter__(self):
        return self

    def __next__(self):
        # It would be more efficient to read by chunk like real file objets instead of calling readline
        # ... but it's breaking tests
        received = super(MeteredFile, self).readline()
        if not received:
            raise StopIteration()
        self._read_ops += 1
        self._read_bytes += len(received)
        return received

    def read(self, size=-1):
        received = super(MeteredFile, self).read(size)
        self._read_ops += 1
        self._read_bytes += len(received)
        return received

    @property
    def read_bytes(self):
        return self._read_bytes

    @property
    def read_ops(self):
        return self._read_ops

    def write(self, b):
        self._write_ops += 1
        res = super(MeteredFile, self).write(b)
        if res > -1:
            self._write_bytes += res
        return res

    @property
    def write_bytes(self):
        return self._write_bytes

    @property
    def write_ops(self):
        return self._write_ops



class MeteredSocket:
    """Implement using a delegation model."""

    def __init__(self, socket):
        self.received_ops = 0
        self.received_bytes = 0
        self.sent_ops = 0
        self.sent_bytes = 0
        self.socket = socket

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self.socket.__exit__(exc_type, exc_val, exc_tb)

    def recv(self, bufsize, flags=0):
         # The flag should not be passed as positional argument! But it's breaking tests
        received = self.socket.recv(bufsize, flags)
        self.received_ops += 1
        self.received_bytes += len(received)
        return received

    @property
    def recv_bytes(self):
        return self.received_bytes

    @property
    def recv_ops(self):
        return self.received_ops

    def send(self, data, flags=0):
        self.sent_ops += 1
        res = self.socket.send(data, flags)
        if res > -1:
            self.sent_bytes += res
        return res

    @property
    def send_bytes(self):
        return self.sent_bytes

    @property
    def send_ops(self):
        return self.sent_ops
