inputs = []
def solveDay01():
    temp = max(inputs)
    counter = 0
    for item in inputs:
        if item > temp:
            counter += 1
        temp = item
    return counter


def parseDay01Input():
    with open("../inputs/day01", 'r') as file:
        for line in file:
            stripped_line = int(line.strip())
            inputs.append(stripped_line)

if __name__ == '__main__':
    parseDay01Input()
    print(solveDay01())


