import time
import numpy as np
import json


class Task:
    def __init__(self, identifier, size=None):
        self.identifier = identifier
        # choix taille probleme
        self.size = size or np.random.randint(300, 3_000)
        # gene entree du probleme
        self.a = np.random.rand(self.size, self.size)
        self.b = np.random.rand(self.size)
        # preparation du résultat
        self.x = np.zeros((self.size))
        self.time = 0

    def work(self):
        start = time.perf_counter()
        self.x = np.linalg.solve(self.a, self.b)
        self.time = time.perf_counter() - start

    def to_json(self) -> str:
        return json.dumps({'identifier': self.identifier, 'size': self.size, 'a': self.a.tolist(),
                           'b': self.b.tolist(), 'x': self.x.tolist(), 'time': self.time})

    @classmethod
    def from_json(cls, text: str) -> "Task": #cls -> prendre la classe en parametre
        #decoding JSON
        recup = json.loads(text)
        task = cls(recup['identifier'])
        task.size = np.array(recup['size'])
        task.a = np.array(recup['a'])
        task.b = np.array(recup['b'])
        task.x = np.array(recup['x'])
        task.time = recup['time']
        return task

    def __eq__(self, other: "Task") -> bool or str:
        if self.identifier != other.identifier:
            return False, print("identifier")
        if self.size != other.size:
            return False, print("size")
        if not np.array_equal(self.a, other.a):
            return False, print("a")
        if not np.array_equal(self.b, other.b):
            return False, print("b")
        if not np.array_equal(self.x, other.x):
            return False, print("x")
        if self.time != other.time:
            return False, print("time")
        return True, None

    # Test unitaire
def test_task_equality():
    a = Task("task1")

    a_json = a.to_json()
    print("Task sérialisée en JSON.")

    b = Task.from_json(a_json)
    print("Task désérialisée.")

    equal, diff_equals = a == b
    if equal:
        print("Test réussi : La tache sérialisé et déserialisée sont égales.")
    else:
        print(f"Test échoué : Différence détectée dans l'attribut '{diff_equals}'.")

test_task_equality()
