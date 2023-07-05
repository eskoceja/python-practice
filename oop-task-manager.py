from bcolors import bcolors


class Task:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.completed = False


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, deadline):
        task = Task(title, description, deadline)
        self.tasks.append(task)

    def view_tasks(self):
        for task in self.tasks:
            status = bcolors.OKGREEN + "Completed" + \
                bcolors.ENDC if task.completed else bcolors.WARNING + "Incomplete" + bcolors.ENDC
            print(bcolors.HEADER +
                  f"Title: {task.title}\nDescription: {task.description}\nDeadline: {task.deadline}\nStatus: {status}\n" + bcolors.ENDC)

    def mark_complete(self, task_title):
        for task in self.tasks:
            if task.title == task_title:
                task.completed = True
                break


task_manager = TaskManager()

task_manager.add_task("Complete Python Project",
                      "Finish coding the task manager OOP Python Project", "2023-07-15")
task_manager.add_task("Complete TDD assignment",
                      "Finish tests for the test driven development assignment", "2023-07-07")
task_manager.mark_complete("Complete Python Project")

while True:

    options = bcolors.OKBLUE + """--- Task Manager Menu ---
    1. Add a task
    2. Mark a task complete
    3. View tasks
    4. Quit""" + bcolors.ENDC

    print(options)

    choice = input(bcolors.BOLD + bcolors.OKBLUE +
                   "Enter your choice: " + bcolors.ENDC)

    if choice == "1":
        title = input(bcolors.OKCYAN + "Enter task title: " + bcolors.ENDC)
        description = input(
            bcolors.OKCYAN + "Enter task description: " + bcolors.ENDC)
        deadline = input(bcolors.OKCYAN +
                         "Enter task deadline: " + bcolors.ENDC)
        task_manager.add_task(title, description, deadline)
        print(bcolors.OKGREEN + "Task added successfully!" + bcolors.ENDC)

    elif choice == "2":
        task_title = input(
            bcolors.OKCYAN + "Enter task title to mark complete: " + bcolors.ENDC)
        task_manager.mark_complete(task_title)
        print(bcolors.OKGREEN + "Task marked as complete!" + bcolors.ENDC)

    elif choice == "3":
        task_manager.view_tasks()

    elif choice == "4":
        print(bcolors.UNDERLINE+"Good-bye!"+bcolors.ENDC)
        break

    else:
        print("Invalid choice. Please try again.")
