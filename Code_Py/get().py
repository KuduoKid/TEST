#方法get()的第一个参数用于指定键，必不可少；
#第二个参数为指定的键不存在时要返回的值，是可选的
#调用get() 时，如果没有指定第二个参数且指定的键不存在，Python将返回值None
alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)
