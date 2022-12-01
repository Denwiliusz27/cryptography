# generuje liste punktów krzywej eliptycznej dla podanego a, b i p
def gen(a,b,p):
    result = []

    for x in range(p):
        for y in range(p):
            L = (y**2) % p
            P = (x**3 + a*x + b) % p
            # sprawdzenie czy punkt x,y spełnia nierówność y^3 = (x^2 + ax + b) % p
            if L == P:
                result.append([x, y])

    return result

if __name__ == '__main__':
    print(gen(-1, 0, 7) == [[0, 0], [1, 0], [4, 2], [4, 5], [5, 1], [5, 6], [6, 0]])
    print(gen(-1, 0, 11) == [[0, 0], [1, 0], [4, 4], [4, 7], [6, 1], [6, 10], [8, 3], [8, 8], [9, 4], [9, 7], [10, 0]])
    print(gen(-1, 1, 7) == [[0, 1], [0, 6], [1, 1], [1, 6], [2, 0], [3, 2], [3, 5], [5, 3], [5, 4], [6, 1], [6, 6]])
    print(gen(0, 2, 5) == [[2, 0], [3, 2], [3, 3], [4, 1], [4, 4]])
