# Multithreading Project
The Multithreading Project is a practical endeavor designed to delve deep into multithreading and Git usage, through the implementation of solutions in Python and C++.

## Project Description
This project presents a task management application based on a queue architecture. The central elements of this application are as follows:

**Boss** : It creates tasks and places them in a queue.

**Task (Tâche)** : Represents a unit of work.

**Minion** : Retrieves tasks from the queue, executes them, and sends the results.

## Project Structure
**Boss.py** : Contains the Boss class responsible for creating and adding tasks to the queue.

**Manager.py** : Introduces the QueueManager class which supervises the queue, as well as the QueueClient class used to interact with it.

**Minion.py** : Contains the Minion class, responsible for fetching tasks from the queue, executing them, and sending the results.

**Task.py** : Implements the Task class, describing a task with work procedures and JSON conversion.

**Proxy.py** : Provides a basic proxy server that presents a task from the queue in JSON format when an HTTP GET request is received.

**Low_level.cpp** : A C++ script accomplishing a task using the Eigen library, fetching a task from the queue via the proxy.

## Dependencies
- Python 3
- Numpy
- C++

## Running Python Part
First, run:

```
python manager.py
```

Then, run a boss to add a task to the queue:

``` 
python boss.py
```

Launch as many servers as needed:

```
python minion.py
```

## Running Components and Accessing Task Results via Proxy
First, run:

```
python manager.py
```

Run a boss to add a task to the queue:

```
python boss.py
```

Launch a single proxy:

```
python proxy.py
```

You can access the first task in the queue via a web browser using the URL: https://localhost:8000

## C++ Part

I reached the implementation stage of the Boss-Minion model in C++, however, I encountered complications with CMAKE. Nevertheless, I have still provided you with the code for low_level.cpp.



