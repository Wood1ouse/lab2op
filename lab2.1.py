import os
dir = os.path.relpath('resources')
new_file = open('sum.csv', 'w')
files = ('1.csv', '2.csv')
for csv in files:
    with open('{0}/{1}'.format(dir, csv)) as file:
        num_line = 1
        for line in file:
            if num_line == 1:
                num_line += 1
                continue
            new_file.write(line)
