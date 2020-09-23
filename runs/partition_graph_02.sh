
#	Copyright (C) 2020 by
#	Jing Zhang <jgzhang@bu.edu>, Densmore Lab, Boston University
# 	All rights reserved.
#	OSI Non-Profit Open Software License ("Non-Profit OSL") 3.0 license.

# Partition given graphs/genetic circuits; assign biological gates from the gate library to maximize circuit score

#!/bin/bash -l

# Specify hard time limit for the job
#$ -l h_rt=72:00:00

# Send an email when the job finishes or if it's aborted 
#$ -m ea

# Request a 28 processor node with at least 512 GB of RAM
#$ -pe omp 28
#$ -l mem_per_core=8G


BIN_PATH=/home/jackson/code/pegbox/bin
export METIS_DLL=/usr/local/lib/libmetis.so
python $BIN_PATH/partition_gate_assignment.py -settings settings.txt -samples 216
#python $BIN_PATH/partition_gate_assignment.py -settings settings.txt -samples 2
#python $BIN_PATH/partition_gate_assignment.py -settings settings.txt -samples 3
#python $BIN_PATH/partition_gate_assignment.py -settings settings.txt -samples 4
