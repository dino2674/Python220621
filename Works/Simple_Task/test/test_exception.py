import tasks
import pytest

def test_add_raises():
    with pytest.raises(TypeError):
        tasks.add(task='String Type')