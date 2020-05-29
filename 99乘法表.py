x = 1 
while x <= 9:
  y = 1
  while y <= x:
    print("%d*%d=%d\t"%(y,x,x*y),end="")
    y += 1
  print("") #换行
  x += 1
print("结束")
