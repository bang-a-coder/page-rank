from collections import defaultdict
from typing import DefaultDict
import math


network = {
	"A": ["B"],
	"B": ["A", "C"],
	"C": ["A"]
}


def pageRank(page, numerator):
	res = 0
	for inc_page in getLinks(page):
		res += numerator[inc_page]/len(network[inc_page])

	return res


def getLinks(page):
	links = []

	for key in network.keys():
		if page in network[key]: links.append(key)

	return links


def powerIteration(G):

	iterations = defaultdict(dict)

	for page in G:
		iterations[0].update({page: 1/len(G.items())})

	def controller(const,k):
		tot = 0
		for page in G.keys():

			tot += abs(iterations[k][page] - iterations[k-1][page])
		
		if tot > const: 
			print(tot)
			return True
		
	k = 0

	def iterator(k):
		k += 1
		for page in G.keys():
				iterations[k].update({page: pageRank(page, iterations[k-1])})

		if controller(0.01,k) == True: return iterator(k)
		return
	
	iterator(k)
	
	finalRanks = iterations
	return finalRanks


# print(getLinks("A"))
print(powerIteration(network))
