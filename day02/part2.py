import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def isSafe(level: list[int]) -> bool:
    if level[1] < level[0]:
        direction = -1
    else:
        direction = 1

    for n1, n2 in zip(level, level[1:]):
        diff = direction * (n2 - n1)
        if not (1 <= diff <= 3):
            return False
    else:
        return True
    
def solve(s: str) -> int:
    lines = s.splitlines()
    levels = []
    safeCount = 0

    # parse input
    for line in lines:
        levels.append(list(map(int, line.split())))

    for level in levels:
        if isSafe(level):
            safeCount += 1
        else:
            for i in range(len(level)):
                newLevel = level[:i] + level[i + 1:]
                if isSafe(newLevel):
                    safeCount += 1
                    break
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
EXPECTED = 4


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0


if __name__ == '__main__':
    main()
