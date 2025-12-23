export class NucleotideCounts {
  static parse(adn) {
    var count = {A:0, C:0, G:0, T:0};
    [...adn].forEach((x) => {
      if (!"ACGT".includes(x)){
        throw new Error('Invalid nucleotide in strand');    
      }
      count[x]++;
    });
    return `${count['A']} ${count['C']} ${count['G']} ${count['T']}`;
  }
}
