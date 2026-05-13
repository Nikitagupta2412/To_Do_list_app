import json

# LOAD TASKS FROM JSON FILE
file = open("tasks.json", "r")
tasks = json.load(file)
file.close()


# SAVE TASKS FUNCTION
def savetasks():

    file = open("tasks.json", "w")

    json.dump(tasks, file)

    file.close()


# ADD TASK
def addtask():

    print("ADD NEW TASK")

    while True:

        taskname = input("enter task name: ")

        task = {
            "task": taskname,
            "completed": False
        }

        tasks.append(task)

        savetasks()

        print("task added successfully")

        choice = input("want to add more tasks? ")

        if choice.lower() != "yes":
            break


# VIEW TASKS
def viewtasks():

    print("\nYOUR TASKS\n")

    if len(tasks) == 0:

        print("no tasks available")

    else:

        for i in tasks:

            print(i)


# MARK TASK COMPLETED
def completetask():

    print("MARK TASK AS COMPLETED")

    name = input("enter task name: ")

    found = False

    for i in tasks:

        if i["task"] == name:

            i["completed"] = True

            savetasks()

            print("task marked completed")

            found = True

            break

    if found == False:

        print("task not found")


# DELETE TASK
def deletetask():

    print("DELETE TASK")

    name = input("enter task name to delete: ")

    found = False

    for i in tasks:

        if i["task"] == name:

            tasks.remove(i)

            savetasks()

            print("task deleted successfully")

            found = True

            break

    if found == False:

        print("task not found")


# MENU SYSTEM
while True:

    print("\nPRESS 1 TO ADD TASK")
    print("PRESS 2 TO VIEW TASKS")
    print("PRESS 3 TO COMPLETE TASK")
    print("PRESS 4 TO DELETE TASK")
    print("PRESS 5 TO EXIT")

    choice = input("enter your choice: ")

    if choice == "1":

        addtask()

    elif choice == "2":

        viewtasks()

    elif choice == "3":

        completetask()

    elif choice == "4":

        deletetask()

    elif choice == "5":

        print("program exited")

        break

    else:

        print("invalid choice")
