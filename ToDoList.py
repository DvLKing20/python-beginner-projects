import asyncio
import os
class ToDoList:
    def __init__(self):
        self.tasks = list()
        if not os.path.exists("ToDoList.txt"):
            with open("ToDoList.txt", 'w') as file:
               print("task file created")

    async def ask_task(self):
        add_task = input("What would you like to add?: ")
        with open(f"ToDoList.txt", 'a') as file:
            file.write(add_task+"\n")
        print(f"task added")

    async def display_task(self):
        with open("ToDoList.txt", 'r') as file:
           for line in file:
             self.tasks.append(line.strip())
        for index,task in enumerate(self.tasks,start=1):
            print(f"{index}: {task}")
        print()

    async def remove_task(self):
        try:
              if self.tasks:
                    index = int(input("What would you like to remove?: ")) - 1
                    task = self.tasks
                    if task[index] in self.tasks:
                        del self.tasks[index]
                        with open("ToDoList.txt", 'w') as file:
                           for task in self.tasks:
                               file.write(task+"\n")
                        print(f"task removed")
              else:
                 print("No tasks added")

        except ValueError:
             print("\nInvalid Input")

    async def show_display(self):
        try:
           print(" 1: Add task\n 2: Remove task\n 3: Display task")
           index = int(input("What would you like to show?: "))
           return index
        except ValueError:
            print("\nInvalid Input")

    async def main(self):
       while True:
         index = await self.show_display()
         if index == 1:
             await self.ask_task()
         elif index == 2:
             await self.remove_task()
         elif index == 3:
             await self.display_task()
         else:
             print("Invalid option")


if __name__ == "__main__":
 application_reference = ToDoList()
 asyncio.run(application_reference.main())