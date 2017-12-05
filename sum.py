#print the sum of number from 1 to 100
# sum = 0
# for x in range(101):
  # sum = sum + x
# print(sum)



#calculate the even number from 100 to 200 计算100到200之间的偶数和
# sum = 0
# n = 100
# while n < 201 and n > 99:
    # sum = sum + n
    # n = n + 2
# print(sum)


#calculate the even number from 100 to 200 计算100到200之间的偶数和
#sum = 0
# for n in range(201):
    # if n % 2 == 1 or n < 99:
	    # continue 
    # else :
	    # sum = sum + n
# print(sum)


#Sonia@20171126让用户输入两个数，A,B,计算从A加到B
# def is_number(s):
    # try:
        # float(s)
        # return True
    # except ValueError:
        # pass
 
    # try:
        # import unicodedata
        # unicodedata.numeric(s)
        # return True
    # except (TypeError, ValueError):
        # pass
 
    # return False

# while True:
    # a = input("please input an integer\n")
    # if (is_number(a)):
        # a = int(a)  #此时a才是int类型的
        # break  
    # else:
        # print("Error Input, please input again\n")
# while True:
    # b = input("please input an integer\n")
    # if (is_number(b)):
        # b = int(b)  #同上
        # break		
    # else:
        # print("Error Input, please input again\n")

# sum = 0  #同样要用到的参数，可以考虑丢外面
# if a > b:
    # while a >= b:
        # sum += b
        # b = b + 1
# elif a < b:
    # while a <= b:
        # sum += a  #同上
        # a = a + 1
# else:
    # sum = a + b 
    
# print(sum) 

# x年收入，y%年利率复利，z小目标。全都是浮点数
# 要么输出n年达到小目标，如果n>40，输出，n-40
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False
	
while True:
    x = input("请输入年金x\n")
    if (is_number(x)):
        x = float(x)  
        break  
    else:
        print("Error Input, please input again\n")
		
while True:
    y = input("请输入年利率y\n")
    if (is_number(y)):
        y = float(y)  
        break		
    else:
        print("Error Input, please input again\n")
		
while True:
    z = input("请输入小目标z\n")
    if (is_number(z)):
        z = float(z)  
        break 
    else:
        print("Error Input,please input again\n")
		
# while !is_number(x)
sum = 0
n = 0
while sum < z:
    sum = x + sum*(1+y)
    n = n + 1
if n > 40: 
    print("复利终值=", sum, ", 相差年数=", (n - 40))
else:	
    print("复利终值=", sum, ", 相差年数=", n)	

# 这个notepad++最上面的标题栏表明了当前文件的位置，打开即可
# 打开了.py文件所在的目录之后，在该目录下打开命令行
# 按住shift键然后在空白处右键单击鼠标，选择在此处打开命令行
# Windows10 打开的默认是powershell窗口而不是cmd窗口，功能是一样的
# 你试试看
