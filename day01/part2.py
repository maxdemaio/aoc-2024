import os.path
from collections import Counter

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    list1 = []
    list2 = []
    counter = {}
    score = 0
    # set up lists with ints
    for line in lines:
        list1.append(int(line.split()[0]))
        list2.append(int(line.split()[1]))

    # set up count dict for count in list2
    counter = Counter(list2)

    # get score
    for num in list1:
        score += num * counter.get(num, 0)
    return score

# TODO: change for the small example given
INPUT_S = '''\
3   4
4   3
2   5
1   3
3   9
3   3
'''
EXPECTED = 31

def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0

if __name__ == '__main__':
    main()
