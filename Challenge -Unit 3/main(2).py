class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    # Sort the list of students in descending order of CGPA
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

# Example usage:
student1 = Student("Alice", "001", 3.8)
student2 = Student("Bob", "002", 3.6)
student3 = Student("Charlie", "003", 3.9)
student4 = Student("David", "004", 3.7)

students = [student1, student2, student3, student4]

sorted_students = sort_students(students)

# Printing the sorted list of students
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, Average: {student.cgpa}")

# Output:
# Name: Charlie, Roll Number: 003, CGPA: 3.9
# Name: Alice, Roll Number: 001, CGPA: 3.8
# Name: David, Roll Number: 004, CGPA: 3.7
# Name: Bob, Roll Number: 002, CGPA: 3.6
