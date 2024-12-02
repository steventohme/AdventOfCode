import heapq
# returns rank of hand and first card type

class Cards_part1:

    def __init__(self, cards, bid):
        self.cards = cards
        self.rank = self.determine_hand_type()
        self.bid = bid
    
    def determine_hand_type(self):
        card_counts = {card: self.cards.count(card) for card in self.cards}
        sorted_counts = sorted(card_counts.values(), reverse=True)

        if sorted_counts[0] == 5:
            rank = 5
        elif sorted_counts[0] == 4:
            rank = 4  # Four of a kind
        elif sorted_counts[0] == 3 and sorted_counts[1] == 2:
            rank = 3.5 # Full house
        elif sorted_counts[0] == 3:
            rank = 3  # Three of a kind
        elif sorted_counts[0] == 2 and sorted_counts[1] == 2:
            rank = 2.5  # Two pair
        elif sorted_counts[0] == 2:
            rank = 2  # One pair
        else:
            rank = 1 # High card
        return rank
    
    def __lt__(self, other):
        if self.rank != other.rank:
            return self.rank < other.rank
        
        num_mapping = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7':7, '8': 8, '9': 9}

        i = 0
        while i < 5 and num_mapping[self.cards[i]] == num_mapping[other.cards[i]]:
            i += 1
        
        return num_mapping[self.cards[i]] < num_mapping[other.cards[i]]

class Cards_part2:

    def __init__(self, cards, bid):
        self.cards = cards
        self.rank = self.determine_hand_type()
        self.bid = bid
    
    def determine_hand_type(self):
        card_counts = {card: self.cards.count(card) for card in self.cards if card != 'J'}
        joker_count = self.cards.count('J')
        sorted_counts = sorted(card_counts.values(), reverse=True)
        

        if joker_count == 5 or sorted_counts[0] == 5:
            return 5
        elif sorted_counts[0] == 4:
            return 4 + joker_count
        elif sorted_counts[0] == 3 and len(sorted_counts) >= 2 and sorted_counts[1] == 2:
            return 3.5
        elif sorted_counts[0] == 3:
            return 3 + joker_count
        elif sorted_counts[0] == 2 and len(sorted_counts) >= 2 and sorted_counts[1] == 2:
            return 2.5 + joker_count
        elif sorted_counts[0] == 2:
            return 2 + joker_count
        else:
            return 1 + joker_count
    
    def __lt__(self, other):
        if self.rank != other.rank:
            return self.rank < other.rank
        

        num_mapping = {'T': 10, 'J': 1, 'Q': 12, 'K': 13, 'A': 14, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7':7, '8': 8, '9': 9}

        i = 0
        while num_mapping[self.cards[i]] == num_mapping[other.cards[i]] and i < 4 :
            i += 1
        
        return num_mapping[self.cards[i]] < num_mapping[other.cards[i]]

def part1(fh):
    hands = []
    for line in fh:
        cards = Cards_part1(line.split()[0], int(line.split()[1]))
        heapq.heappush(hands, cards)
    
    win_total = 0
    for i in range(1, len(hands) + 1):
        cards = heapq.heappop(hands)
        win_total += cards.bid*i
    
    return win_total


def part2(fh):
    hands = []
    for line in fh:
        cards = Cards_part2(line.split()[0], int(line.split()[1]))
        heapq.heappush(hands, cards)
    
    win_total = 0
    for i in range(1, len(hands) + 1):
        cards = heapq.heappop(hands)
        win_total += cards.bid*i
    
    return win_total


def test(filename):
    with open(filename) as fh:
        print(part1(fh.read().strip().split('\n')))
    with open(filename) as fh:
        print(part2(fh.read().strip().split('\n')))
        

test ('inputs/day-07-input.txt')