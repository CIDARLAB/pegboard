#!/usr/bin/env python
"""
Analyze circuit score and load within each partition after gate assignment 
"""

import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt
import os
from os import path

DATA_PREFIX = '../results/'
OUT_PREFIX  = './gate assignment analysis/'


def plot_circuit_score (n):
	""" plot circuit score trajectories in simulated annealing for a group of graphs with the same n"""
	fig = plt.figure(figsize=(5,3))
	ax  = fig.add_subplot(111)

	numfile = 0
	for dirname in os.listdir(DATA_PREFIX):
		if dirname.startswith('DAG'+str(n)):
			S = DATA_PREFIX + dirname + '/S_trajectory.txt'
			if path.exists(S):
				lines = [open(S, 'r').read().strip("\n")][0].split('\n')
				for line in lines:
					SList = [float(s) for s in line.split('\t')[1].split(',')]
					ax.plot(range(len(SList)), SList, linewidth=0.2, c='k')
				numfile += 1
	ax.set_ylabel('Cicuit Score')
	ax.set_xlabel('Time Steps')
	outfig = OUT_PREFIX + 'S trajectories_n=' + str(n) + '.pdf'
	plt.savefig(outfig, dpi=200)
	plt.show()
	print('total number of graph plotted', numfile)

def plot_part_load (n): 
	""" calculate the load """





if __name__ == '__main__':
	if path.isdir(OUT_PREFIX) == False:
		os.makedirs(OUT_PREFIX)

	# plot_circuit_score (30)