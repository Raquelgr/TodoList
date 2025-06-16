class TodoList:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, description):
        if not description or not description.strip():
            raise ValueError("Descrição da tarefa não pode estar vazia!")

        task = {
            'id': self.next_id,
            'description': description.strip(),
            'completed': False
        }

        self.tasks.append(task)
        self.next_id += 1
        return task['id']

    def complete_task(self, task_id):
        task = self.get_task(task_id)

        if task:
            task['completed'] = True
            return True

        raise ValueError(f"Tarefa não encontrada com o identificador {task_id}")

    def remove_task(self, task_id):
        task = self.get_task(task_id)

        if task:
            self.tasks.remove(task)
            return True

        raise ValueError(f"Tarefa não encontrada com o identificador {task_id}")

    def get_task(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                return task

        raise ValueError(f"Tarefa não encontrada com o identificador {task_id}")

    def get_all_tasks(self):
        return self.tasks.copy()

    def get_completed_tasks(self):
        return [task for task in self.tasks if task['completed']]

    def get_pending_tasks(self):
        return [task for task in self.tasks if not task['completed']]

    def count_tasks(self):
        return len(self.tasks)