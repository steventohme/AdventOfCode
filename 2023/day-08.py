from math import gcd
import time
def lowestCommonMultiple(lst):
    lcm = lst[0]
    for i in lst[1:]:
        lcm = lcm*i//gcd(lcm, i)
    return lcm

def part1(fh):
    instructions = fh[0]

    nodes = fh[2:]
    nodes_dict = {}
    for node in nodes:
        node = node.split(' = ')

        nodes_dict[node[0]] = (node[1][1:4], node[1][6:-1])
    
    num_steps = 0
    curr_node = 'AAA'
    while True:
        for i in instructions:
            if i == 'R':
                curr_node = nodes_dict[curr_node][1]
            elif i == 'L':
                curr_node = nodes_dict[curr_node][0]
            
            num_steps += 1

            if curr_node == 'ZZZ':
                return num_steps

    

    


def part2(fh):
    instructions = fh[0]

    nodes = fh[2:]
    nodes_dict = {}
    curr_nodes = []
    for node in nodes:
        node = node.split(' = ')

        nodes_dict[node[0]] = (node[1][1:4], node[1][6:-1])

        if node[0][-1] == 'A':
            curr_nodes.append(node[0])
    
    num_steps = []
    for node in curr_nodes:
        node_num_steps = 0
        go = True
        curr_node = node
        while go:
            for i in instructions:
                if i == 'R':
                    curr_node = nodes_dict[curr_node][1]
                elif i == 'L':
                    curr_node = nodes_dict[curr_node][0]
                
                node_num_steps += 1
                if curr_node[-1] == 'Z':
                    num_steps.append(node_num_steps)
                    go = False
                    break
        
    return lowestCommonMultiple(num_steps)


def test(filename):
    with open(filename) as fh:
        print(part1(fh.read().strip().split('\n')))
    with open(filename) as fh:
        print(part2(fh.read().strip().split('\n')))

test('inputs/day-08-input.txt')