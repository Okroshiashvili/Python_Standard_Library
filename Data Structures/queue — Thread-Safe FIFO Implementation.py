


"""
A thread-safe first-in, first-out (FIFO) implementation of queue 


This can be used to pass the data between producer and consumer threads safely.
Locking is handled for the caller and the size of the queue can be restricted.

"""



import queue


# Basic FIFO Queue


# Empty queue
q = queue.Queue()

for i in range(5):
    q.put(i) # insert element in queue

# empty() method checks if queue is empty
while not q.empty():
    print(q.get(), end= ' ')



# LIFO Queue - last-in, first-out

q = queue.LifoQueue()

for i in range(5):
    q.put(i)

print()

while not q.empty():
    print(q.get(), end= ' ')




# Priority Queue

"""
Priority queue uses the sort order of the contents of the queue to decide which item to retrieve
"""


import functools
import threading

@functools.total_ordering
class Job:

    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        print("New Job :", description)
        return
    

    def  __eq__(self, other):
        try:
            return self.priority == other.priority
        except AttributeError:
            return NotImplemented
    

    def __lt__(self, other):
        try:
            return self.priority < other.priority
        except AttributeError:
            return NotImplemented


print()
print("=" * 40)

# empty queue
q = queue.PriorityQueue()

q.put(Job(3, "Mid-level job"))
q.put(Job(10, "Low-level job"))
q.put(Job(1, "Important job"))


def process_job(q):
    """
    Function to process queue

    """
    while True:
        next_job = q.get()
        print("Processing job :", next_job.description)
        q.task_done()


# define workers who will work on the queue
workers = [
    threading.Thread(target=process_job, args=(q,)),
    threading.Thread(target=process_job, args=(q,))
]


for worker in workers:
    worker.setDaemon(True)
    worker.start()

q.join()




