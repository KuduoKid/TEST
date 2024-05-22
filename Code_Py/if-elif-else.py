#4岁以下免费；4～18岁收费25美元；18岁（含）以上收费40美元
age = 12
if age < 4:
 print("Your admission cost is $0.")
elif age < 18:
 print("Your admission cost is $25.")
else:
 print("Your admission cost is $40.")
#使用多个elif代码块
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}.")
#但if-elif-else 结构的作用更小：它只确定门票价格，而不是在确定门票价格的同时打印一条消息

#省略else代码块
age = 12
if age < 4:
 price = 0
elif age < 18:
 price = 25
elif age < 65:
 price = 40
elif age >= 65:
 price = 20
print(f"Your admission cost is ${price}.")
#除效率更高外，这些修订后的代码还更容易修改：要调整输出消息的内容，只需修改一个而不是三个函数调用print()

#else 是一条包罗万象的语句，只要不满足任何if 或elif 中的条件测试，其中的代码就会执行。这可能引入无效甚至恶意的数据
#每个代码块都仅在通过了相应的测试时才会执行
#如果if 测试和elif 测试都未通过，Python将运行else代码块中的代码
#如果只想执行一个代码块，就使用if-elif-else 结构；如果要执行多个代码块，就使用一系列独立的if 语句




