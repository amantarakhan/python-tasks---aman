from models import Course, Student

# Regestration system class -> this implemnted so that course and student class talk to each other


class Registration:
    def __init__(self):
        self.courses = {}
        self.students = {}

        # adding a course or a student to the main dictionary -------------------------------------------------------------

    def add_student(self, student_id, name):
        if self.find_student(student_id) is not None:
            print("Student ID already exists")
            return False
        else:
            new_student = Student(student_id, name)
            # student id is the key and the new student object is the vlaue and we store them in the dictionary
            self.students[student_id] = new_student
            print(f"Student {name} added successfully.")
            return True

    def add_course(self, course_code, title, capacity):
        if self.find_course(course_code) is not None:
            print(" Duplicate Course Code")
            return False
        else:
            new_course = Course(title, course_code, capacity)
            self.courses[course_code] = new_course
            print(f"Course {title} added successfully.")
            return True

        # drop and enroll student from a course functions----------------------------------------------------
    def enroll_student_in_course(self, student_id, course_code):
        student = self.find_student(student_id)
        course = self.find_course(course_code)

        if student is None:
            print("Error: Student not found.")
            return

        if course is None:
            print("Error: course not found.")
            return

        if course.add_student(student):
            student.enroll(course)
            print(f"Successfully enrolled {student.name} in {course.title}.")
        else:
            print("Enrollment failed: Course is full or student already enrolled.")

    def drop_student_from_course(self, student_id, course_code):
        student = self.find_student(student_id)
        course = self.find_course(course_code)

        if student is None:
            print("Error: Student not found.")
            return

        if course is None:
            print("Error: course not found.")
            return

        if course.remove_student(student):
            student.drop(course)
            print(f"Successfully dropped {student.name} from {course.title}.")
        else:
            print("Error: Student is not enrolled in this course.")

        # here are all the view functions ---------------------------------------------


    def view_all_students(self):
        if not self.students:
            print("No students registered.")
            return
        
        print("\n--- List of All Students ---")
        for s in self.students.values():
            print(f"ID: {s.student_id} | Name: {s.name}")


    def view_all_courses(self):
        if not self.courses:
            print("No courses have been added to the system yet.")
            return

        print("\n--- List of All Courses ---")
        for course in self.courses.values():
            enrolled_count = len(course.students)
            print(
                f"Code: {course.course_code} | Title: {course.title} | Enrolled: {enrolled_count}/{course.capacity}")

    def display_student_schedule(self, student_id):
        student = self.find_student(student_id)
        if student:
            print(f"\n--- Schedule for {student.name} ({student_id}) ---")
            if not student.courses:
                print("No courses enrolled.")
            for course in student.courses:
                print(f"- {course.title} ({course.course_code})")
        else:
            print("Error: Student not found.")


# ----------------------------------------------------------------------------
# helper function (to help me search a student / course before doing anything )

    def find_student(self, student_id):
        # Returns the object or None automatically
        return self.students.get(student_id)

    def find_course(self, course_code):
        return self.courses.get(course_code)
