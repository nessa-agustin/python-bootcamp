class Item:
    def __init__(self, item_name, item_info):
        self.item_name = item_name
        self.item_info = item_info

class Inventory(Item):
    def __init__(self):
        self.inventory: list[Item] = []

    def add(self):
        item_name = input("Item name: ")
        item_info = input("Item info: ")
        new_item = Item(item_name, item_info)
        # item = {"Name": item_name, "Info": item_info}
        self.inventory.append(new_item)
        print(self.inventory)

    def remove(self):
        index = int(input("Index (remove): "))
        removed_item = self.inventory.pop(index)
        print(f"{removed_item} removed from inventory\n")

    def read(self):
        index = int(input("Index (read): "))
        item = self.inventory[index]
        # print(f"Item {index}: {item}\n")
        print(f"Item {item.item_name}: {item.item_info}\n")

    def show(self):
        if not self.inventory:
            print("Inventory is empty.\n")
            return

        for number, item in enumerate(self.inventory, start=1):
            print(f"Item {number}:")

            # for key, value in info_detail.items():
            print(f"\t{item.item_name}: {item.item_info}")

    
    def main(self):
        running = True
        # item_detail = str | int | float
        # inventory: list[dict[str, item_detail]] = []

        while running:
            command = input("Command: ").strip().lower()

            if command == "add":
                self.add()
            elif command == "remove":
                self.remove()
            elif command == "read":
                self.read()
            elif command == "show":
                self.show()
            elif command == "exit":
                running = False
                print("Exiting...")


inv = Inventory()
inv.main()