# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
# input: 156 178 165 171 187
# 2nd input: 180 124 165 173 189 169 146
no_of_students = 0
height_sum = 0
for h in student_heights:
    height_sum += h
    no_of_students += 1
print(no_of_students)
height_average = round(height_sum / no_of_students)

print(height_average)

