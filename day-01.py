def part1(fh):
    sum = 0
    for line in fh:
        nums = []
        for char in line:
            if char.isnumeric():
                nums.append(char)
            
        sum += int(nums[0] + nums[-1])
    
    return sum

def part2(fh):
    num_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    sum = 0
    for line in fh:
        nums = []
        for i, char in enumerate(line):
            if char.isnumeric():
                nums.append(char)
            
            for d, val in enumerate(num_words):
                if line[i:(i+len(val))] == val:
                    nums.append(str(d + 1))
                    break
        
        sum += int(nums[0] + nums[-1])
            
    return sum

def test(filename):
    with open(filename) as fh:
        print(part1(fh.read().strip().split('\n')))
        print(part2(fh.read().strip().split('\n')))
