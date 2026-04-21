
# course class ---------------------------

class Course:
    def __init__(self, title, course_code, capacity):
        self.title = title
        self.course_code = course_code
        self.capacity = capacity
        self.students = []  # List to hold Student objects


    def add_student(self, student):
        # Check if student is NOT already enrolled AND course is NOT full 
        if student not in self.students and len(self.students) < self.capacity:
            self.students.append(student)
            return True
        return False



    def remove_student(self, student):
        # Check if the student object exists in our list 
        if student in self.students:
            self.students.remove(student)
            return True
        return False

        

# student class -------------------------
class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = []  # List to hold Course objects 


    def enroll ( self , Course ) : 
        if Course not in self.courses :
            self.courses.append(Course)
            return True
        return False

    def drop (self , Course ) :
        if Course in self.courses : 
            self.courses.remove(Course)
            return True 
        return False 
            