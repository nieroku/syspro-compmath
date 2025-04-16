import os

PRECISION = float(os.getenv("PRECISION", 0.00001))
SYMBOLS = os.getenv("SYMBOLS", "0#*")
STEP = float(os.getenv("STEP", 0.1))
POWER = len(SYMBOLS)


def find_root(z):
    while abs(z ** POWER - 1) > PRECISION:
        z -= ((z ** POWER) - 1) / (POWER * (z ** (POWER - 1)))
    return z


def main():
    half_width, half_height = (dim // 2 for dim in os.get_terminal_size())

    roots = []
    basins = []
    for y in range(-half_height, half_height):
        basins.append([])
        for x in range(-half_width, half_width):
            if x == 0 and y == 0:
                basins[-1].append(' ')
                continue
            root = find_root(complex(x * STEP, y * STEP))
            i = 0
            while i < len(roots):
                if abs(root - roots[i]) <= PRECISION:
                    break
                i += 1
            else:
                roots.append(root)
            basins[-1].append(SYMBOLS[i])

    print(*("".join(row) for row in basins), sep='\n', end="")


if __name__ == "__main__":
    main()
    input()
