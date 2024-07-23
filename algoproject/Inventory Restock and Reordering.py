class InventoryManager:
    def __init__(self, inventory):
        self.inventory = inventory

    def check_stock(self):
        low_stock_items = [item for item in self.inventory.items if item.stock < 5]
        return low_stock_items

    def reorder_items(self):
        low_stock_items = self.check_stock()
        for item in low_stock_items:
            print(f"Reordering item: {item.title} (ISBN: {item.isbn})")
