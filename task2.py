

#task a
def fun_1(string2,string1):
	streets=[]
	roads=[]
	file1=open('Street_Centrelines.csv')
	file2=open('Bus_Stops.csv')

	for sentens in file2:
		sent=sentens.strip()
		list2=sent.split(',')
		if list2[7]==string2:
			if list2[9] not in streets:
				streets.append(list2[9])
			else:
				pass

	for lines in file1:
		line=lines.strip()
		list1=line.split(',')
		if list1[10]==string1:
			if list1[23] in streets:
				roads.append(list1[4])
	return roads
print(fun_1('Accessible','ARTERIAL'))

#task b
def fun2():
	'''Prints local street with a  non standard bus stop'''
	other=fun_1('Non-Standard','LOCAL STREET')
	print(other)
fun2()

#task3
def fun3():
	new=fun_1('Inaccessible','MINOR COLLECTOR')
	print(new)
fun3()
