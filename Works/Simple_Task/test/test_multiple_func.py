import tasks
import pytest


def test_task_equality():
    t1 = tasks.Task('Do 1', 'jgp')
    t2 = tasks.Task('Do 1', 'jgp')

    assert t1 == t2

def test_add_raises():
    with pytest.raises(TypeError):
        tasks.add(task='String Type')

def test_add_returns_valid_id():
    tasks.start_task_db('./')
    task = tasks.Task('Coding', 'jgp')
    id = tasks.add(task)
    tasks.stop_task_db()
    assert isinstance(id, int)

def test_added_task_has_id_set():
    tasks.start_task_db('./')
    task = tasks.Task('Do Nothing', owner='jgp', completed=True)
    id = tasks.add(task)

    task_from_db = tasks.get(id)
    tasks.stop_task_db()
    assert task_from_db.id == id