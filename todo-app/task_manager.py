from storage import Storage

class TaskManager(Storage):
    def __init__(self, filename):
        super().__init__(filename)
        self_tasks = self.load()
    def add_task(self, task):
        self.tasks.append(task)
        self.save(self.tasks)
    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save(self.tasks)
    
    def get_tasks(self):
        return self.tasks
