class InventoryManagementSystem:
    def __init__(self):
        # Initialize the inventory as an empty dictionary
        self.inventory = {}

    def add_item(self, item_name, quantity, price):
        """Add a new item to the inventory."""
        # Check if the item already exists in the inventory
        if item_name in self.inventory:
            print(f"{item_name} already exists. Updating quantity and price.")
            # If it exists, update the quantity and price
            self.inventory[item_name]['quantity'] += quantity
            self.inventory[item_name]['price'] = price  # Update price
        else:
            # If it doesn't exist, create a new entry in the inventory
            self.inventory[item_name] = {'quantity': quantity, 'price': price}
        # Print confirmation of the addition or update
        print(f"Added/Updated {item_name}: {quantity} units at ${price:.2f} each.")

    def update_item(self, item_name, quantity=None, price=None):
        """Update an existing item in the inventory."""
        # Check if the item exists in the inventory
        if item_name in self.inventory:
            # If a new quantity is provided, update it
            if quantity is not None:
                self.inventory[item_name]['quantity'] = quantity
            # If a new price is provided, update it
            if price is not None:
                self.inventory[item_name]['price'] = price
            # Print confirmation of the update
            print(f"Updated {item_name}: {self.inventory[item_name]['quantity']} units at ${self.inventory[item_name]['price']:.2f} each.")
        else:
            # If the item does not exist, notify the user
            print(f"{item_name} does not exist in the inventory.")

    def delete_item(self, item_name):
        """Remove an item from the inventory."""
        # Check if the item exists in the inventory
        if item_name in self.inventory:
            # If it exists, delete the item
            del self.inventory[item_name]
            print(f"Deleted {item_name} from inventory.")
        else:
            # If the item does not exist, notify the user
            print(f"{item_name} does not exist in the inventory.")

    def view_inventory(self):
        """Display the current inventory."""
        # Check if the inventory is empty
        if not self.inventory:
            print("Inventory is empty.")
        else:
            # If not empty, display each item with its details
            print("Current Inventory:")
            for item_name, details in self.inventory.items():
                print(f"{item_name}: {details['quantity']} units at ${details['price']:.2f} each.")

def main():
    # Create an instance of the InventoryManagementSystem
    inventory_system = InventoryManagementSystem()

    while True:
        # Display the main menu
        print("\n Inventory Management System")
        print("1. Add Item")
        print("2. Update Item")
        print("3. Delete Item")
        print("4. View Inventory")
        print("5. Exit")
        choice = input("\n Select an option: ")

        # Handle user choice for adding an item
        if choice == '1':
            name = input("Enter item name: ")
            qty = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            inventory_system.add_item(name, qty, price)
        # Handle user choice for updating an item
        elif choice == '2':
            name = input("Enter item name to update: ")
            qty = input("Enter new quantity (leave blank to keep current): ")
            price = input("Enter new price (leave blank to keep current): ")
            # Convert inputs to appropriate types or keep them None
            qty = int(qty) if qty else None
            price = float(price) if price else None
            inventory_system.update_item(name, qty, price)
        # Handle user choice for deleting an item
        elif choice == '3':
            name = input("Enter item name to delete: ")
            inventory_system.delete_item(name)
        # Handle user choice for viewing the inventory
        elif choice == '4':
            inventory_system.view_inventory()
        # Handle user choice for exiting the system
        elif choice == '5':
            print("\n Exiting the system.")
            break
        else:
            # Notify user of invalid option
            print("\n Invalid option. Please try again.")

main()
