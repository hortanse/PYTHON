#!/usr/local/bin/python
### Written by Yi-Fan Chou (chouoyi@pennmedicine.upenn.edu) on 04/19/2017
# This script two inputs files, the first one is original fam file (contains 1023 samples) and Add a comment to this line
# the second file is the sample list that you would like to run QC pipeline.

from __future__ import print_function
import pandas as pd
import sys

#make sure the user passed two arguments

if len(sys.argv) != 3:
    raise Exception("Usage: {0} <input files here>".format(sys.argv[1:]))

#read in input data
fam = pd.read_csv(sys.argv[1], sep="\t",header=None)
fam.fillna(0.0)

sample = pd.read_csv(sys.argv[2], sep="\t",header=None)

sample_set = set()
n = fam.shape[0]  #The number of rows in fam file
m = sample.shape[0] #The number of rwos in sample_id file

#Setting up sample id set
for mi in range(m):
    sample_set.add(sample.iat[mi, 0]) # add first column of sample df into sample_set

#Test the fam file to see if the sample id in fam file is also in sample_set

fout = open("modified_file.fam", "w")
for ni in range(n):
    if fam.iat[ni, 1] in sample_set: #2nd column of fam file
        lis = "\t".join([str(e) for e in fam.iloc[ni][:]])
        lis = lis + "\n"
        fout.write(lis)

fout.close()
