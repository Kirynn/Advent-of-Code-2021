import pathlib

input_file = pathlib.Path(__file__).parent / 'input.txt'

def printCard(card):

    print('\n'.join([str(r) for r in card]), end='\n\n')

def part1(cards, called):

    for number in called:

        for card in cards:

            for x, row in enumerate(card):

                for i, (num, call) in enumerate(row):

                    if num == number:

                        card[x][i] = (num, True)

                if all([el[1] for el in row]):

                    flat = [j[0] for sub in card for j in sub if not j[1]]
                    return sum(flat) * number

                for y in range(5):
                    col = [row[y] for row in card]

                    if all([el[1] for el in col]):

                        flat = [j[0] for sub in card for j in sub if not j[1]]
                        return sum(flat) * number


    return -1

def part2(cards, called):

    won = []

    for number in called:

        for card_index, card in enumerate(cards):

            if (card_index in won):
                pass

            for x, row in enumerate(card):
                
                for i, (num, call) in enumerate(row):

                    if num == number:

                        card[x][i] = (num, True)

                if all([el[1] for el in row]) and card_index not in won:
                    won.append(card_index)

                for y in range(5):
                    col = [row[y] for row in card]

                    if all([el[1] for el in col]) and card_index not in won:
                        won.append(card_index)

            if len(set(won)) == len(cards):

                flat = [j[0] for sub in card for j in sub if not j[1]]
                return sum(flat) * number

if __name__ == '__main__':

    with open(input_file, 'r') as file:

        called = [int(x) for x in file.readline().split(',')]

        cards = []
        working = []
        i = 1
        for line in file:
            if not (line.strip() == ''):
                values = [int(l) for l in line.strip('\n').split(' ') if not l == '']
                working.append([(i, False) for i in values])
                if not i % 5:
                    cards.append(working)
                    working = []
                i += 1

        print(part1(cards, called))
        print(part2(cards, called))

'''
Takeaway:
use numpy lol
'''