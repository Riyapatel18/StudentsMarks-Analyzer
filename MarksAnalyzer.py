# Dictionary to store student marks
marks = {}

n = int(input("Enter number of students: "))

# Taking input from user
for i in range(n):
    name = input("Enter student name: ")
    m1 = int(input("Enter marks in Math: "))
    m2 = int(input("Enter marks in Science: "))
    m3 = int(input("Enter marks in English: "))
    
    marks[name] = [m1, m2, m3]

print("\n--- Student Averages ---")

# Student-wise average
for name in marks:
    avg = sum(marks[name]) / 3
    print(f"{name} → Average: {avg:.2f}")

# Finding Topper
max_total = 0
topper = ""

for name in marks:
    total = sum(marks[name])
    if total > max_total:
        max_total = total
        topper = name

print(f"\nTopper: {topper} with {max_total} marks")

# Subject-wise averages
math_total = 0
science_total = 0
english_total = 0

for name in marks:
    math_total += marks[name][0]
    science_total += marks[name][1]
    english_total += marks[name][2]

students = len(marks)

print("\nSubject-wise averages:")
print(f"Math: {math_total / students:.1f}")
print(f"Science: {science_total / students:.1f}")
print(f"English: {english_total / students:.1f}")