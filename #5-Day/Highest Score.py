# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
st = student_scores[0]
for ind in student_scores[1:]:
    if st>ind:
        continue
    else:  
        st = ind
print(f"The highest score in the class is: {st}")

#print(f"The highest score in the class is: {max(student_scores)}")


