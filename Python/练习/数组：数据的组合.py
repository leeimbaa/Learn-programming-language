记录粉丝对他的好感度
他一共有五个粉丝
fs1=90
fs2=85
fs3=60
fs4=87
fs5=99

1.
fs=[90,85,60,87,99]

fs[0]+=1
fs[1]+=1
fs[2]+=1
fs[3]+=1
fs[4]+=1

print(fs[0])
print(fs[1])
print(fs[2])
print(fs[3])
print(fs[4])

2.
fs=[90,85,60,87,99] #定义数组fs
i=1                 #定义变量i为1
while i<5:			#当i小于5时
	fs[i]+=1		#把数组中每组数据都+1	
	i+=1            #把变量i的值+1，再返回i
print(fs[0])		#打印数组中第一个数据fs[0]的值
print(fs[1])		#打印数组中第一个数据fs[1]的值
print(fs[2])		#打印数组中第一个数据fs[2]的值
print(fs[3])		#打印数组中第一个数据fs[3]的值
print(fs[4])		#打印数组中第一个数据fs[4]的值

3.
fs=[90,85,60,87,99]
i=0
while i<5:
	fs[i]+=1
	print(fs[i])
	i+=1
4.
fs=[90,85,60,87,99,12,121,456,1231,4564,1231,45641321,456,1231,451231,5412]
i=0
while i<16:
  fs[i]+=1
  print(fs[i])
  i+=1
 
5.
fs=[90,85,60,87,99,12,121,456,1231,4564,1231,45641321,456,1231,451231,5412]
i=0
while i<len(fs):
  fs[i]+=1
  print(fs[i])
  i+=1
 
6.
fs=[90,85,60,87,99,12,121,456,1231,4564,1231,45641321,456,1231,451231,5412]
i=0
for i in fs:
	i+=1
for i in fs:
	print(i)

7.
