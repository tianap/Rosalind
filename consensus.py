'''
Rosalind: Bioinformatics Stronghold
ID: CONS
Title: Consensus and Profile

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several possible 
consensus strings exist, then you may return any one of them.)
'''
from Bio import SeqIO
seq_array = []

for seq_record in SeqIO.parse('rosalind_cons.txt', 'fasta'):
	seq_array.append(seq_record.seq)

'''
Profile matrix:

   A  C  G  T
1
2
3
4
.
.
.
n
'''
profile = []
for i in range(len(seq_array[0])):
	A = 0
	C = 0
	G = 0
	T = 0
	for j in seq_array:
		if j[i] == 'A':
			A+=1
		elif j[i] == 'C':
			C+=1
		elif j[i] == 'G':
			G+=1
		elif j[i] == 'T':
			T+=1
	profile.append([A,C,G,T])

consensus = ''
for count in profile:
	base = count.index(max(count))
	if base == 0:
		consensus += 'A'
	elif base == 1:
		consensus += 'C'
	elif base == 2:
		consensus += 'G'
	else:
		consensus += 'T'

new=open('consensus_seq.txt','w')
new.write(consensus)
new.close()