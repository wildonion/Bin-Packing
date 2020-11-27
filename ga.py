



# ----------------- 1D BIN PACKING PROBLEM USING GENETIC ALGORITHM -----------------
# ----------------------------------------------------------------------------------


import numpy as np
import random
from bppga import chromosome, ga


# =================================
OBJECTS     = [6, 9, 4, 3, 5, 2]
CAPACITY    = 13
POP_SIZE    = 40 # size of population
GENERATION  = 10
# BEST_OUTPUT = []
# =================================

# create a population from bins
# bin = gene | population = 40 and set of chromosomes | chromosome = a list of bins
population = np.array([chromosome(OBJECTS, CAPACITY) for i in range(POP_SIZE)])
ga = ga(population)



# termination condition
for generation in range(GENERATION):

	print(f"\n[+] Generation >>>>>>>>> {generation} ")
	

	fitness = ga.fitness(ga.population) # total fitness for all chromosomes
	print(f"[+] Fitness >>>>>>>>> {sum(fitness)}")

	# BEST_OUTPUT.append(ga.population)
	# # The best result in the current iteration.
	# for bo in BEST_OUTPUT:
	# 	for p in bo:
	# 		print(f"\n[+] Best result :::::::::::: {p.permutation}")
	
	# Selecting parents in the population for mating.
	parents = np.array(ga.wheel_roulette_selection(2))
	# print("\n[+] Parents")
	# print(parents)
	
	# Generating next generation using crossover.
	offspring_crossover = ga.crossover(parents, offspring_size=(POP_SIZE-len(parents), len(parents[0])))
	# print("\n[+] Crossover")
	# print(offspring_crossover)
	
	# Adding some variations to the offsrping using mutation.
	offspring_mutation = ga.mutate(offspring_crossover, OBJECTS, CAPACITY)
	# print("\n[+] Mutation ")
	# print(offspring_mutation)

	print("\n========================\n")
	
	# Creating the new population based on the parents and offspring.
	# for p in ga.population:

	# 	np.array(p.permutation)
	# 	np.array(parents)
	# 	np.array(offspring_mutation)
	# 	p.permutation[0:len(parents)][:] = parents
	# 	p.permutation[len(parents):][:] = offspring_mutation

	# 	for i in range(len(parents)):
	# 		for j in range(len(p.permutation[0])):
	# 			p.permutation[i][j] = parents[i][j]

	# 	for i in range(len(parents), len(offspring_mutation)):
	# 		for j in range(len(p.permutation[0])):
	# 			p.permutation[i][j] = offspring_mutation[i][j]





# Getting the best solution after iterating finishing all generations.
# At first, the fitness is calculated for each solution in the final generation.
# Then return the index of that solution corresponding to the best fitness.
fitness = ga.fitness(ga.population)
best_match_idx = numpy.where(fitness == numpy.max(fitness))
print(f"[+] Best solution ===================== {ga.population[best_match_idx][:]}")
print(f"[+] Best solution fitness ============= {ga.population[best_match_idx][:].fitness()}")