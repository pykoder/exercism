export const steps = (n) => {
  // if (n > 1) return steps(n&1?3*n+1:n>>1)+1; 
  // if (n == 1) return 0;
  // throw Error('Only positive numbers are allowed');

  // non-recursive version for comparison purpose
  // looks like node correctly apply TCO
  // as recursive and non recursive version have
  // basically the same performance.
  for (var count = 0 ; n > 1 ; count++) {
    n = n&1?3*n+1:n>>1;
  }
  if (n == 1) return count;
  throw Error('Only positive numbers are allowed');
};
