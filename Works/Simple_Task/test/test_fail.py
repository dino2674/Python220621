import tasks

def test_task_equality():
    t1 = tasks.Task('Do 1', 'jgp')
    t2 = tasks.Task('Do 2', 'pkg')

    assert t1 == t2