#虽然不能修改元组的元素，但可以给存储元组的变量赋值,如果要修改前述矩形的尺寸，可重新定义整个元组
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
 print(dimension)

 #Change
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
 print(dimension)

#每级缩进都使用四个空格,每行都不要超过80字符,不要在程序文件中过多使用空行
#对你使用的编辑器进行设置，使其在第80个字符处显示一条垂直参考线


