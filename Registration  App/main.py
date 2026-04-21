
  
from Registration import Registration

my_registration = Registration()

def display_menu(): 
    print ("""
    --- Registration Management System ---
    1. Add a new student
    2. Add a new course with a capacity
    3. Enroll a student in a course
    4. Drop a student from a course
    5. View all students
    6. View all courses
    7. View all courses for a specific student
    8. Exit 
    """)
    try: 
        return int(input("Select an option: "))
    except ValueError: 
        return 0
    
while True: 
    choice = display_menu()
    match choice:
        case 1:
            s_id = input("Enter Student ID: ").strip()
            name = input("Enter Student Name: ").strip()
            my_registration.add_student(s_id, name) 

        case 2:
            c_code = input("Enter Course Code: ").strip()
            title = input("Enter Course Title: ").strip()
            try:
                cap = int(input("Enter Capacity: "))
                my_registration.add_course(c_code, title, cap)
            except ValueError:
                print("Invalid capacity. Please enter a number.")

        case 3:
            s_id = input("Enter Student ID: ").strip()
            c_code = input("Enter Course Code: ").strip()
            my_registration.enroll_student_in_course(s_id, c_code) 

        case 4:
            s_id = input("Enter Student ID: ").strip()
            c_code = input("Enter Course Code: ").strip()
            my_registration.drop_student_from_course(s_id, c_code) 

        case 5:
            my_registration.view_all_students()

        case 6:
            my_registration.view_all_courses() 

        case 7:
            s_id = input("Enter Student ID: ")
            my_registration.display_student_schedule(s_id)

        case 8:
            print("Goodbye!")
            break
            
        case _:
            print("Invalid selection. Try again.")