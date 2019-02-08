
#task a
def fun_1(index2,index1,string2,string1):
	streets=[]
	roads=[]
	file1=open('Street_Centrelines.csv')
	file2=open('Bus_Stops.csv')

	for sentens in file2:
		sent=sentens.strip()
		list2=sent.split(',')
		if list2[index2]==string2:
			if list2[9] not in streets:
				streets.append(list2[9])
			else:
				pass

	for lines in file1:
		line=lines.strip()
		list1=line.split(',')
		if list1[index1]==string1:
			if list1[23] in streets:
				roads.append(list1[4])
	return roads
print(fun_1(7,10,'Accessible','ARTERIAL'))
