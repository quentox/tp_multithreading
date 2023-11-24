from Manager import QueueClient
import queue


class Minion(QueueClient):
    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            try:
                task = self.tasks.get()  # Get a task
                print("----------")
                print(f"Tâche {task.identifier} reçus.")
            except queue.Empty:
                print("Queue est vide, Les Minion ne travailles plus.")
                return  # Stop if the task queue is empty

            task.work()  # Execute the task
            print(f"Tâche {task.identifier} complété en {task.time:.4f} seconds.")
            print(f"Matrice random du problème, a: {task.a}")
            print(f"Vecteur Random du problème, b: {task.b}")
            self.results.put(task)  # Send the result to the results queue
            print(f"Résultat de la tâche {task.identifier} envoyé.")
            print("----------")


if __name__ == "__main__":
    minion = Minion()
    minion.run()
