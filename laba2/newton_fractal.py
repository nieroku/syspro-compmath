import os

PRECISION = 0.00001
SYMBOLS = "0#*"


def find_root(z):
    while abs(z ** 3 - 1) > PRECISION:
        z -= ((z ** 3) - 1) / (3 * z * z)
    return z


def main():
    half_width, half_height = (dim // 2 for dim in os.get_terminal_size())

    roots = []
    basins = []
    for y in range(-half_height, half_height + 1):
        if y == 0:
            continue
        basins.append([])
        for x in range(-half_width, half_width + 1):
            if x == 0:
                continue
            root = find_root(complex(x / 10, y / 10))
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
