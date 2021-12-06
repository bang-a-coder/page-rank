from collections import defaultdict
from typing import DefaultDict
import math


network = {
	"A": ["B"],
	"B": ["A", "C"],
	"C": ["A"]
}

def pageRank(incLinks, numerator):
	res = 0
	for inc_page in incLinks:
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

	k = 1
	for page in G.keys():
		iterations[k].update({page: pageRank(getLinks(page), iterations[k-1])})

	finalRanks = iterations
	return finalRanks


# print(getLinks("A"))
print(powerIteration(network))