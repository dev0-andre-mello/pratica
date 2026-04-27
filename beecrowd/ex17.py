value_of_n = int(input())

inn = 0

out = 0

for _ in range(value_of_n):
    value = int(input())
    if 10 <= value <= 20:
        inn += 1
    else:
        out += 1
print(f"{inn} in")
print(f"{out} out")
