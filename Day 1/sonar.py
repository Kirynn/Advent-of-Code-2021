from typing import List


from typing import List

def part1(values: List[int]) -> int:

    count = 0
    for i, val in enumerate(values):
        if (i > 0 and val > values[i-1]): count += 1

    return count

def part2(values: List[int]) -> int:

    three_sums = []
    for i in range(len(values)):
        if (i+2 < len(values)):
            val = values[i] + values[i+1] + values[i+2]
            three_sums.append(val)
    return part1(three_sums)

if __name__ == '__main__':

    with open('input.txt', 'r') as file:

        values = [int(line.strip()) for line in file]
        
        print(f'There are {part1(values)} values that are larger then their previous value.')
        print(f'There are {part2(values)} values that are larger then their previous value when using a three sliding window.')
