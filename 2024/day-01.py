def part1(fh):
    left_values = []
    right_values = []

    for item in fh:
        left, right = map(int, item.split())
        left_values.append(left)
        right_values.append(right)

    left_values.sort()
    right_values.sort()

    result = 0    
    for i in range(len(left_values)):
        result += abs(left_values[i] - right_values[i])
    
    return result

def part2(fh):
    left_values = set()
    right_values = []

    for item in fh:
        left, right = map(int, item.split())
        left_values.add(left)
        right_values.append(right)

    result = 0 
    for item in left_values:
        result += item * right_values.count(item)
    
    return result

def test(filename):
    with open(filename) as fh:
        print(part1(fh.read().strip().split('\n')))
    with open(filename) as fh:
        print(part2(fh.read().strip().split('\n')))

test('2024/inputs/day-01-input.txt')