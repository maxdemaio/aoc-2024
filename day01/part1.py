import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    list1 = []
    list2 = []
    for line in lines:
        list1.append(int(line.split()[0]))
        list2.append(int(line.split()[1]))
    # TODO: implement solution here!
    list1.sort()
    list2.sort()
    sum = 0
    for i in range(len(list1)):
        if list1[i] > list2[i]:
            sum += list1[i] - list2[i]
        else:
            sum += list2[i] - list1[i]
    return sum

# TODO: change for the small example given
INPUT_S = '''\
3   4
4   3
2   5
1   3
3   9
3   3
'''
EXPECTED = 11


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0

if __name__ == '__main__':
    main()
