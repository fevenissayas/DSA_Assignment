class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.complete = False

    def getTitle(self):
        return self.title

    def getDescription(self):
        return self.description

    def isCompleted(self):
        return self.complete

    def markCompleted(self):
        self.complete = True

class Node:
    def __init__(self, task):
        self.task = task
        self.next = None

class ToDoList:
    def __init__(self):
        self.head = None

    def addToDo(self, task):
        new_node = Node(task)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def markToDoAsCompleted(self, title):
        temp = self.head
        while temp:
            if temp.task.getTitle() == title:
                temp.task.markCompleted()
                return True
            temp = temp.next
        return False

    def viewToDoList(self):
        tasks = []
        temp = self.head
        while temp:
            task = temp.task
            tasks.append({
                "title: ": task.getTitle(),
                "what to do: ": task.getDescription(),
                "is your task completed? ": task.isCompleted()
            })
            temp = temp.next
        return tasks

#Testing (example):

if __name__ == "__main__":
    todo_list = ToDoList()

    task1 = Task("Task 1", "Do your Laundary")
    task2 = Task("Task 2", "Attend your meeting")
    todo_list.addToDo(task1)
    todo_list.addToDo(task2)

    todo_list.markToDoAsCompleted("Task 0")

    for task in todo_list.viewToDoList():
        print(task)
