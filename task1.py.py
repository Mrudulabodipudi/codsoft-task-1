class ToDoList:
    def __init__(self):
        self.tasks = []

    def run(self):
        while True:
            print("1. Add task")
            print("2. View tasks")
            print("3. Delete task")
            print("4. Exit")
            option = input("Choose an option: ")

            if option == "1":
                self.add_task()
            elif option == "2":
                self.view_tasks()
            elif option == "3":
                self.delete_task()
            elif option == "4":
                break
            else:
                print("Invalid option. Please try again.")

    def add_task(self):
        task = input("Enter task: ")
        self.tasks.append(task)
        print("Task added!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def delete_task(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            self.view_tasks()
            task_number = int(input("Enter task number to delete: "))
            if 1 <= task_number <= len(self.tasks):
                del self.tasks[task_number - 1]
                print("Task deleted!")
            else:
                print("Invalid task number.")


if __name__ == "__main__":
    to_do_list = ToDoList()
    to_do_list.run()

