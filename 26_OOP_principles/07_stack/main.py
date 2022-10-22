class Stack:
    def __init__(self):
        self.__st = []

    def __str__(self):
        return '; '.join(self.__st)

    def push(self, elem):
        self.__st.append(elem)

    def pop(self):
        if len(self.__st) == 0:
            return None
        return self.__st.pop()


class TaskManager:
    def __init__(self):
        self.task = dict()

    def __str__(self):
        display = []
        if self.task:
            for i_priority in sorted(self.task.keys()):
                display.append('{priority} {task}\n'.format(
                    priority=str(i_priority),
                    task=self.task[i_priority]
                    )
                )
        return ''.join(display)

    def new_task(self, task, priority):
        if task not in self.task:
            self.task[priority] = Stack()
        self.task[priority].push(task)


manager = TaskManager()

manager.new_task(task="сделать уборку", priority=4)
manager.new_task(task="помыть посуду", priority=4)
manager.new_task(task="отдохнуть", priority=1)
manager.new_task(task="поесть", priority=2)
manager.new_task(task="сдать дз", priority=2)

print(manager)

