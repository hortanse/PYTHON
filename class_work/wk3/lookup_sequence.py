#!/usr/bin/env python

import re

gene = raw_input('Please enter an accession = ')
g1, g2 = gene.split('.')
pattern = g1 + '[.]' + g2

protein = ''
protein_start = False

file_in = open('e_coli_k12_dh10b.faa', 'r')
for line in file_in:
    if protein_start:
        if line[0] == '>':
            break
        else:
            protein += line
    if line[0] == '>':
        match = re.search(pattern, line)
        if match:
            gene_out = line
            protein_start = True
#output
print(gene_out)
print(protein)			