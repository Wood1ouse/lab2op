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
new_file.close()


points = dict()
countries = 0
with open('sum.csv') as summer:
    for line in summer:
        array = line.split(',')
        country = array[0]
        points[country] = 0
        countries += 1


for i in range(1, countries + 1):
    votes = []
    with open('sum.csv') as summer:
        for line in summer:
            array = line.split(',')
            votes.append([array[i], array[0]])
        votes.sort(reverse=True)
        prize = 12
        for place in range(10):
            if place < 2:
                points[votes[place][1]] += prize
                prize -= 2
            else:
                points[votes[place][1]] += prize
                prize -= 1

array_of_points = []
for k, v in points.items():
    array_of_points.append([v, k])

array_of_points.sort(reverse=True)
adequate_view = []
for i in range(len(array_of_points)):
    adequate_view.append([array_of_points[i][1], array_of_points[i][0]])

with open('results.csv', 'w') as result_file:
    num = 0
    for country, points in adequate_view:
        if num == 10:
            break
        result_file.write(f"{country};{points}\n")
        print(country, ':', points)
        num += 1
