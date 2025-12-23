export const steps = (n) => {
  if (n > 1) return steps(n&1?3*n+1:n>>1)+1; 
  if (n == 1) return 0;
  throw Error('Only positive numbers are allowed');
};
