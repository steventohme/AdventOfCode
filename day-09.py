def absolute_differences_last(lst):
    differences = []
    for i in range(len(lst)-1):
        differences.append(int(lst[i+1]) - int(lst[i]))
    all_same = all(difference == 0 for difference in differences)
    last_value = int(lst[-1]) if lst else None
    return differences, all_same, last_value

def absolute_differences(lst, last):
    differences = []
    for i in range(len(lst)-1):
        differences.append(int(lst[i+1]) - int(lst[i]))
    all_same = all(difference == 0 for difference in differences)
    if last:
        return differences, all_same, int(lst[-1]) if lst else None
    return differences, all_same, int(lst[0]) if lst else None

def part1(fh):
    sum_last_values = 0
    for line in fh:
        last_values = []
        differences, all_same, last_value = absolute_differences(line.split(), True)
        while not all_same:
            last_values.append(last_value)
            differences, all_same, last_value = absolute_differences(differences, True)
        
       
        
        sum_last_values += sum(last_values) + last_value
    
    return sum_last_values

def part2(fh):
    sum_first_values=  0
    for line in fh:
        first_values = []
        differences, all_same, first_value = absolute_differences(line.split(), False)
        while not all_same:
            first_values.append(first_value)
            differences, all_same, first_value = absolute_differences(differences, False)

        for i in range(1, len(first_values) + 1):
            first_value = first_values[-i] - first_value

        sum_first_values += first_value
    
    return sum_first_values

def test(filename):
    with open(filename) as fh:
        print(part1(fh.read().strip().split('\n')))
    with open(filename) as fh:
        print(part2(fh.read().strip().split('\n')))

test('inputs/day-09-input.txt')