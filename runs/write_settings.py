import os


BIN_PATH = '/Users/JGZHANG/Work/Densmore lab/Partition/genetic-circuit-partitioning/runs'
GRAPH_PREFIX = BIN_PATH + '/graph'

f_in = open(BIN_PATH + '/settings-1.txt', 'w') 
f_in.write('sample\tn\tk\tgraph_path\tlib_path\tin_nodes\tout_nodes\toutput_path\n')
sample = 1
for filename in os.listdir(GRAPH_PREFIX):
	n = filename.split('.')[0][-2:]
	k = filename.split('.')[1]
	graph_path = GRAPH_PREFIX
	lib_path = BIN_PATH + '/lib'
	in_nodes = "0,1,2"
	out_nodes = 3
	output_path = BIN_PATH + '/results'
	f_in.write('\t'.join([str(sample), n, k, graph_path, lib_path, in_nodes, str(out_nodes), output_path])+'\n')
	sample += 1