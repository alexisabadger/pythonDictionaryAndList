# This code makes a nested list.

row = 6
column = 2

x = []
for j in range(row):
    x.append([0 for i in range(column)])

print(x)



# Print output: [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

# x = [[0 for i in range(column)] for j in range(row)]
# print(x)
# https://stackoverflow.com/questions/35437028/understanding-creating-a-2d-list-with-nested-loops