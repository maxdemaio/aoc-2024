import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    levels = []
    safeCount = 0
    for line in lines:
        print(line)
        levels.append(list(map(int, line.split())))

    for level in levels:
        safe = True
        if level == sorted(level):
            # ascending
            i = 0
            j = 1
            while j < len(level):
                diff = level[j] - level[i]
                if diff > 3 or diff == 0:
                    safe = False
                    break
                i += 1
                j += 1
            if safe:
                safeCount += 1
        elif level == sorted(level, reverse=True):
            # descending
            i = 0
            j = 1
            while j < len(level):
                diff = level[i] - level[j]
                if diff > 3 or diff == 0:
                    safe = False
                    break
                i += 1
                j += 1
            if safe:
                safeCount += 1
        else:
            # unsafe, not increasing or decreasing
            continue

    return safeCount

# TODO: change for the small example given
INPUT_S = '''\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
'''
EXPECTED = 2


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0


if __name__ == '__main__':
    main()
