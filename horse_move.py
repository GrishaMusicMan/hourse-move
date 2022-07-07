from horse_say import horse

n = 8
matrix = [['.']*n for _ in range(8)]
letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
# coord = input()
coord = 'f3'

one = int(coord[1])-1
two = letters.index(coord[0])
matrix[one][two] = 'N'
chg = (-2, -1, 1, 2)

for i in chg:
    for j in chg[::-1]:
        if abs(i) != abs(j) and one+i in range(n) and two+j in range(n):
            matrix[one+i][two+j] = '*'

for row in matrix[::-1]:
    print(*row)
