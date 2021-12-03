# Day one of Advent of Code 2021

data = []
with open('src/day-1/data.csv', 'r', encoding='utf-8') as f:
    for row in f:
        data.append(int(row))

count = 0

for i, j in zip(data, data[1:]):
    if j > i:
        count += 1

print(count)