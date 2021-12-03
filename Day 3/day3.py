def most_common(lst):
    return max(set(lst), key=lst.count)

def least_common(lst):
    return min(set(lst), key=lst.count)

def part1(values):

    c = [[values[j][i] for j in range(len(values))] for i in range(12)]
    g = int(''.join([most_common(i) for i in c]), 2)
    e = int(''.join([least_common(i) for i in c]), 2)

    return g * e


def part2(values):

    oxygen = values[:]
    for i in range(12):
        col = [row[i] for row in oxygen]
        check = '1' if col.count('1') == col.count('0') else most_common(col)
        oxygen = list(filter(lambda num: num[i] == check, oxygen))

    carbon = values[:]
    for i in range(12):
        col = [row[i] for row in carbon]
        check = '0' if col.count('1') == col.count('0') else least_common(col)
        carbon = list(filter(lambda num: num[i] == check, carbon))

    oxygen = int(''.join(oxygen), 2)
    carbon = int(''.join(carbon), 2)

    return oxygen * carbon

if __name__ == '__main__':

    with open('input.txt', 'r') as file:

        values = [str(v).strip() for v in file]

    print(part1(values))
    print(part2(values))