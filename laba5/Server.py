from numpy import zeros

def permutations(n, length):
    numbers = range(n)
    permutations = n**length
    output = zeros((permutations, length), dtype=int)

    for i in range(length):
        t2 = n**i
        p1 = 0
        while (p1 < permutations):
            for al in range(n):
                for p2 in range(t2):
                    output[p1, i] = numbers[al]
                    p1 += 1
    return output