import tasks
import pytest


def test_add_raises():
    with pytest.raises(ValueError) as excinfo:
        task = tasks.Task('reading books', 'jgp', True, 1)
        tasks.add(task)
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "task.id value Error"