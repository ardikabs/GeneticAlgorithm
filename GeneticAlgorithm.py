
from helper import Const as c
from kromosom import Kromosom
from individu import Individu
import random
import math
from operator import itemgetter


def initPopulation():
	individu = []

	for i in range(c.jml_individu):
		value = Individu(randomizerKromosom())
		individu.append(value)

	return individu

def randomizerKromosom():
	kromosom = []

	for i in range(c.jml_kromosom):
		rand_x = random.randint(0,c.max_x+1)
		rand_y = random.randint(0,c.max_y+1)
		value = Kromosom(rand_x,rand_y)
		kromosom.append(value)	

	return kromosom

def fitnessProcess(data,individu):
	fitness = [0]*len(individu)

	for i in range(len(individu)):
		temp_jarak = 0
		for j in range(len(data)):
			temp_jarak += distance(data[j],individu[i])

		temp_jarak = 1/temp_jarak
		fitness[i] = (temp_jarak)
 
	for i in range(len(fitness)):
		if(i>0):
			fitness[i] = fitness[i-1] + fitness[i]*1000 
		else:
			fitness[i] = fitness[i]*1000

	return fitness

def fitnessCentroid(data,centroid):
	temp_jarak = 0.0
	for i in range(len(data)):
		temp_jarak += distance(data[i],centroid)
	return temp_jarak
	


def distance(data,individu):
	jarak = []

	for i in range(len(individu.kromosom)):
		valueX = math.pow(individu.kromosom[i].x - data.x,2)
		valueY = math.pow(individu.kromosom[i].y - data.y,2)
		result = math.sqrt(valueX+valueY)
		jarak.append(result)

	jarak.sort()
	return jarak[0]	

def rouletteSelection(individu,fitness):
	newIndividu = [0]*len(individu)

	for i in range(len(individu)):
		newIndividu[i] = individu[roulette(fitness)]

	return newIndividu

def roulette(fitness):
	comp = random.uniform(0,fitness[-1])

	for i in range(len(fitness)):
		if(comp <= fitness[i]):
			return i
	return 0

def cloning(individu):
	newIndividu = []

	for i in range(len(individu)):
		kromosom = []

		for j in range(len(individu[i].kromosom)):
			temp_x = individu[i].kromosom[j].x
			temp_y = individu[i].kromosom[j].y
			valueKrom = Kromosom(temp_x,temp_y)
			kromosom.append(valueKrom)

		valueInd = Individu(kromosom)
		newIndividu.append(valueInd)

	return newIndividu

def crossOver(individu):
	newIndividu = cloning(individu)

	for i in range(0,len(individu),2):
		induk1 = newIndividu[i]
		induk2 = newIndividu[i+1]

		if( random.uniform(0,1) < c.prob_CO):
			# TODO kawinkan
			index1=None
			index2=None
			tpoint1 = random.randint(0,c.jml_gen*c.jml_kromosom)
			tpoint2 = random.randint(0,c.jml_gen*c.jml_kromosom)

			if(tpoint1<=tpoint2):
				index1 = tpoint1
				index2 = tpoint2
			else:
				index1 = tpoint2
				index2 = tpoint1

			for j in range(index1,index2):
				if(j%2 == 0):
					temp_x = induk1.kromosom[j/2].x
					induk1.kromosom[j/2].x = induk2.kromosom[j/2].x
					induk2.kromosom[j/2].x = temp_x
				else:
					temp_y = induk1.kromosom[j/2].y
					induk1.kromosom[j/2].y = induk1.kromosom[j/2].y
					induk2.kromosom[j/2].y = temp_y
	return newIndividu

def mutasi(individu):
	newIndividu = cloning(individu)

	shift_x = c.max_x / 100
	shift_y = c.max_y / 100

	for i in range(len(individu)):
		index = random.randint(0,c.jml_gen*c.jml_kromosom-1)
		if(random.uniform(0,1) < c.prob_M):
			sign = 0
			if(random.randint(0,1) > 0):
				sign = 1
			else:
				sign = -1

			if(index%2 == 0):
				value = newIndividu[i].kromosom[index/2].x + (shift_x*sign)
				if(value > c.max_x):
					sign = -1
				elif(value < 0):
					sign = 1
				
				value = newIndividu[i].kromosom[index/2].x + (shift_x*sign)
				newIndividu[i].kromosom[index/2].x = value
			 
			else:
				value = newIndividu[i].kromosom[index/2].y + (shift_y*sign)
				if(value > c.max_y):
					sign = -1
				elif(value < 0):
					sign = 1
				value = newIndividu[i].kromosom[index/2].y + (shift_y*sign)
				newIndividu[i].kromosom[index/2].y = value

	return newIndividu


def elitism(induk,anak,data):
	individu = cloning(induk)
	individu.extend(cloning(anak))
	comparator = []
	selectedIndividu = []
	for i in range(len(individu)):
		temp_jarak = 0
		for j in range(len(data)):
			temp_jarak += distance(data[j],individu[i])
		value = i,temp_jarak
		comparator.append(value)

	comparator.sort(key=itemgetter(1),reverse=False)
	for i in range(len(individu) - len(induk)):
		selectedIndividu.append(individu[comparator[i][0]])
	return selectedIndividu









