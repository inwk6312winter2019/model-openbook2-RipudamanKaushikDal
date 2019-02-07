#task a
def make_tup():
	file=open('Street_Centrelines.csv')
	for lines in file:
		line=lines.strip()
		mylist=line.split(',')
		Tup=(mylist[2],mylist[4],mylist[6],mylist[7])
		print(Tup,'\n')
make_tup()

#task b
def hist():
	dic={}
	file=open('Street_Centrelines.csv')
	for lines in file:
		line=lines.strip()
		mylist=line.split(',')
		if mylist[12] not in dic:
			dic[mylist[12]]=1
		else:
			dic[mylist[12]]+=1
	return dic
print(hist())

#task c
def get_owned():
	newlist=[]
	file=open('Street_Centrelines.csv')
	for lines in file:
		line=lines.strip()
		mylist=line.split(',')
		newlist.append(mylist[11])
	return newlist
print(get_owned())

#task d
def Street_list():
	d={}
	file=open('Street_Centrelines.csv')
	for lines in file:
		line=lines.strip()
		mylist=line.split(',')
		if mylist[10] not in  d:
			d[mylist[10]]=[mylist[2]]
		else:
			d[mylist[10]].append(mylist[2])
	return d
print(Street_list())
