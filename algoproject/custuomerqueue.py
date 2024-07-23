class Customer:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

class CustomerQueue:
    def __init__(self):
        self.queue = []

    def add_customer(self, customer):
        self.queue.append(customer)
        self.queue.sort(key=lambda x: x.priority, reverse=True)  # Higher priority first

    def serve_customer(self):
        if self.queue:
            return self.queue.pop(0)
