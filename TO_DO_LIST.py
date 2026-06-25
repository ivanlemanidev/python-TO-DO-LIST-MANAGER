import json
import os

def task_added():
    user_input = input("Enter your task : ")
    while len(user_input.replace(" ","")) == 0:
        user_input = input("please Enter a valid task : ") 
        
    task_information = {"Description":user_input, "Status":" ⛔"}
    if task_information in tasks:
        print("this task already exists")
        output = False
    else:
        print("task added successfuly")
        output = task_information
    return output

def return_task():
    task_ID = input("Enter task ID : ").replace(" ","")
    while task_ID.isdigit() == False:
        task_ID = input("Enter valid task ID : ").replace(" ","")
    list_task = []
    for i, task in enumerate(tasks, 1):
        list_task.append(str(i))
        if str(i) == task_ID:
            valid_task = task
    if task_ID not in list_task:
        valid_task = "Error: invalid task ID"
    return valid_task

def task_completed():
    valid_answer = return_task()
    if type(valid_answer) == dict:
        if valid_answer["Status"] == " ⛔":
            valid_answer["Status"] = " ✅"
            print("Task completed successfuly")
        elif valid_answer["Status"] == " ✅":
            print("task already completed")
    else:
        print(valid_answer) 

def task_deleted():
    valid_answer = return_task()
    if type(valid_answer) == dict:
        tasks.remove(valid_answer)
        print("Task deleted successfuly")
    else:
        print(valid_answer)

def task_saved():
    with open("tasks.json", "w", encoding = "UTF-8") as f:
        json.dump(tasks, f, indent = 4, ensure_ascii = False)
    print("Tasks saved successfuly")

def task_edited():
    valid_answer = return_task()
    new_description = input("Enter your new task : ")
    while len(new_description.replace(" ","")) == 0:
        new_description = input("please Enter a valid new task : ")
    if type(valid_answer) == dict:
        valid_answer["Description"] = new_description
        print("Task edited successfuly")
    else:
        print(valid_answer)

tasks = []

if os.path.exists("tasks.json") and os.path.isfile("tasks.json"):
    with open("tasks.json", "r", encoding = "UTF-8") as f:
        tasks = json.load(f)

while True:
    print("\n TASK-MANAGEMENT-SYSTEM -- TO-DO-LIST -- \n")
    print("1. Add a task")
    print("2. Display all tasks")
    print("3. mark a task as completed")
    print("4. Delete a task")
    print("5. save tasks")
    print("6. Edit a task")
    print("7. Exit \n")
    getting = False
    list_choice = [str(i) for i in range(8) if i != 0]
    user_choice = input("Which option do you choose : ").replace(" ","")
    while user_choice not in list_choice:
        user_choice = input("Please Select a choice from the menu : ").replace(" ","")
    if user_choice == "1":
        print("\n")
        getting = task_added()
    elif user_choice == "2":
        print("\n")
        if len(tasks) == 0:
            print("No tasks at the moment")
        else:
            print("your task list :")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task['Description']} <<{task['Status']} >>")
    elif user_choice == "3":
        print("\n")
        task_completed()
    elif user_choice == "4":
        print("\n")
        task_deleted()
    elif user_choice == "5":
        print("\n")
        task_saved()
    elif user_choice == "6":
        print("\n")
        task_edited()
    else:
        break
    if getting == False:
        pass
    else:
        tasks.append(getting)
    with open("tasks.json", "w", encoding = "UTF-8") as f:
        json.dump(tasks, f, indent = 4, ensure_ascii = False)

