def part1(fh):
    def safety_check(report):
        previous = report[0]
        increasing = True if report[1] > report[0] else False

        for item in report[1:]:
            if item == previous or abs(item - previous) > 3:
                return False
            if increasing and item < previous or not increasing and item > previous:
                return False

            previous = item
        
        return True

    result = 0
    for report in fh:
        report = list(map(int, report.split()))
        if safety_check(report):
            result += 1
    
    return result

def part2(fh):
    def safety_check(report):
        previous = report[0]
        increasing = True if report[1] > report[0] else False

        for item in report[1:]:
            if item == previous or abs(item - previous) > 3:
                return False
            if increasing and item < previous or not increasing and item > previous:
                return False

            previous = item
        
        return True

    def is_safe_with_removal(report):
        for i in range(len(report)):
            # Create a new report with one level removed
            modified_report = report[:i] + report[i+1:]
            if safety_check(modified_report):
                return True
        return False

    result = 0
    for report in fh:
        report = list(map(int, report.split()))
        if safety_check(report) or is_safe_with_removal(report):
            result += 1
    
    return result

def test(filename):
    with open(filename) as fh:
        print(part1(fh.read().strip().split('\n')))
    with open(filename) as fh:
        print(part2(fh.read().strip().split('\n')))

test('2024/inputs/day-02-input.txt')