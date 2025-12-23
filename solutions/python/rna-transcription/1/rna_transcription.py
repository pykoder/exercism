
TRANS = { 'G' : 'C', 'C' : 'G', 'T' : 'A', 'A' : 'U'}
def to_rna(dna_strand):
    return "".join(map(lambda x: TRANS[x], dna_strand ))



