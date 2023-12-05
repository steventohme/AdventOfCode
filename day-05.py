def part1(fh):
    seeds = map(int, fh[0].split()[1:])
    for chunk in fh[1:]:
        ranges = []
        for line in chunk.split('\n')[1:]:
            destination, source, amount = map(int, line.split())
            ranges.append((destination, source, amount))
    
        new_seeds = []
        for x in seeds:
            for destination, source, amount in ranges:
                if x in range(source, source + amount):
                    new_seeds.append(x - source + destination)
                    break
            else:
                new_seeds.append(x)
        seeds = new_seeds
    

    return min(seeds)


def part2(fh):
    seeds = list(map(int, fh[0].split()[1:]))
    seed_ranges = []
    for i in range(0, len(seeds), 2):
        seed_ranges.append((seeds[i], seeds[i] + seeds[i + 1]))
    for chunk in fh[1:]:
        ranges = []
        for line in chunk.split('\n')[1:]:
            destination, source, amount = map(int, line.split())
            ranges.append((destination, source, amount))
    
        new_seed_ranges = []
        while len(seed_ranges) > 0:
            start, end = seed_ranges.pop()
            for destination, source, amount in ranges:
                startingOverlap = max(start, source)
                endingOverlap = min(end, source + amount)
                if startingOverlap < endingOverlap:
                    new_seed_ranges.append((startingOverlap - source + destination, endingOverlap - source + destination))
                    if start < startingOverlap:
                        seed_ranges.append((start, startingOverlap))
                    if endingOverlap < end:
                        seed_ranges.append((endingOverlap, end))
                    break
            else:
                new_seed_ranges.append((start, end))
        seed_ranges = new_seed_ranges
    
    return min(seed_ranges)



def test(filename):
    with open(filename) as fh:
        print(part1(fh.read().strip().split('\n\n')))
    with open(filename) as fh:
        print(part2(fh.read().strip().split('\n\n')))

test('test.txt')