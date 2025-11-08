def product():
    """ TODO: Takes three inputs (or two) and print the product"""

# TODO: product(1, 1, 1)	# 1
# TODO: product(1, 2, 3)	# 6
# TODO: product(2, 5, 10)	# 100
# TODO: product(3, 3)	    # 9
# TODO: product(2, 5)	    # 12

def get_product(num1, num2, num3=1):
    return num1 * num2 * num3


test1 = get_product(1, 1, 1)
print(test1)

test2 = get_product(1, 2, 3)
print(test2)

test3 = get_product(2, 5, 10)
print(test3)

test4 = get_product(3, 3)
print(test4)

test5 = get_product(2, 5)
print(test5)


