students = [['Joe', 'Kim', ''], ['Sam', 'Sue', ''], ['Kelly', 'Chris', '']]
# print(students[0][1])

for x in students:
    index = 0
    print(x[index])

year = 1950
for x in students:
    if x[0] != 'there is a better way to do this but I am not sure how':        
        x[2] = year
        year += 1

print(students)


# https://stackoverflow.com/questions/51318249/python-how-do-i-replace-value-in-a-nested-list

