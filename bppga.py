
from bin import pack
import random
import numpy.random as npr
import numpy as np



class chromosome():

	def __init__(self, objects, capacity):
		self.objects = objects
		self.capacity = capacity
		bins = pack(self.objects, self.capacity) # solve bin packing using first fit algorithm
		self.permutation = [bin.items for bin in bins] # creating chromosome from bins
		self.permutation = random.sample(self.permutation, len(self.permutation))


	def fitness(self):
		return sum([sum(w) for w in self.permutation])+self.capacity-1/self.capacity



class ga():

	def __init__(self, population):
		self.population = population


	def crossover(self, parents, offspring_size):
		offspring = [[0] * offspring_size[1] for i in range(offspring_size[0])] # rows and cols of child
		# crossover takes palce between two parents
		crossover_point = np.uint8(offspring_size[1]/2)
		for k in range(offspring_size[0]):
			# Index of the first parent to mate.
			parent1_idx = k%len(parents)
			# Index of the second parent to mate.
			parent2_idx = (k+1)%len(parents)
			# The new offspring will have its first half of its genes taken from the first parent.
			offspring[k][0:crossover_point] = parents[parent1_idx][0:crossover_point]
			# The new offspring will have its second half of its genes taken from the second parent.
			offspring[k][crossover_point:] = parents[parent2_idx][crossover_point:]
		
		return offspring



	def mutate(self, offspring_crossover, objects, capacity, num_mutations=1):
		mutations_counter = np.uint8(len(offspring_crossover[0]) / num_mutations)
		# Mutation changes a number of genes as defined by the num_mutations argument. The changes are random.
		for idx in range(len(offspring_crossover)):
			gene_idx = mutations_counter - 1
			for mutation_num in range(num_mutations):
				# The random value to be added to the gene.
				random_value = np.random.uniform(float(min(objects)), float(capacity-1), 1)
				offspring_crossover[idx][gene_idx] = offspring_crossover[idx][gene_idx] + random_value
				gene_idx = gene_idx + mutations_counter
		return offspring_crossover


	def wheel_roulette_selection(self, num_parents):
		# parents = np.empty((2, len(self.population[0].permutation)))
		max = sum([c.fitness() for c in self.population])
		selection_probs = [c.fitness()/max for c in self.population]
		parents = []
		for n_p in range(num_parents):
			parents.append(self.population[npr.choice(len(self.population), p=selection_probs)].permutation)
		return parents

	def fitness(self, population):
		return [c.fitness() for c in self.population]