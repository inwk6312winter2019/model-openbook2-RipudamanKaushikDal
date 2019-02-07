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
			if list2[6] not in streets:
				rd=list2[6]
				streets.append(rd.lower())
			else:
				pass

	for lines in file1:
		line=lines.strip()
		list1=line.split(',')
		if list1[10]=='ARTERIAL':
			st=list1[2]
			if st.lower() in streets:
				roads.append(st)
	return roads
print(fun_1())
