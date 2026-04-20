from datetime import datetime
import json

Tasks = []
    


def display_menu(): 
    user_choice = 0  #
    print("\n--- To Do App ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Edit a Task")
    print("6. Exit")
    
    try: 
        user_choice = int(input("Select an option: "))
    except ValueError: 
        print("Invalid input! Please enter a number from [1-6].")
        
    return user_choice


def load_tasks():
    global Tasks # Tells Python to use the Tasks variable defined outside this function (the main list) rather than creating a local one.
    try:
        with open('tasks.json', 'r') as f: # open the file in the read mode (cannt edit it ) the with ensure that its close aoutomatically 
            print("--- File found! Loading data... ---")
            data = json.load(f)
            for t in data:
                t['created_At'] = datetime.strptime(t['created_At'], "%Y-%m-%d %H:%M:%S")
            Tasks = data
    except (FileNotFoundError, json.JSONDecodeError):
        Tasks = []



def save_tasks():
    temp_list = []
    for t in Tasks:
        task_copy = { # this Creates a new dictionary for each task.
            'id': t['id'],
            'title': t['title'],
            'done': t['done'],
            'created_At': t['created_At'].strftime("%Y-%m-%d %H:%M:%S")
        }
        temp_list.append(task_copy) # Adds this "JSON-friendly" version of the task to our temporary list.
    
    with open('tasks.json', 'w') as f: # open the file in the write mode 
        json.dump(temp_list, f,) 


def addTask() : 
    new_task = {} 
    print ("Enter a task Title : ")
    t = input ("")

    if len(Tasks) == 0  :
        new_task['id'] = 1
    else:
        new_task['id'] = Tasks[-1]['id'] + 1
    

    new_task['title'] = t
    new_task ['done'] = False
    new_task ['created_At'] = datetime.now()

    Tasks.append(new_task)
    save_tasks()
    print(f'successfuly added {t} to you list ! ')
    
    

def ViewAll() : 
    if len(Tasks) == 0 : 
        print ('Your to-do list is currently empty!')
    else : 
        print (" all tasks :")
        for t in Tasks : 
            print(f"Title: {t['title']} | is it done : {t['done']} | time Created: {t['created_At']}")    


def MarkAsDone():
    try:
        target_id = int(input("Enter the Task ID to mark as done: "))
        found = False
        for t in Tasks:
            if t['id'] == target_id:
                t['done'] = True
                save_tasks()
                print(f"Task {target_id} is done!")
                found = True
                break
        if not found:
            print(f"Error: No task found with ID {target_id}")
    except ValueError:
        print("Invalid input. Please enter a numeric ID.")



def DeleteTask():
    try:
        target_id = int(input("What is the task ID you want to delete? "))
        for t in Tasks: 
            if t['id'] == target_id: 
                Tasks.remove(t) 
                save_tasks()
                print("Task deleted successfully.")
                return 
        print("ID not found.")
    except ValueError:
        print("Invalid input.")
     

def EditTask() : 
    target_task = int(input("Enter the task ID that you want to Edit :"))
    modified_task = input ("what is the new title for it ?")
    for t in Tasks : 
        if t['id'] == target_task :
            t["title"] = modified_task 
            save_tasks()
            print(f'{target_task} is succuessfully changed to {t['title']} ')


5
load_tasks()
while (True) : 
    choice = int(display_menu()) 
    match (choice) : 
        case 6 : 
            break 
        case 1 : 
            addTask() 
        case 2 : 
            ViewAll()
        case 3 : 
            MarkAsDone()
        case 4 :
            DeleteTask() 
        case 5 :
            EditTask()



