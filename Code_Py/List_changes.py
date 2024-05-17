
name = ['a', 'b', 'c']
changes = 'a'
name.remove(changes)

invite = ("inviting you to dinner together")
for inviting in name:
    print(inviting, ",", invite)

print(f"Unfortunately,  {changes} is unable to attend dinner.")
# f: 格式化字符串, 加f后可以在字符串里面使用用花括号括起来的变量和表达式


#方法remove()用法
"""
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)


changes = name.remove('a') 
方法 remove() 无返回值

print(changes)
print("Unfortunately, " changes " is unable to attend dinner.")
所以打印结果为:Unfortunately, None is unable to attend dinner.

"""
