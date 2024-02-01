# TP Multithreading
Le TP Multithreading est un projet pratique conçu pour explorer en profondeur le multithreading ainsi que l'utilisation de Git, à travers l'implémentation de solutions en Python et en C++.

## Description du Projet
Ce projet présente une application de gestion de tâches qui repose sur une architecture de file d'attente. Les éléments centraux de cette application sont les suivants :

**Boss** : Il crée des tâches et les place dans une file d'attente.

**Task (Tâche)** : Représente une unité de travail.
**Minion** : Récupère des tâches de la file d'attente, les exécutes et envoie les résultats.

## Structure du Projet
**Boss.py** : Contient la classe Boss responsable de la création et de l'ajout de tâches dans la file d'attente.

**Manager.py** : Introduit la classe QueueManager qui supervise la file d'attente, ainsi que la classe QueueClient employée pour interagir avec celle-ci.

**Minion.py** : Contient la classe Minion, responsable de l'extraction des tâches de la file d'attente, de leur exécution et de l'envoi des résultats.

**Task.py** : Implémente la classe Task, décrivant une tâche avec des procédures de travail et de conversion JSON.

**Proxy.py** : Propose un serveur proxy basique qui présente une tâche de la file d'attente sous forme JSON lorsqu'une requête HTTP GET est reçue.

**Low_level.cpp** : Un script C++ accomplissant une tâche grâce à la bibliothèque Eigen, récupérant une tâche de la file d'attente via le proxy.

## Dépendances
**Python**
- Python 3
- Numpy
- C++

## Exécution de la Partie Python
Lancez tout d'abord :

``` python manager.py  ```

Puis lancez un boss pour ajouter une tâche dans la file d'attente :

``` python boss.py ```

Lancez autant de serveurs que nécessaire :

``` python minion.py ```

## Exécution des Composants et Accès aux résultats des Tâches par proxy
Lancez tout d'abord :

``` python manager.py ```

Lancez un boss pour ajouter une tâche dans la file d'attente :

``` python boss.py ```

Lancez un seul proxy :

``` python proxy.py ```

Vous pouvez accéder à la première tâche de la file d'attente via un navigateur Web en utilisant l'URL : https://localhost:8000

## Partie C++

J'ai atteint l'étape d'implémentation du modèle Boss-Minion en C++, cependant, j'ai rencontré des complications liées à CMAKE. Malgré cela, je vous ai tout de même fourni le code pour low_level.cpp.
