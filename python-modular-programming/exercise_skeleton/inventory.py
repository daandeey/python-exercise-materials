"""
EXERCISE SKELETON - Python Modular Programming
=============================================================
Build a small "Inventory Management" MODULE - this mirrors how a
real project separates responsibilities:
    inventory.py (THIS FILE) -> the reusable module: data logic only
    main.py                  -> the orchestrator: imports + uses it

Fill in the TODOs below, then run main.py (not this file) to test:
    python main.py

An inventory is represented as a dict:
    {"Keyboard": {"price": 250000, "qty": 10}, ...}
"""

# =================================================================
# EXERCISE: Inventory Module
# =================================================================

# -----------------------------------------------------------------
# add_item(inventory, name, price, qty)
#   -> if `name` already exists in inventory, ADD qty to its
#      existing qty (a restock)
#   -> otherwise, create a new entry {"price": price, "qty": qty}
#
# HINT: use the `in` operator to check if a key already exists.
def add_item(inventory, name, price, qty):
    # TODO: implement
    pass


# -----------------------------------------------------------------
# remove_item(inventory, name, qty)
#   -> if `name` doesn't exist in inventory, print "Item not
#      found." and return
#   -> if qty requested is MORE than qty in stock, print
#      "Insufficient stock." and return
#   -> otherwise, subtract qty; if the remaining qty reaches 0,
#      remove the item from inventory entirely
def remove_item(inventory, name, qty):
    # TODO: implement
    pass


# -----------------------------------------------------------------
# get_total_value(inventory)
#   -> return the total value of all stock: sum of (price * qty)
#      for every item
def get_total_value(inventory):
    # TODO: implement
    pass


# -----------------------------------------------------------------
# list_low_stock(inventory, threshold=5)
#   -> return a list of item names whose qty is below threshold
def list_low_stock(inventory, threshold=5):
    # TODO: implement
    pass
