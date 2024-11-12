MAX_SIZE_DNA = 6


def is_mutant(dna):
    for a in range(len(dna)):
        for b in range(len(dna[a])):
            for direction in range(1, 9):
                if check_bounds(dna, a, b, direction):
                    return True
    return False


def check_bounds(dna, a, b, dir):
    match dir:
        case 1:  # UP
            if a - 3 >= 0:  # check if within the matrix range
                for c in range(1, 4):
                    if dna[a][b] != dna[a - c][b]:
                        return False
                return True
        case 2:  # DOWN
            if a + 3 < MAX_SIZE_DNA:  # check if within the matrix range
                for c in range(1, 4):
                    if dna[a][b] != dna[a + c][b]:
                        return False
                return True
        case 3:  # LEFT
            if b - 3 >= 0:  # check if within the matrix range
                for c in range(1, 4):
                    if dna[a][b] != dna[a][b - c]:
                        return False
                return True
        case 4:  # RIGHT
            if b + 3 < MAX_SIZE_DNA:  # check if within the matrix range
                for c in range(1, 4):
                    if dna[a][b] != dna[a][b + c]:
                        return False
                return True

        case 5:  # UP LEFT
            # check if within the matrix range
            if ((a - 3) >= 0 and (b - 3) >= 0):
                for c in range(1, 4):
                    if dna[a][b] != dna[a - c][b - c]:
                        return False
                return True
        case 6:  # UP RIGHT
            # check if within the matrix range
            if ((a - 3) >= 0 and (b + 3) < MAX_SIZE_DNA):
                for c in range(1, 4):
                    if dna[a][b] != dna[a - c][b + c]:
                        return False
                return True
        case 7:  # DOWN LEFT
            # check if within the matrix range
            if ((a + 3) < MAX_SIZE_DNA and (b - 3) >= 0):
                for c in range(1, 4):
                    if dna[a][b] != dna[a + c][b - c]:
                        return False
                return True
        case 8:  # DOWN RIGHT
            # check if within the matrix range
            if ((a + 3) < MAX_SIZE_DNA and (b + 3) < MAX_SIZE_DNA):
                for c in range(1, 4):
                    if dna[a][b] != dna[a + c][b + c]:
                        return False
                return True
    return False
