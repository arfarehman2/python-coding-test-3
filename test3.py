students={
    "ali" : 40, "arfa" : 90 , "amna" : 79 , "faha" : 92 , "arowa" : 99
}
total=0
for score in students.values():
  total += score
average = total / len(students)
print("Average score of students is:", average)

highest_score = max(students.values())
lowest_score = min(students.values())

print("Highest score is:", highest_score)
print("Lowest score is:", lowest_score)

highest_scorer=max(students, key=students.get)
lowest_scorer=min(students, key=students.get)

name = input("Enter the name of the student to check their score: ")

grade = students.get(name.lower())
if grade is not None:
    print(f"{name} scored {grade}.")

else:
    print(f"{name} is not found in the records.")
