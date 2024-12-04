import re

def findmult(multString):
    pattern = re.compile(r'\((\d+),(\d+)\)')
    match = pattern.match(multString)
    if match:
        x, y = map(int, match.groups())
        return x * y
    else:
        return 0
def part1(fh):
    result = 0
    for mult in fh:
        mult_list = mult.split('mul') 
        for mult_string in mult_list:
            result += findmult(mult_string)
    
    return result
    
        

def part2(fh):
    result = 0
    enabled = True
    for line in fh:
        segments = line.split('mul')
        prev = segments[0] 
        for segment in segments:
            if 'do()' in prev:
                enabled = True
            elif "don't()" in prev:
                enabled = False
            if enabled:
                result += findmult(segment)
            
            prev = segment
    return result   

def test(filename):
    with open(filename) as fh:
        print(part1(fh.read().strip().split('\n')))
    with open(filename) as fh:
        print(part2(fh.read().strip().split('\n')))

test('2024/inputs/day-03-input.txt')