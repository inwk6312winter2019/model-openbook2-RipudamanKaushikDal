
#task a
def fun_1():
	streets=[]
	roads=[]
	file1=open('Street_Centrelines.csv')
	file2=open('Bus_Stops.csv')

	for sentens in file2:
		sent=sentens.strip()
		list2=sent.split(',')
		if list2[7]=='Accessible':
			if list2[9] not in streets:
				streets.append(list2[9])
			else:
				pass

	for lines in file1:
		line=lines.strip()
		list1=line.split(',')
		if list1[10]=='ARTERIAL':
			if list1[23] in streets:
				roads.append(list1[4])
	return roads
print(fun_1())
