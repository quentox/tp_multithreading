from Manager import QueueClient
from Task import Task
import queue


class Boss(QueueClient):
    def __init__(self):
        super().__init__()

    def submit_tasks(self, num_tasks):
        for i in range(num_tasks):
            task = Task(identifier=i)  # Create a task
            self.tasks.put(task)  # Put the task in the queue

    def collect_results(self):
        results = []
        for i in range(num_tasks):
            try:
                result = self.results.get()  # Get the result
                results.append(result)
            except queue.Empty:
                print("La queue du résultat est vide ")
                break  # Exit the loop if the results queue is empty
        return results


if __name__ == "__main__":
    boss = Boss()
    num_tasks = 10
    boss.submit_tasks(num_tasks)

    print("Tâches envoyé, récupération des résultats...")
    results = boss.collect_results()
    print(f"{len(results)} résultats obtenue.")
