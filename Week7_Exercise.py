values = open('grades.txt', 'r')

grade_dict = {}
for lines in values.readlines():
    temp_list = lines.split(':')
    grade_dict[float(temp_list[1])] = temp_list[0]


total = sum(grade_dict.keys())
print(total)
a = 'The name of the student with the highest grade is ' + str(grade_dict[max(grade_dict.keys())] + "\n")
b = 'The name of the student with the lowest grade is ' + str(grade_dict[min(grade_dict.keys())] + "\n")
c = 'The average grade of class is ' + str(total/len(grade_dict.keys())) + "\n"

print(a + b + c)

class_stats = open("class_stats.txt", "w")
class_stats.write(a)
class_stats.write(b)
class_stats.write(c)

