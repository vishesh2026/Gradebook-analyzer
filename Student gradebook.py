class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.grades = {}  # Use a dictionary to store grades by subject

    def add_grade(self, subject, score):
        self.grades[subject] = score

    def get_average(self):
        if not self.grades:
            return 0
        total_score = sum(self.grades.values())
        return total_score / len(self.grades)

class Gradebook:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def find_student(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                return student
        return None

    def list_students(self):
        for student in self.students:
            print(f"{student.roll_number}: {student.name}")

    def remove_student(self, roll_number):
        student = self.find_student(roll_number)
        if student:
            self.students.remove(student)
            print(f"Student {student.name} removed.")
        else:
            print("Student not found!")

    def display_student_grades(self, roll_number):
        student = self.find_student(roll_number)
        if student:
            print(f"Grades for {student.name} (Roll Number: {student.roll_number}):")
            for subject, score in student.grades.items():
                print(f"{subject}: {score}")
        else:
            print("Student not found!")

def main():
    gradebook = Gradebook()

    while True:
        print("\nStudent Gradebook Menu:")
        print("1. Add Student")
        print("2. Add Grade")
        print("3. Calculate Average")
        print("4. List Students")
        print("5. Remove Student")
        print("6. Display Student Grades")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            roll_number = input("Enter student roll number: ")
            student = Student(name, roll_number)
            gradebook.add_student(student)
            print(f"Student {name} added successfully!")

        elif choice == "2":
            roll_number = input("Enter student roll number: ")
            student = gradebook.find_student(roll_number)
            if student:
                subject = input("Enter subject: ")
                score = float(input("Enter score: "))
                student.add_grade(subject, score)
                print(f"Grade added for {student.name} in {subject}")
            else:
                print("Student not found!")

        elif choice == "3":
            roll_number = input("Enter student roll number: ")
            student = gradebook.find_student(roll_number)
            if student:
                average = student.get_average()
                print(f"Average score for {student.name}: {average}")
            else:
                print("Student not found!")

        elif choice == "4":
            gradebook.list_students()

        elif choice == "5":
            roll_number = input("Enter student roll number to remove: ")
            gradebook.remove_student(roll_number)

        elif choice == "6":
            roll_number = input("Enter student roll number to display grades: ")
            gradebook.display_student_grades(roll_number)

        elif choice == "7":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
