map_codon_to_protein = {}
for protein, codons in {
    "Methionine": ("AUG",),
    "Phenylalanine": ("UUU", "UUC"),
    "Leucine": ("UUA", "UUG"), 
    "Serine": ("UCU", "UCC", "UCA", "UCG"),
    "Tyrosine": ("UAU", "UAC"),
    "Cysteine": ("UGU", "UGC"),
    "Tryptophan": ("UGG",),
    "STOP": ("UAA", "UAG", "UGA")
}.items():
    for codon in codons:
        map_codon_to_protein[codon] = protein

def proteins(strand):
    proteins = []
    for x in range(0, len(strand), 3):
        codon = strand[x:x+3]
        protein = map_codon_to_protein[codon]
        if protein == "STOP":
            break
        proteins.append(protein)
    return proteins
            
