# Ask the cost and pax or count for three separate items
item_cost_1 = int(input('Enter cost for Item1: \n'))  # Let the user enter a number
item_count_1 = int(input('Enter quantity for Item1: \n'))  # Let the user enter a number

item_cost_2 = int(input('Enter cost for Item2: \n'))  # Let the user enter a number
item_count_2 = int(input('Enter quantity for Item2: \n'))  # Let the user enter a number

item_cost_3 = int(input('Enter cost for Item3: \n'))  # Let the user enter a number
item_count_3 = int(input('Enter quantity for Item3: \n'))  # Let the user enter a number

# Calculate the total
total_item1 = item_cost_1 * item_count_1
total_item2 = item_cost_2 * item_count_2
total_item3 = item_cost_3 * item_count_3
total = total_item1 + total_item2 + total_item3
print(total)