def solveDay01(inputs):
    temp = max(inputs)
    counter = 0
    for item in inputs:
        if item > temp:
            counter += 1
        temp = item
    return counter


def checkSum(sum1):
    if len(sum1) == 3:
        return True
    return False


def splitInputIntoSumOf3Elements(inputs):
    inputs_splitted = []
    counter = 0
    sum1 = []
    sum2 = []
    sum3 = []
    for item in inputs:
        if counter == 0:
            sum1.append(item)
            counter += 1
            continue
        if counter == 1:
            sum1.append(item)
            sum2.append(item)
            counter += 1
            continue

        sum1.append(item)
        sum2.append(item)
        sum3.append(item)
        if checkSum(sum1):
            inputs_splitted.append(sum(sum1))
            sum1 = []
        if checkSum(sum2):
            inputs_splitted.append(sum(sum2))
            sum2 = []
        if checkSum(sum3):
            inputs_splitted.append(sum(sum3))
            sum3 = []
        counter += 1

    print(inputs_splitted)
    return inputs_splitted


def solveDay01SecondChallenge(inputs):
    inputs_splitted = splitInputIntoSumOf3Elements(inputs)
    return solveDay01(inputs_splitted)


def parseDay01Input():
    inputs = []
    with open("../inputs/day01", 'r') as file:
        for line in file:
            stripped_line = int(line.strip())
            inputs.append(stripped_line)
    return inputs


if __name__ == '__main__':
    print(solveDay01(parseDay01Input()))
    print(solveDay01SecondChallenge(parseDay01Input()))
