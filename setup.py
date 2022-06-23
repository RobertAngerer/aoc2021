import requests

cookie = {
    'Cookie': "ru=53616c7465645f5f3eab3df743bf95b5e5a6a212352f5d9cdf3656e39be7600754fbf45024d84ed5cb97ff002cf3519d; session=53616c7465645f5f872c728a15b44ec4562d28494cd3ece3347a7f5ab5dbb5a534d0e3b118e6098988bfa51726143dec32fdae6829e434c31a44917e079c293d"}
aocBaseURL = "https://adventofcode.com/2021/day/"


def getInputData(day):
    requests.get(aocBaseURL + day + "/input", cookies=cookie)


def saveInputDataToFile(day):
    save_file_location = "inputs/day"
    if day < 10:
        save_file_location += "0"
    save_file_location += str(day)
    with open(save_file_location, "w+") as file:
        file.write(requests.get(aocBaseURL + str(day) + "/input", cookies=cookie).text)


def sendAnswer(day, level, answer):
    body = {"level": level, "answer": answer}
    response = requests.post(aocBaseURL + str(day) + "/answer", cookies=cookie, data=body)
    print(response.text)
