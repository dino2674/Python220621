import tasks
import pytest

@pytest.fixture(scope='module')
def tasks_db():
    tasks.start_task_db('./')

    yield

    tasks.stop_task_db()