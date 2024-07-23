class Report:
    def __init__(self, inventory, transaction_manager, customer_queue):
        self.inventory = inventory
        self.transaction_manager = transaction_manager
        self.customer_queue = customer_queue

    def generate_inventory_report(self):
        print("Inventory Report:")
        for item in self.inventory.items:
            print(f"{item.title} (ISBN: {item.isbn}) - Stock: {item.stock}, Price: {item.price}")

    def generate_transaction_report(self):
        print("Transaction Report:")
        transactions = []
        while not self.transaction_manager.transaction_stack.is_empty():
            transactions.append(self.transaction_manager.process_transaction())
        for transaction in transactions:
            print(transaction)

    def generate_customer_report(self):
        print("Customer Queue Report:")
        for customer in self.customer_queue.queue:
            print(f"Customer: {customer.name}, Priority: {customer.priority}")
