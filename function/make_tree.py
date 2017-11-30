import copy
import math

# create the tree using the frequencies using huffmann algorithm
def makeTree(list):
	sum =0

	for i in list:
		sum += i[1]

	while(list[0][1] < sum and len(list) > 2):

		minval1 = math.inf

		for i in range(len(list)):

			if(list[i][1] < minval1 and list[i][1] > 0):
				minval1 = list[i][1]
				min1 = i
				x = copy.deepcopy(list[i])

		list[min1][1] = -1000

		minval2 = math.inf

		for i in range(len(list)):

			if(list[i][1] < minval2 and list[i][1] > 0):
				minval2 = list[i][1]
				min2 = i
				y = copy.deepcopy(list[i])

		list[min2][1] = -1000

		name = str(list[min1][0]) + str(list[min2][0])
		val = minval1 + minval2
			
		list.append([name,val,[x,y]])
		
		if(min1 < min2):
			list.pop(min1)
			if(min2 == 0):
				list.pop(min2)

			else:
				list.pop(min2 - 1)
		elif(min1 > min2):
			list.pop(min1)
			list.pop(min2)


	z =copy.deepcopy(list[0])
	if(z[1] < list[1][1]):
		name = z[0]+ list[1][0]
		val = z[1] + list[1][1]

	
		list.append([name,val,[z,list[1]]])
	else:
		name = list[1][0] + z[0]
		val = list[1][1] + z[1]

	
		list.append([name,val,[list[1],z]])
	
	list.pop(0)
	list.pop(0)

	return list 
