def part1(fh):
    card_sum = 0 
    for line in fh:
        split_line = line.split("|")
        winning_nums = split_line[0].split()
        your_nums = split_line[1].split()
        
        card_score = 0
        for num in your_nums:
            if num in winning_nums and card_score == 0:
                card_score = 1
            elif num in winning_nums:
                card_score *= 2

        card_sum += card_score
    
    return card_sum

def part2(fh):
    cards = 0
    copies = [1 for _ in range(len(fh))]
    for game, line in enumerate(fh):
        split_line = line.split("|")
        winning_nums = split_line[0].split()
        your_nums = split_line[1].split()

        matches = 0 
        for num in your_nums:
            if num in winning_nums:
                cards += copies[game]
                matches += 1
        
        for i in range(1, matches + 1):
            copies[game + i] += copies[game]
                
    
    return sum(copies)
        
            
        



def test(filename):
    with open(filename) as fh:
        print(part1(fh.read().strip().split('\n')))
    with open(filename) as fh:
        print(part2(fh.read().strip().split('\n')))

test('inputs/day-04-input.txt')