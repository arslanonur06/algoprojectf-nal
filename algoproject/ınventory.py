class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        self.items.sort(key=lambda x: x.isbn)  # Sort by ISBN

    def find_item(self, isbn):
        left, right = 0, len(self.items) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.items[mid].isbn == isbn:
                return self.items[mid]
            elif self.items[mid].isbn < isbn:
                left = mid + 1
            else:
                right = mid - 1
        return None
