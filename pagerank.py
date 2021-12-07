from collections import defaultdict
from typing import DefaultDict
import math


network = {
	"A": ["B"],
	"B": ["A"],
	"C": ["A"],
	"D": ["C"]
}


def pageRank_init(page, numerator, alpha, G):
	res = 0
	for inc_page in getLinks(page):
		res += numerator[inc_page]/len(network[inc_page])

	return alpha/len(G) + (1-alpha) * res


def getLinks(page):
	links = []

	for key in network.keys():
		if page in network[key]: links.append(key)

	return links


def powerIteration_init(G):

	iterations = defaultdict(dict)
 
	for page in G:
		iterations[0].update({page: 1/len(G.items())})

	def controller(const,k):
		tot = 0
		for page in G.keys():

			tot += abs(iterations[k][page] - iterations[k-1][page])
		
		if tot > const: 
			return True
		
	k = 0

	def iterator(k):
		k += 1
		for page in G.keys():
				iterations[k].update({page: pageRank_init(page, iterations[k-1], 0.15, G)})

		if controller(0.01,k) == True: return iterator(k)
		return
	
	iterator(k)
	
	finalRanks = iterations[max(iterations.keys())]
	return finalRanks


# print(getLinks("A"))

def fullPageRank(i, alpha, G, ranks):

	sigma = 0
	for inc_link in getLinks(i):
		sigma += ranks[inc_link] / len(G[inc_link]) 
	
	return alpha/len(G) + (1-alpha) * sigma	



init_ranks = powerIteration_init(network)

print(fullPageRank("A", 0.15, network, init_ranks))
print(fullPageRank("B", 0.15, network, init_ranks))
print(fullPageRank("C", 0.15, network, init_ranks))
print(fullPageRank("D", 0.15, network, init_ranks))
