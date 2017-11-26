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
sum = 0
for n in range(201):
    if n % 2 == 1 or n < 99:
	    continue 
    else :
	    sum = sum + n
print(sum)