MAX_SIZE_DNA = 6


def is_mutant(dna):
    for a in range(len(dna)):
        for b in range(len(dna[a])):
            for direction in range(1, 9):
                if verificar_bordes(dna, a, b, direction):
                    return True
    return False


def verificar_bordes(dna, a, b, dir):
    match dir:
        case 1:  # arriba
            if a - 3 >= 0:  # verificamos que este dentro del rango de la matriz
                for c in range(1, 4):
                    if dna[a][b] != dna[a - c][b]:
                        return False
                return True
        case 2:  # abajo
            if a + 3 < MAX_SIZE_DNA:  # verificamos que este dentro del rango de la matriz
                for c in range(1, 4):
                    if dna[a][b] != dna[a + c][b]:
                        return False
                return True
        case 3:  # izquierda
            if b - 3 >= 0:  # verificamos que este dentro del rango de la matriz
                for c in range(1, 4):
                    if dna[a][b] != dna[a][b - c]:
                        return False
                return True
        case 4:  # derecha
            if b + 3 < MAX_SIZE_DNA:  # verificamos que este dentro del rango de la matriz
                for c in range(1, 4):
                    if dna[a][b] != dna[a][b + c]:
                        return False
                return True

        case 5:  # arriba izq
            # verificamos que este dentro del rango de la matriz
            if ((a - 3) >= 0 and (b - 3) >= 0):
                for c in range(1, 4):
                    if dna[a][b] != dna[a - c][b - c]:
                        return False
                return True
        case 6:  # arriba der
            # verificamos que este dentro del rango de la matriz
            if ((a - 3) >= 0 and (b + 3) < MAX_SIZE_DNA):
                for c in range(1, 4):
                    if dna[a][b] != dna[a - c][b + c]:
                        return False
                return True
        case 7:  # abajo izq
            # verificamos que este dentro del rango de la matriz
            if ((a + 3) < MAX_SIZE_DNA and (b - 3) >= 0):
                for c in range(1, 4):
                    if dna[a][b] != dna[a + c][b - c]:
                        return False
                return True
        case 8:  # abajo der
            # verificamos que este dentro del rango de la matriz
            if ((a + 3) < MAX_SIZE_DNA and (b + 3) < MAX_SIZE_DNA):
                for c in range(1, 4):
                    if dna[a][b] != dna[a + c][b + c]:
                        return False
                return True
    return False
