import tasks
import pytest


@pytest.mark.basic
def test_add_returns_valid_id():
    tasks.start_task_db('./')
    task = tasks.Task('Coding', 'jgp')
    id = tasks.add(task)
    tasks.stop_task_db()
    assert isinstance(id, int)

@pytest.mark.smoke
def test_added_task_has_id_set():
    tasks.start_task_db('./')
    task = tasks.Task('Do Nothing', owner='jgp', completed=True)
    id = tasks.add(task)

    task_from_db = tasks.get(id)
    tasks.stop_task_db()
    assert task_from_db.id == id