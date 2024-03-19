"""
Copyright (c) 2024 Author. All Rights Reserved.
Queue implementation to use with algorithms
"""


class Queue:
    """
    FIFO Queue implementation
    """

    def __init__(self):
        """
        Initialize the queue
        """
        self.queue = []

    def enqueue(self, item):
        """
        Add an item to the queue
        """
        self.queue.append(item)

    def dequeue(self):
        """
        Remove an item from the queue
        """
        return self.queue.pop(0)

    def is_empty(self):
        """
        Check if the queue is empty
        """
        return len(self.queue) == 0

    def size(self):
        """
        Return the size of the queue
        """
        return len(self.queue)
