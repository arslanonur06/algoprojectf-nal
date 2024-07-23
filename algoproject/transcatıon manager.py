class TransactionManager:
    def __init__(self):
        self.transaction_stack = Stack()

    def add_transaction(self, transaction):
        self.transaction_stack.push(transaction)

    def process_transaction(self):
        return self.transaction_stack.pop()

    def undo_transaction(self):
        return self.transaction_stack.pop()
