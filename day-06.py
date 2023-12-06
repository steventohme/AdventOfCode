import time
def part1(fh):
    time_line = fh[0].split()[1:]
    distance_line = fh[1].split()[1:]

    product = 1
    
    for i in range(len(time_line)):
        time = int(time_line[i])
        record = int(distance_line[i])
        num = 0
        in_range = False
        for j in range(time + 1):
            distance_traveled = j * (time - j)
            if distance_traveled > record:
                num += 1
                in_range = True
            elif distance_traveled < record and in_range:
                break
        product *= num

    return product
                


def part2(fh):
    time = int(''.join(fh[0].split()[1:]))
    distance = int(''.join(fh[1].split()[1:]))
    
    num = 0
    in_range = False
    for i in range(time + 1):
        distance_traveled = i * (time - i)
        if distance_traveled > distance:
            num += 1
            in_range = True
        elif distance_traveled < distance and in_range:
            break

    return num

def test(filename):
    with open(filename) as fh:
        print(part1(fh.read().strip().split('\n')))
    with open(filename) as fh:
        print(part2(fh.read().strip().split('\n')))
        

test ('inputs/day-06-input.txt')