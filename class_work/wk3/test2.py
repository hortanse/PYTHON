from Bio import SeqIO
handle = open("e_coli_k12_dh10b.faa")
records = list(SeqIO.parse(handle, "fasta"))
handle.close()
print ("Found %i records" % len(records))