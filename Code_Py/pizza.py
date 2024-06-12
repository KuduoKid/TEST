pizza = {
    'crust': 'thick', 
    'toppings': ['mushroom', 'extra cheese']
    }
print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\"{topping}\"")  # 使用f-string正确插入变量值
    #print("\"f + f'topping')


