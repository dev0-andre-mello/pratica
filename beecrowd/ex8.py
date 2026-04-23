line1 = input().split()

x1 = float(line1[0])
y1 = float(line1[1])

line2 = input().split()

x2 = float(line2[0])
y2 = float(line2[1])

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print(f"{distance:.4f}")
