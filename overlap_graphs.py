'''
Rosalind: Bioinformatics Stronghold
ID: GRPH
Title: Overlap Graphs

Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.

Return: The adjacency list corresponding to O_3. You may return edges in any order.
'''
from Bio import SeqIO

edges = []
k = 3
seqs = {}

'''
seqs format:
{sequence ID: [full sequence, first k bases, last k bases]}
'''

for seq_record in SeqIO.parse('rosalind_grph.txt', 'fasta'):
	sequence = str(seq_record.seq)
	seqs.update({seq_record.id:[sequence, sequence[0:k], sequence[len(sequence)-k:len(sequence)]]})
for key in seqs.keys():
	for other_key in seqs.keys():
		if other_key != key: #only compare to other keys
			if seqs[key][2] == seqs[other_key][1]:
				edges.append([key, other_key]) # saves the edges to a list

new=open('seq_graphs.txt', 'w')
for edge in edges: # write edges to new file
	new.write(edge[0]+" "+edge[1])
	new.write('\n')
new.close()


