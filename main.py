from collections import deque
from copy import deepcopy
class Node():
    def __init__(self, value, ancestor=None):
        self.set_ancestor(ancestor)
        self.value = value
        self.children = []
        self.visited = False
    def add_child(self, child):
        self.children.append(child)
    def set_ancestor(self, ancestor):
        self.ancestor = ancestor
    def get_ancestor(self):
        return self.ancestor

def iter_range(ls, start=0, end=None):
    if not(end):
        end = len(ls) - 1
    if (end < 0):
        end += len(ls)
    for key in range(start, end+1):
        yield ls[key]
def append_more(list, stack):
    for val in list:
        stack.append(val)
    return stack

def file_inp():
    with open("input") as file:
        first = True
        for line in file:
            if not (first):
                inp = line.split()
                inp = [int(zadost) for zadost in inp]
            first = False
    return inp

def urednici(ukoly=[]):
    ukoly += [0, 0, 0]
    u1 = ukoly[0]
    u2 = ukoly[1]
    u1_time = 0
    u2_time = 0
    index = 2
    while(index + 1 < len(ukoly)):
        if (u1 < u2):
            u1_time += u1
            u2_time += u1
            u2 -= u1
            u1 = ukoly[index]
        elif (u2 < u1):
            u1_time += u2
            u2_time += u2
            u1 -= u2
            u2 = ukoly[index]
        else:
            u1_time += u1
            u2_time += u2
            u1 = ukoly[index]
            u2 = ukoly[index+1]
            index += 1
        index += 1
    u1_time += u1
    u2_time += u2
    return max(u1_time, u2_time)

def make_task_tree(tasks):
    actual_node = Node(tasks[0])
    root = actual_node
    last = None
    for task in iter_range(tasks, 1):
        node = Node(task)
        while(True):
            if not(actual_node):
                last.set_ancestor(node)
                node.add_child(last)
                actual_node = node
                root = actual_node
                break
            if (task < actual_node.value):
                actual_node.add_child(node)
                node.set_ancestor(actual_node)
                actual_node = node
                break
            last = actual_node
            actual_node = actual_node.get_ancestor()
    return root

def output(n):
    with open("output", "w") as file:
        file.write(n)

def sort_tasks(root):
    stack = deque()
    stack.append(root)
    tasks = []
    while(stack):
        actual_node = stack.pop()
        if not (actual_node.visited):
            data = actual_node.children
            data += [actual_node]
            actual_node.visited = True
            data = data[::-1]
            stack = append_more(data, stack)

        else:
            tasks.append(actual_node.value)
    return tasks

tasks = file_inp()
tree = make_task_tree(tasks)
tasks = sort_tasks(tree)
n = urednici(tasks)
output(str(n))