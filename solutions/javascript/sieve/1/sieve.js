export const primes = (limit) => {

  var sieve = new Set();
  for(let i = 2; i <= limit ; i++) {
    sieve.add(i);
  }

  var res = [];
  for (let n = 2 ; n <= limit ; n++){
    if (sieve.has(n)){
      res.push(n);
      var m = n;
      while (m <= limit) {
        sieve.delete(m);
        m += n;
      }
    }
  }
  
  return res;
};
