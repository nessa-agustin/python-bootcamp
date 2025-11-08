def product():
    """TODO: Takes three inputs and print the product"""

# TODO: product(1, 1, 1)	# 1
# TODO: product(1, 2, 3)	# 6
# TODO: product(2, 5, 10)	# 100

def get_product(num1, num2, num3):
    # product_result = num1 * num2 * num3
    return num1 * num2 * num3


number1 = int(input('Enter num1: '))
number2 = int(input('Enter num2: '))
number3 = int(input('Enter num3: '))

product_result = get_product(number1, number2, number3)
print(product_result)


