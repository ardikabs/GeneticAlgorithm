from ruspini import Ruspini as Rs
from helper import Const as c
def fileReader(files):
	dataset = []
	with open(files,'r') as ins :
		datalist = ins.read().splitlines()
		for i in range(len(datalist)):
			line = datalist[i]
			lists = line.split(',')
			temp = Rs(i,lists[0],lists[1],lists[2])
			dataset.append(temp)
			
			if(int(lists[0]) > c.max_x):
				c.max_x = int(lists[0])
			if(int(lists[1]) > c.max_y):
				c.max_y = int(lists[1])
	return dataset

