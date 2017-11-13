#!/usr/bin/env python

import jinja2
import re

# This line tells the template loader where to search for template files
templateLoader = jinja2.FileSystemLoader( searchpath="./templates" )

# This creates your environment and loads a specific template
env = jinja2.Environment(loader=templateLoader)
template = env.get_template('week04_sol.html')

# Load the genes from a FASTA file
gene_count = 0
gene_out = 20

protein_list = []
protein = ''
protein_start = False

gene_list = list()
for line in open("e_coli_k12_dh10b.faa"):
    if protein_start:
        if line[0] != '>':
            protein += line
        else:
            protein_list.append(protein)
            protein = ''
            gene_count += 1
            protein_start = True
            gene_id = line[1:]
            gene_list.append(gene_id)
            continue
    if line[0] == '>':
        protein_start = True
        gene_id = line[1:]
        gene_list.append(gene_id)

gene_count += 1
protein_list.append(protein)

genes_table = list()
for i in range(gene_out):
    gene_length = len(protein_list[i])
    gene_id = gene_list[i].split("|")
    gene_id.append(gene_id[4])
    gene_id[4] = gene_length
    genes_table.append(gene_id)

print "Content-Type: text/html\n\n"
print template.render(genes = genes_table)

