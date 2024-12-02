def bfs(matrix, position, distance):
    compatible = {
    (-1,0): ['|', '7', 'F'],
    (0, 1): ['-', 'J', '7'],
    (1, 0): ['|', 'L', 'J'],
    (0, -1): ['-', 'L', 'F'],
    }
    pipe_type = {
    'S': ((1, 0), (0, 1), (-1, 0), (0, -1)),
    '|': ((1, 0), (-1, 0)),
    '-': ((0, 1), (0, -1)),
    'L': ((-1, 0), (0, 1)),
    'J': ((-1, 0), (0, -1)),    
    '7': ((1, 0), (0, -1)),
    'F': ((1, 0), (0, 1)),
    }   
    queue = [(position, distance)]
    visited = {}
    while queue:
        if len(queue[0]) == 2:
            position, distance = queue.pop(0)
        else:
            direction, position, distance = queue.pop(0)
        
        if position in visited:
            continue
        
        x, y = position
        if x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix[0]):
            continue
        
        if matrix[x][y] == 'S':
            visited[position] = distance
            for move in pipe_type['S']:
                queue.append((move, (x + move[0], y + move[1]), distance + 1))

        elif matrix[x][y] in compatible[direction]:
            visited[position] = distance
            if matrix[x][y] in pipe_type:
    
                for move in pipe_type[matrix[x][y]]:
                    queue.append((move, (x + move[0], y + move[1]), distance + 1))
        

        
    return distance, visited

def part1(fh):
    

    matrix = []

    for i, line in enumerate(fh):
        row = []
        for j, char in enumerate(line):
            row.append(char)
            if char == 'S':
                start = (i, j)
        matrix.append(row)

    distance, _ = bfs(matrix, start, 0)

    return distance - 1

    

def part2(fh):  
    def replace_S(matrix, coordinates):
        compatible = {
        (-1,0): ['|', '7', 'F'],
        (0, 1): ['-', 'J', '7'],
        (1, 0): ['|', 'L', 'J'],
        (0, -1): ['-', 'L', 'F'],
        }
        reverse_compatible = {
        (1,0): ['|', '7', 'F'],
        (0, -1): ['-', 'J', '7'],
        (-1, 0): ['|', 'L', 'J'],
        (0, 1): ['-', 'L', 'F'],
        }

        connected_directions = []
        for direction in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            x, y = coordinates
            x += direction[0]
            y += direction[1]
            pipe = matrix[x][y]
            if pipe in compatible[direction]:
                connected_directions.append(direction)
        
        pipe = set(reverse_compatible[connected_directions[0]]) & set(reverse_compatible[connected_directions[1]])

        matrix[coordinates[0]][coordinates[1]] = list(pipe)[0]

        
    matrix = []
    for i, line in enumerate(fh):
        row = []
        for j, char in enumerate(line):
            row.append(char)
            if char == 'S':
                start = (i, j)
        matrix.append(row)

    _, visited = bfs(matrix, start, 0)
    replace_S(matrix, start)
    w = len(matrix[0])
    h = len(matrix)
    in_pipe = 0
    for y, line in enumerate(matrix):
        for x, char in enumerate(line):
            if (y, x) in visited:
                continue

            crosses = 0
            x2, y2 = x, y

            while x2 < w and y2 < h:
                char2 = matrix[y2][x2]
                if (y2, x2) in visited and char2 != 'L' and char2 != '7':
                    crosses += 1
                x2 += 1
                y2 += 1
            
            if crosses % 2 == 1:
                in_pipe += 1
    return in_pipe
    


def test(filename):
    with open(filename) as fh:
        print(part1(fh.read().strip().split('\n')))
    with open(filename) as fh:
        print(part2(fh.read().strip().split('\n')))

test('inputs/day-10-input.txt')