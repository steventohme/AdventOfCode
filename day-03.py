def is_adjacent(num_position, symbol_position):
    num_row, num_start, num_end = num_position
    sym_row, sym_col = symbol_position

    return (sym_row in {num_row - 1, num_row + 1} and num_start - 1 <= sym_col <= num_end + 1) or \
           (sym_col in {num_start - 1, num_end + 1} and sym_row == num_row)

def part1(fh):
    number_positions = {} # format: {number: [[y, startx, endx]]}
    symbol_positions = []# y, x
    for row, line in enumerate(fh):
        col = 0
        while col < len(line):
            if line[col].isdigit():
                num = line[col]
                j = col + 1
                while j < len(line) and line[j].isdigit():
                    num += line[j]
                    j += 1
                
                if num not in number_positions:
                    number_positions[num] = [[row, col, j - 1]]
                else:
                    number_positions[num].append([row, col, j - 1])

                
                col = j
            elif line[col] != '.':
                symbol_positions.append([row, col])
                col += 1
            else:
                col += 1
    
    
    part_number_sum = 0
    for number, positions in number_positions.items():
        for position in positions:
            if any(is_adjacent(position, symbol) for symbol in symbol_positions):
                part_number_sum += int(number)
    
    return part_number_sum


def part2(fh):
    number_positions = {} # format: {number: [[y, startx, endx]]}
    symbol_positions = []# y, x
    for row, line in enumerate(fh):
        col = 0
        while col < len(line):
            if line[col].isdigit():
                num = line[col]
                j = col + 1
                while j < len(line) and line[j].isdigit():
                    num += line[j]
                    j += 1
                
                if num not in number_positions:
                    number_positions[num] = [[row, col, j - 1]]
                else:
                    number_positions[num].append([row, col, j - 1])

                
                col = j
            elif line[col] != '.':
                symbol_positions.append([row, col])
                col += 1
            else:
                col += 1

    gear_ratio_sum = 0
    for symbol in symbol_positions:
        adjacent_numbers = [number for number, positions in number_positions.items() 
                            for position in positions if is_adjacent(position, symbol)]
        if len(adjacent_numbers) == 2:
            gear_ratio_sum += int(adjacent_numbers[0]) * int(adjacent_numbers[1])
    
    return gear_ratio_sum

            
        
def test(filename):
    with open(filename) as fh:
        print(part1(fh.read().strip().split('\n')))
    with open(filename) as fh:
        print(part2(fh.read().strip().split('\n')))

test('./inputs/day-03-input.txt')