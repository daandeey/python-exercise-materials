"""
Orchestrator for the Inventory exercise. This is the "main.py" of
the project - it imports the inventory module and drives it, the
same way main.py did in 03_organizing_project/. You shouldn't need
to change this file; the exercise is in inventory.py.

Run:
    python main.py
"""
import inventory

if __name__ == "__main__":
    stock = {}

    inventory.add_item(stock, "Keyboard", 250_000, 10)
    inventory.add_item(stock, "Mouse", 100_000, 3)
    inventory.add_item(stock, "Keyboard", 250_000, 5)   # restock -> qty becomes 15

    inventory.remove_item(stock, "Mouse", 1)             # qty becomes 2
    inventory.remove_item(stock, "Monitor", 1)           # Item not found.
    inventory.remove_item(stock, "Keyboard", 100)        # Insufficient stock.

    print("Stock:", stock)
    print("Total value:", inventory.get_total_value(stock))
    print("Low stock (threshold=5):", inventory.list_low_stock(stock))

    # Expected output:
    # Item not found.
    # Insufficient stock.
    # Stock: {'Keyboard': {'price': 250000, 'qty': 15}, 'Mouse': {'price': 100000, 'qty': 2}}
    # Total value: 3950000
    # Low stock (threshold=5): ['Mouse']
