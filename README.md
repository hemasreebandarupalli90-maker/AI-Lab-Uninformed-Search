
# AI Assignment 

Hemasree
SE24UCSE045


## Overview

This assignment consists of Python programs that demonstrate important concepts in Artificial Intelligence. The programs implement a Turing Test model, a CAPTCHA generation system, and uninformed search algorithms for solving a classic AI problem.



## 1. Turing Test Implementation

This program demonstrates the basic idea of the Turing Test proposed by Alan Turing.

In this implementation, a simple interaction system is designed where a judge communicates with two participants — a human and a machine. The judge evaluates the responses and attempts to determine which participant is the machine.

The architecture includes:

* Judge Interface
* Human Participant
* Machine Agent
* Communication Server

This program demonstrates how intelligent behavior can be simulated and evaluated.

Implementation File:
turing_test/turing_test.py


## 2. CAPTCHA Generator

This program generates a CAPTCHA and verifies whether the user enters the correct text.

First, a random string containing letters and numbers is generated. The system then displays this string to the user. The user must enter the same text correctly to pass the verification process.

CAPTCHA is used to differentiate humans from automated programs (bots). If the entered text matches the generated text, the program displays a success message. Otherwise, it displays an error message.

Implementation File:
captcha/captcha.py



## 3. Missionaries and Cannibals Problem

This program solves the classic Missionaries and Cannibals problem using uninformed search algorithms.

In this problem, three missionaries and three cannibals must cross a river using a boat that can carry only two people at a time. The rule is that cannibals should never outnumber missionaries on either side of the river.

Each state in the problem is represented by:

* Number of missionaries on the left side
* Number of cannibals on the left side
* Boat position

Algorithms Implemented:

* Breadth First Search (BFS)
* Depth First Search (DFS)

BFS uses a queue and guarantees an optimal solution, while DFS uses a stack and explores deeply before backtracking.

Implementation Files:

* search_algorithms/bfs.py
* search_algorithms/dfs.py
* search_algorithms/missionaries_cannibals.py


## Conclusion

Through this assignment, important Artificial Intelligence concepts were implemented using Python programs. The Turing Test demonstrates evaluation of intelligent behavior. The CAPTCHA generator shows a human verification mechanism. The Missionaries and Cannibals problem demonstrates how uninformed search algorithms explore state spaces to find valid solutions.

