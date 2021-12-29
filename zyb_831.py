# existing code
mult_table = [
[1, 2, 3],
[2, 4, 6],
[3, 6, 9]
]

# my code
#   |
#  \|/
#   V

x = '| '
rowlen = len(mult_table) - 1

# print(x, rowlen) # testing values

for row in mult_table:
    for cell in row[0:rowlen]:
        print(cell, '{}'.format(x), end='')
    print(row[rowlen])
