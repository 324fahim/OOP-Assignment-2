 class Student:
    def __init__(self, name, roll_number, subjects, marks):
        self.name = name
        self.roll_number = roll_number
        self.subjects = subjects
        self.marks = marks

    def calculate_grade(self):
        total_marks = sum(self.marks)
        average_marks = total_marks / len(self.marks)
        if average_marks >= 90:
            return 'A'
        elif 80 <= average_marks < 90:
            return 'B'
        elif 70 <= average_marks < 80:
            return 'C'
        elif 60 <= average_marks < 70:
            return 'D'
        else:
            return 'F'

# Creating instances of the Student class
student1 = Student("Alice", "A001", ["Math", "Science", "History"], [88, 92, 75])
student2 = Student("Bob", "A002", ["English", "Physics", "Chemistry"], [79, 85, 91])

# Displaying student information
print(f"Student 1 Information:")
print(f"Name: {student1.name}")
print(f"Roll Number: {student1.roll_number}")
print(f"Subjects: {student1.subjects}")
print(f"Marks: {student1.marks}")
print(f"Grade: {student1.calculate_grade()}\n")

print(f"Student 2 Information:")
print(f"Name: {student2.name}")
print(f"Roll Number: {student2.roll_number}")
print(f"Subjects: {student2.subjects}")
print(f"Marks: {student2.marks}")
print(f"Grade: {student2.calculate_grade()}")
