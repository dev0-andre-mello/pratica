line = input().split()
a = int(line[0])
b = int(line[1])
c = int(line[2])

MAIORAB = (a + b + abs(a - b)) / 2
MAIOR = (MAIORAB + c + abs(MAIORAB - c)) / 2
print(f'{MAIOR:.0f} eh o maior')
