t = int(input('Correct type of tea: '))

answers = list(map(int, input('Answers: ').split()))

print(answers.count(t))
