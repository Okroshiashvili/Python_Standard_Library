


"""
A double-ended queue, or deque, supports adding and removing elements from either end of the queue.
The more commonly used stacks and queues are degenerate forms of deques, where the inputs and outputs are restricted to a single end.
"""


import collections

d = collections.deque('abcdefg')

print('Initial Deque :', d)
print('Length :', len(d))
print('Left End :', d[0])
print('Right End :', d[-1])

d.remove('c')
print('remove(c) :', d)


# Deque can be populated from either end, termed "lef" or "right"

d = collections.deque()

print('*' * 20)
print("Populating to the right")
d.extend('abcdefg')
print("Extended :", d)
d.append('h')
print("Appended :", d)

print()

print("Populating to the left")
d.extendleft(range(6))
print("Extended left :", d)
d.appendleft(10)
print("Appended left :", d)


# Consuming

d = collections.deque('abcdefg')

print('=' * 20)

print("Initial Deque :", d)
d.pop()
print("Remove item from the right :", d)
d.popleft()
print("Remove item from the left :", d)

# As Deque is thread-safe, content can be consumed from both ends simultaneously

import threading
import time

candle = collections.deque(range(5))

print('-' * 40)

def burn(direction, nextSource):
    """
    The threads alternate between each end, removing items until the deque is empty
    """
    while True:
        try:
            next = nextSource()
        except IndexError:
            break
        else:
            print("{:>8}: {}".format(direction, next))
            time.sleep(0.1)
    print("{:>8} done".format(direction))
    return

left = threading.Thread(target=burn,
                        args=('Left', candle.popleft))

right = threading.Thread(target=burn,
                        args=('Right', candle.pop))


left.start()
right.start()

left.join()
right.join()


# Rotating

d = collections.deque(range(1, 11))

print('+' * 40)

print("Initial Deque :", d)
d.rotate(5)
print("Right Rotation :", d)
d.rotate(-5)
print("Left Rotation :", d)


# Limit Deque size

import random
random.seed(1)

d1 = collections.deque(maxlen=3)
d2 = collections.deque(maxlen=3)

print('*' * 40)

for i in range(5):
    n = random.randint(0, 10)
    print("n = ", n)
    d1.append(n)
    d2.appendleft(n)
    print('D1 :', d1)
    print('D2 :', d2)



# Moving Average

from collections import deque
import itertools

def moving_average(iterable, n=3):
    """
    Iterates over iterable and calculates moving average
    
    """
    it = iter(iterable)
    d = deque(itertools.islice(it, n-1))
    d.appendleft(0)
    s = sum(d)
    
    for item in it:
        s += item - d.popleft()
        d.append(item)
        yield s / n

my_list = [40, 30, 50, 46, 39, 44]

print("Moving Averages :")
print(list(moving_average(my_list)))
