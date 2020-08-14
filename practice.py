print('Health managment system :  ')
def getdate():
    import datetime
    return datetime.datetime.now()
import datetime
def gettime():
    return datetime.datetime.now()
a = int(input('Enter  1 : lock.  2 : reterive\n'))
if a == 1:
	filename = input('filename : ');
	value = input('Type here\n')
	with open(filename + ".txt" , 'a') as f:
		f.write (str([str(gettime())]) + ":" + value + "\n");
	num = int(input('you want to add more please type 1: Yes  2: No\n'))
	if num == 1:
				while(True):
					value = input('Type here\n')
					with open(filename + ".txt" , 'a') as f:
						f.write (str([str(gettime())]) + ":" + value + "\n");
					num = int(input('you want to add more please type 1: Yes  2: No\n'))
					if num==2:
						print('Item added successfully')
						break
if a == 2:
	filename = input('filename : ');
	with open(filename + ".txt" ) as f:
		for i in f:
			print(i,end = " ")
#else:
#	print('Item added successfully')