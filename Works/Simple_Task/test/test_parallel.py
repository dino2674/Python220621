import tasks
import pytest

@pytest.mark.parametrize('input', list(range(10)))
def test_get_raises(tasks_db, input):
    task = tasks.get(input)
    assert isinstance(task.id, int)