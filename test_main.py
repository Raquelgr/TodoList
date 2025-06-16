import pytest
from main import TodoList

class TestTodoList:
    def setup_method(self):
        self.todo = TodoList()

    def test_add_task(self):
        task_id = self.todo.add_task("Estudar Engenharia de Software 2")

        assert task_id == 1
        assert len(self.todo.tasks) == 1
        assert self.todo.tasks[0]['description'] == "Estudar Engenharia de Software 2"
        assert self.todo.tasks[0]['completed'] is False

    def test_cannot_add_empty_task(self):
        with pytest.raises(ValueError, match="Descrição da tarefa não pode estar vazia!"):
            self.todo.add_task("")

        with pytest.raises(ValueError, match="Descrição da tarefa não pode estar vazia!"):
            self.todo.add_task("   ")

        assert len(self.todo.tasks) == 0

    def test_complete_task(self):
        task_id = self.todo.add_task("Fazer exercícios")

        result = self.todo.complete_task(task_id)
        assert result is True

        task = self.todo.get_task(task_id)
        assert task['completed'] is True

    def test_cannot_complete_non_existent_task(self):
        with pytest.raises(ValueError, match="Tarefa não encontrada com o identificador 999"):
            self.todo.complete_task(999)

    def test_remove_task(self):
        task_id = self.todo.add_task("Tarefa para remover")
        assert len(self.todo.tasks) == 1

        result = self.todo.remove_task(task_id)
        assert result is True
        assert len(self.todo.tasks) == 0

    def test_cannot_remove_non_existent_task(self):
        with pytest.raises(ValueError, match="Tarefa não encontrada com o identificador 999"):
            self.todo.remove_task(999)

    def test_get_all_tasks(self):
        id1 = self.todo.add_task("Tarefa 1")
        id2 = self.todo.add_task("Tarefa 2")
        id3 = self.todo.add_task("Tarefa 3")

        all_tasks = self.todo.get_all_tasks()
        assert len(all_tasks) == 3
        assert all_tasks[0]['id'] == id1
        assert all_tasks[1]['id'] == id2
        assert all_tasks[2]['id'] == id3

    def test_get_all_completed_tasks(self):
        id1 = self.todo.add_task("Tarefa 1")
        id2 = self.todo.add_task("Tarefa 2")
        id3 = self.todo.add_task("Tarefa 3")

        self.todo.complete_task(id1)
        self.todo.complete_task(id3)

        completed_tasks = self.todo.get_completed_tasks()
        assert len(completed_tasks) == 2
        assert completed_tasks[0]['id'] == id1
        assert completed_tasks[1]['id'] == id3

    def test_get_all_pending_tasks(self):
        id1 = self.todo.add_task("Tarefa 1")
        id2 = self.todo.add_task("Tarefa 2")
        id3 = self.todo.add_task("Tarefa 3")

        self.todo.complete_task(id1)
        self.todo.complete_task(id3)

        pending_tasks = self.todo.get_pending_tasks()
        assert len(pending_tasks) == 1
        assert pending_tasks[0]['id'] == id2

    def test_count_tasks(self):
        self.todo.add_task("Tarefa 1")
        self.todo.add_task("Tarefa 2")
        self.todo.add_task("Tarefa 3")

        assert self.todo.count_tasks() == 3