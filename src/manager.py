class TaskManager:
    def __init__(self):
        self.tasks = {}
        self.counter = 1

    def create_task(self, title, priority="Média"):
        if not title:
            raise ValueError("O título da tarefa não pode ser vazio.")
        
        task = {
            "id": self.counter,
            "title": title,
            "priority": priority,
            "status": "A Fazer"
        }
        self.tasks[self.counter] = task
        self.counter += 1
        return task

    def read_tasks(self):
        return list(self.tasks.values())

    def update_task_status(self, task_id, new_status):
        if task_id not in self.tasks:
            raise KeyError("Tarefa não encontrada.")
        self.tasks[task_id]["status"] = new_status
        return self.tasks[task_id]

    def delete_task(self, task_id):
        if task_id not in self.tasks:
            raise KeyError("Tarefa não encontrada.")
        return self.tasks.pop(task_id)