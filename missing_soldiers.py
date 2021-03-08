barries = int(input())

d = []
x_cord = []
overlap = 0

for _ in range(barries):
    takes = list(map(int, input().split(" ")))
    x_cord.append([takes[0], takes[0] + takes[2]])
    d.append(takes[2])

x_cord.sort(key=lambda x : x[0])

final = [x1 for x in x_cord for x1 in x]

i = 1
while i < len(final):
    if (i + 1 < len(final)):
        if final[i] < final[i +1]:
            overlap += final[i] - final[i + 1] + 1
        elif final[i + 1] < final[i]:
        	pass
        elif final[i] == final[i + 1]:
        	pass
    i += 2


print(max(final) + overlap - final[0] + 1)
