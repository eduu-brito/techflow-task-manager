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
    
if __name__ == "__main__":
    print("=== TECHFLOW TASK MANAGER ===")
    
    # Instanciando o gerenciador de tarefas
    manager = TaskManager()
    
    # 1. Demonstração de Criação de Tarefa (Ajustado para o seu método real)
    print("\n[Criando uma tarefa...]")
    task = manager.create_task("Entregar carga Setor A", "Alta")
    print(f"Tarefa criada com sucesso: {task}")
    
    # 2. Demonstração da Regra de Negócio (Bloqueio de título vazio)
    print("\n[Testando restrição de segurança (Título Vazio)...]")
    try:
        manager.create_task("")
    except ValueError as e:
        print(f"Sucesso! O sistema bloqueou a operação. Erro esperado: {e}")
        
    print("\n=============================")