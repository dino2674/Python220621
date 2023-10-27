import tinydb

class Task():
    def __init__(self, db_path):
        self._db = tinydb.TinyDB(db_path + 'task_db.json')
    
    def add(self, task):
        task_id = self._db.insert(task)
        task['id'] = task_id
        self._db.update(task, doc_ids=[task_id])
        return task_id
    
    def update(self, task_id, task):
        self._db.update(task, doc_ids=[task_id])
    
    def delete(self, task_id):
        self._db.remove(doc_ids=[task_id])
    
    def get(self, task_id):
        return self._db.get(doc_id=task_id)
    
    def gen_id(self):
        id = 1
        while self._db.contains(doc_ids=[id]):
            id += 1
        return id

    def stop_db(self):
        self._db.close()
    
def start_db(db_path):  
    return Task(db_path)