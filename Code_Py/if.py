#1 检查是否相等

#2 一个等号是陈述,两个等号则是发问
#如果大小写很重要，这种行为有其优点。但如果大小写无关紧要，只想检查变量的值，可将变量的值转换为小写，再进行比较

#3 检查是否不相等
#要判断两个值是否不等，可结合使用惊叹号和等号 !=

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
 print("Hold the anchovies!")
#你编写的大多数条件表达式检查两个值是否相等，但有时候检查两个值是否不等的效率更高

#使用and检查多个条件
#使用or检查多个条件
#检查特定值是否包含在列表中,可使用关键字in

requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings
print('mushrooms' in requested_toppings)

#检查特定值是否不包含在列表中,使用关键字 not in
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
 print(f"{user.title()}, you can post a response if you wish.")

#布尔表达式,布尔值通常用于记录条件,在跟踪程序状态或程序中重要的条件方面，布尔值提供了一种高效的方式











