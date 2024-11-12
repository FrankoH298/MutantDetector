from mutant import *
def test1():
    dna = [
        "BTGCGA",
        "CAGTGC",
        "TTATGT",
        "AGAAGG",
        "CCCCTA",
        "TCACTG"
    ]
    is_mutant(dna)
    dna = [
        "ATGCBA",
        "CAGTGC",
        "TTATGT",
        "AGAAGG",
        "BCCCTA",
        "TCACTG"
    ]
    is_mutant(dna)
    dna = [
        "BTGCBA",
        "CAGTGC",
        "TTATGT",
        "AGAAGG",
        "CCCCTA",
        "TCACTG"
    ]
    is_mutant(dna)
    dna = [
        "BAGCBA",
        "CAATGC",
        "TTAAGT",
        "AGAAAG",
        "BCACTA",
        "TCACTG"
    ]
    is_mutant(dna)
    dna = [
        "BTGABA",
        "CAATGC",
        "TAATGT",
        "AGAAGG",
        "BCACTA",
        "TCACTG"
    ]
    is_mutant(dna)
    dna = [
        "BTGABA",
        "CAATGC",
        "TAATGT",
        "AGAAGG",
        "BCACTA",
        "TCACTG"
    ]
    is_mutant(dna)

test1()