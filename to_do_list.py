items_to_do = []

def show_menu():
    print("""Hello, I am your Task Manager.
    How would you like to magage your list today?
    Press 1 to Add New Task.
    Press 2 to Delete Task.
    Press 3 to View All Tasks.
    Press q to quit. """)

def add_task():
    task_name = input("Please enter task you wish to add: ")
    task_priority = input("Please enter the priority of the task: ")
    tasks = {"Title": task_name, "Priority": task_priority}
    items_to_do.append(tasks)

def view_tasks():
    for i in range(len(items_to_do)):
        print(f'{i + 1}) {items_to_do[i]["Title"]} - {items_to_do[i]["Priority"]}')

def delete_task():
    task_number = int(input("Which task would you like to delete: ")) - 1
    for items in items_to_do:
        if task_number == items_to_do.index(items):
            items_to_do.remove(items)

def quit():
    print("Thank you for using my handy dandy features :D ")
    print("Have a fun day working on your list!")

user_input = ""

while user_input != "q":
    show_menu()
    user_input = input("Please make your selection: ")

    if user_input == "1":
        add_task()
    elif user_input == "2":
        delete_task()
    elif user_input == "3":
        view_tasks()
    elif user_input == "q":
        quit()
    else:
        print("Invalid Input")
