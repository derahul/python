__author__ = 'vishwakr'

line1 = [line.rstrip('\n') for line in open('file1', 'r')]
line2 = [line.rstrip('\n') for line in open('file2', 'r')]

with open('difference_items', 'w') as file_diff:
    for i in line1:
        if i not in line2:
            print(i)
            file_diff.write(i+'\n')

with open('common_items', 'w') as file_comm:
    for i in line1:
        if i in line2:
            print(i)
            file_comm.write(i+'\n')
