import tasks
import pytest

def test_add_returns_valid_id(tasks_db):
    task = tasks.Task('Coding', 'jgp')
    id = tasks.add(task)
    assert isinstance(id, int)

def test_added_task_has_id_set(tasks_db):
    task = tasks.Task('Do Nothing', owner='jgp', completed=True)
    id = tasks.add(task)

    task_from_db = tasks.get(id)
    assert task_from_db.id == id