import tasks
import pytest


@pytest.mark.parametrize('title, owner, completed',
[('Action1', None, False),
('Action2', 'jgp', False),
('Action3', None, True),
('Action4', 123, False),
])

def test_add(title, owner, completed):
    tasks.start_task_db('./')
    task = tasks.Task(title, owner, completed)
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    tasks.stop_task_db()
    assert t_from_db.id == task_id