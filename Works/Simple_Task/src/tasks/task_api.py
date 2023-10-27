from collections import namedtuple
from six import string_types
from tasks import task_db

Task = namedtuple('Task', ['title', 'owner', 'completed', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)

def add(task):
    if not isinstance(task, Task):
        raise TypeError('task must be Task object')
    if not isinstance(task.title, string_types):
        raise ValueError('task.summary must be string')
    if not ((task.owner is None) or 
            isinstance(task.owner, string_types)):
        raise ValueError('task.owner must be string or None)')
    if task.id is not None:
        raise ValueError('task.id must None')
    
    task_id = _tasksdb.add(task._asdict())
    return task_id

def update(task_id, task):
    if not isinstance(task_id, int):
        raise TypeError('task_id must be an int')
    if not isinstance(task, Task):
        raise TypeError('task must be Task object')
    current_task = _tasksdb.get(task_id)
    updates = task._asdict()
    for field in task._fields:
        if field != 'id' and updates[field] is not None:
            current_task[field] = updates[field]
    _tasksdb.update(task_id, current_task)

def delete(task_id):
    if not isinstance(task_id, int):
        raise TypeError('task_id must be an int')
    _tasksdb.delete(task_id)

def get(task_id):
    if not isinstance(task_id, int):
        raise TypeError('task_id must be an int')
    task_dict = _tasksdb.get(task_id)
    return Task(**task_dict)

_tasksdb = None

def start_task_db(db_path):
    if not isinstance(db_path, string_types):
        raise TypeError('db_path must be a string')
    global _tasksdb

    _tasksdb = task_db.start_db(db_path)

def stop_task_db():
       
    global _tasksdb
    _tasksdb.stop_db()
    _tasksdb = None