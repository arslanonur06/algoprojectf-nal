if __name__ == "__main__":
    inventory = Inventory()
    transaction_manager = TransactionManager()
    customer_queue = CustomerQueue()

    # Add inventory items
    inventory.add_item(InventoryItem("1234567890", "Book Title 1", "Author 1", 10, 29.99))
    inventory.add_item(InventoryItem("0987654321", "Book Title 2", "Author 2", 5, 39.99))

    # Process a transaction
    transaction_manager.add_transaction("Purchase: Book Title 1")
    transaction_manager.process_transaction()

    # Add customers
    customer_queue.add_customer(Customer("Alice", 1))
    customer_queue.add_customer(Customer("Bob", 2))

    # Generate reports
    report = Report(inventory, transaction_manager, customer_queue)
    report.generate_inventory_report()
    report.generate_transaction_report()
    report.generate_customer_report()
