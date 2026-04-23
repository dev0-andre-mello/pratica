line = input().split()

code = int(line[0])
quantity = int(line[1])

price = [0, 4.00, 4.50, 5.00, 2.00, 1.50]

total = price[code] * quantity

print(f'Total: R$ {total:.2f}')
