items = ["rice", "noodles", "toyo", "spam", "coffee"]
item_to_find = "spam"

for item in items:
    # TODO: If item equals the item_to_find
    #  # print and exit loop
    print('Current Item: ', item)
    if item == item_to_find:
        print('Item found: ', item_to_find)
        break


# continue - non-linear skips
# break - stop loop