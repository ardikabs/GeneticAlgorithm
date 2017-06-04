from reader import fileReader
from helper import Const as c
import GeneticAlgorithm as GA
import matplotlib.pyplot as plt
from matplotlib import animation  


text = None
ax = None
def initial_graph(xlists=[],ylists=[]):
	fig = plt.figure(figsize=(15,10),dpi=80)
	fig.suptitle("K-Means Optimazation with Genetic Algorithm", fontsize=14, fontweight='bold')
	plt.ion()
	plt.xlabel('X')
	plt.ylabel('Y')
	plt.title('Ruspini Dataset')
	plt.plot(xlists, ylists, 'ro',color="black",label="Ruspini data")
	plt.grid(True)
	plt.legend()
	plt.axis([0, c.max_x+10, 0, c.max_y+10])
	plt.show(block=False)

if __name__ == "__main__":
	
	file 			= "ruspini.data"
	ds_ruspini 		=  fileReader(file)
	all_individu 	= GA.initPopulation()
	centroid		= None

	listsX = [data.x for data in ds_ruspini]
	listsY = [data.y for data in ds_ruspini]
	initial_graph(listsX,listsY)
	

	for i in range(c.jml_generasi):
		fitness 		= GA.fitnessProcess(ds_ruspini,all_individu)
		all_individu	= GA.rouletteSelection(all_individu,fitness)
		all_induk 		= GA.cloning(all_individu)

		all_individu 	= GA.crossOver(all_individu)
		all_individu 	= GA.mutasi(all_individu)

		all_anak 		= GA.cloning(all_individu)

		all_individu 	= GA.elitism(all_induk,all_anak,ds_ruspini)
		all_individu 	= GA.cloning(all_individu)

		ax = plt.gca()
		for item in ax.collections:
			item.remove()

		centroid = all_individu[0]
		fitnessCentroid = GA.fitnessCentroid(ds_ruspini,centroid)

		# for j in range(len(centroid.kromosom)):
		# 	plt.scatter(centroid.kromosom[j].x,centroid.kromosom[j].y,color="blue")
		# 	plt.draw()

		# print "Generasi ke : {}".format(i)
		# print "Nilai Fitness : {} (Minimasi)".format(fitnessCentroid)
		# print "\n"
		
		# plt.pause(0.1)

	for j in range(len(centroid.kromosom)):
		ax = plt.gca()
		for item in ax.collections:
			item.remove()
		if j == 0:
			plt.plot(centroid.kromosom[j].x,centroid.kromosom[j].y,"ro",color="red",label="Optimized Centroid {}".format(j+1))
		elif j == 1:	
			plt.plot(centroid.kromosom[j].x,centroid.kromosom[j].y,"ro",color="yellow",label="Optimized Centroid {}".format(j+1))
		elif j == 2:	
			plt.plot(centroid.kromosom[j].x,centroid.kromosom[j].y,"ro",color="magenta",label="Optimized Centroid {}".format(j+1))
		elif j == 3:	
			plt.plot(centroid.kromosom[j].x,centroid.kromosom[j].y,"ro",color="cyan",label="Optimized Centroid {}".format(j+1))

		plt.legend()
		plt.draw()

	plt.show()
	raw_input("PRESS ANY KEY TO CONTINUE.")
	plt.close(plt.figure(figsize=(15,10),dpi=80))




