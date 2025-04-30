# TODO между классами и после них 2 пустые строчки кода, а между методам 1 пустая строчка
# TODO если используете pycharm используйте ctrl + alt + L

class Stack:
    def __init__(self):
        self.stack = []
    def add_elem(self, value):
        self.stack.append(value)
    def remove_elem(self):
        return self.stack.pop()

class TaskManager:
    def __init__(self):
        self.stack = Stack()
    def new_task(self, task: str, priority: int):
        self.stack.add_elem((priority, task))

    def __str__(self):
        task_by_priority = {}
        for priority, task in self.stack.stack:
            if priority not in task_by_priority:
                task_by_priority[priority] = []
            task_by_priority[priority].append(task)

        result = []
        for priority in sorted(task_by_priority):
            tasks = '; '.join(task_by_priority[priority])
            result.append(f"{priority} {tasks}")

        return '\n'.join(result)

    def remove_task(self, task: str):
        new_stack = []
        for priority, task_name in self.stack.stack:
            if task_name != task:
                new_stack.append((priority, task_name))
        self.stack.stack = new_stack

manager = TaskManager()
manager.new_task("уборка", 3)
manager.new_task("помыть посуду", 2)
manager.new_task("отдохнуть", 1)
manager.new_task("помыть посуду", 2)

print("До удаления:")
print(manager)

manager.remove_task("помыть посуду")
print("После удаления:")
print(manager)