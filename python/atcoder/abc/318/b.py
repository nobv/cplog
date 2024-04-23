N = int(input())
sheets = [list(map(int, input().split())) for _ in range(N)]
total = set()
for sheet in sheets:
    for x in [i for i in range(sheet[0], sheet[1])]:
        for y in [i for i in range(sheet[2], sheet[3])]:
            total.add((x, y))
print(len(total))
