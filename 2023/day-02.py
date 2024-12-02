def part1(fh):
    game_num = 1
    allowed_games_sum = 0
    for line in fh:
        game_values = line.split(':')[-1]
        sets = game_values.split(';')
        allowed = True
        for set in sets:
            blue_sum, red_sum, green_sum = 0, 0, 0
            for pull in set.split(','):
                number, color = pull.split()
                number = int(number)
                if color == 'red':
                    red_sum += number
                    if red_sum > 12:
                        allowed = False
                        break
                elif color == 'green':
                    green_sum += number
                    if green_sum > 13:
                        allowed = False
                        break
                elif color == 'blue':
                    blue_sum += number
                    if blue_sum > 14:
                        allowed = False
                        break
            if not allowed:
                break

        if allowed:
            allowed_games_sum += game_num
        game_num += 1

    return allowed_games_sum

def part2(fh):
    power_sum = 0
    for line in fh:
        game_values = line.split(':')[-1]
        sets = game_values.split(';')
        max_blue, max_red, max_green = 0, 0, 0
        for set in sets:
            blue_sum, red_sum, green_sum = 0, 0, 0
            for pull in set.split(','):
                number, color = pull.split()
                number = int(number)
                if color == 'red':
                    red_sum += number
                    max_red = max(max_red, red_sum)
                elif color == 'green':
                    green_sum += number
                    max_green = max(max_green, green_sum)
                elif color == 'blue':
                    blue_sum += number
                    max_blue = max(max_blue, blue_sum)

        power_sum += max_red * max_green * max_blue

    return power_sum

def test(filename):
    with open(filename) as fh:
        print(part1(fh.read().strip().split('\n')))
    with open(filename) as fh:
        print(part2(fh.read().strip().split('\n')))

test('inputs/day-02-input.txt')