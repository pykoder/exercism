export const toRna = (sequence) => {
  const DnaToRna = {'G':'C', 'C':'G', 'T':'A', 'A':'U'};
  return Array.from(sequence).map(c => DnaToRna[c]).join('');
};
