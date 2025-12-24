"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    for x in range(number):
        yield "ABCD"[x % 4]

def generate_row(number):
    """Generate a series of row numbers for airline seats.

    :param number: int - total number of rows to be generated.
    :return: generator - generator that yields row numbers.

    There is no row 13.

    Example: 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5

    """

    for x in range(1, min(number+1, 13)):
        yield x
        yield x
        yield x
        yield x
    for x in range(14, number+2):
        yield x
        yield x
        yield x
        yield x

def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    itrow = generate_row(number//4+1)
    itletter = generate_seat_letters(number)
    for x in range(number):
        yield f"{next(itrow)}{next(itletter)}"

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    return {passengers: seat for passengers, seat in zip(passengers, generate_seats(len(passengers)))}

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    for seat in seat_numbers:
        yield f"{seat}{flight_id}{'0'*12}"[0:12]
