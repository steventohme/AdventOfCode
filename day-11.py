def part1(fh):
    empty_rows = [r for r, row in enumerate(fh) if all(char == '.' for char in row)]
    empty_cols = [c for c, col in enumerate(zip(*fh)) if all(char == '.' for char in col)]
    points = [(r, c) for r, row in enumerate(fh) for c, char in enumerate(row) if char == '#']

    total = 0

    for i, (r1, c1) in enumerate(points):
        for (r2,c2) in points[:i]:
            for r in range(min(r1, r2), max(r1, r2)):
                total += 2 if r in empty_rows else 1
            for c in range(min(c1, c2), max(c1,c2)):
                total += 2 if c in empty_cols else 1

    return total
        

def part2(fh):
    empty_rows = [r for r, row in enumerate(fh) if all(char == '.' for char in row)]
    empty_cols = [c for c, col in enumerate(zip(*fh)) if all(char == '.' for char in col)]

    points = [(r, c) for r, row in enumerate(fh) for c, char in enumerate(row) if char == '#']

    total = 0
    for i, (r1,c1) in enumerate(points):
        for (r2,c2) in points[:i]:
            for r in range(min(r1, r2), max(r1, r2)):
                total += 1000000 if r in empty_rows else 1
            for c in range(min(c1, c2), max(c1,c2)):
                total += 1000000 if c in empty_cols else 1

    return total

def test(filename):
    with open(filename) as fh:
        print(part1(fh.read().strip().split('\n')))
    with open(filename) as fh:
        print(part2(fh.read().strip().split('\n')))

test('inputs/day-11-input.txt')