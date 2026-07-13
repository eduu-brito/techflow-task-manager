import pytest
from src.manager import TaskManager

def test_create_task():
    manager = TaskManager()
    task = manager.create_task("Entregar carga Setor A", "Alta")
    assert task["id"] == 1
    assert task["title"] == "Entregar carga Setor A"
    assert task["status"] == "A Fazer"

def test_create_task_empty_title():
    manager = TaskManager()
    with pytest.raises(ValueError):
        manager.create_task("")

def test_update_status():
    manager = TaskManager()
    manager.create_task("Roteirizar frotas")
    updated = manager.update_task_status(1, "Em Progresso")
    assert updated["status"] == "Em Progresso"