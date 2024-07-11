# class_management.py

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def get_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)

class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        for student in self.students:
            print(f"Student Name: {student.name}, Grades: {student.grades}")

    def get_student_average(self, student_name):
        for student in self.students:
            if student.name == student_name:
                return student.get_average_grade()
        return None

    def get_class_average(self, subject):
        total = 0
        count = 0
        for student in self.students:
            if subject in student.grades:
                total += student.grades[subject]
                count += 1
        if count == 0:
            return 0
        return total / count

def main():
    classroom = Classroom()

    try:
        while True:
            print("\n1. Add a student")
            print("2. Display all students")
            print("3. Get the average grade of a student")
            print("4. Get the class average for a subject")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                name = input("Enter student's name: ")
                student = Student(name)
                while True:
                    subject = input("Enter subject (or 'done' to finish): ")
                    if subject.lower() == 'done':
                        break
                    grade = float(input(f"Enter grade for {subject}: "))
                    student.add_grade(subject, grade)
                classroom.add_student(student)
            elif choice == '2':
                classroom.display_students()
            elif choice == '3':
                name = input("Enter student's name to get average grade: ")
                avg = classroom.get_student_average(name)
                if avg is not None:
                    print(f"Average grade for {name}: {avg}")
                else:
                    print("Student not found.")
            elif choice == '4':
                subject = input("Enter subject to get class average: ")
                avg = classroom.get_class_average(subject)
                print(f"Class average for {subject}: {avg}")
            elif choice == '5':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")
    except KeyboardInterrupt:
        print("\nProgram terminated by user. Exiting...")

if __name__ == "__main__":
    main()
