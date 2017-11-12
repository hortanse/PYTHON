#!/usr/bin/env python

import re

gene_count = 0
min_protein_length = 0
max_protein_length = 0
ave_protein_length = 0
gene_hyp = 0
pattern = 'hypothetical'

protein_list = []
protein = ''
protein_start = False

file_in = open('e_coli_k12_dh10b.faa', 'r')

for line in file_in:
    if protein_start:
        if line[0] != '>':
            protein += line
        else:
            protein_list.append(protein)
            protein = ''
            gene_count += 1
            protein_start = True
            if re.search(pattern, line):
                gene_hyp += 1
            continue
    if line[0] == '>':
        protein_start = True
        if re.search(pattern, line):
            gene_hyp += 1

gene_count += 1
protein_list.append(protein)

# Find the min, max, and averge protein lengths
min_protein_length = len(protein_list[1])
max_protein_length = len(protein_list[1])
list_count = len(protein_list)
print(list_count)
total_length = 0
for i in range(list_count):
    length = len(protein_list[i])
    if min_protein_length > length:
        min_protein_length = length
    if max_protein_length < length:
        max_protein_length = length
    total_length += length
    
ave_protein_length = total_length/gene_count

#output
print('gene count = ', gene_count)
print('min protein lenght = ', min_protein_length)
print('max protein length = ', max_protein_length)
print('averge protein length = ', ave_protein_length)
print('count of genes with hypothetical in the description = ', gene_hyp)


            
            
        