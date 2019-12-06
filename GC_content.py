'''
Rosalind: Bioinformatics Stronghold
ID: GC
Title: Computing GC Content

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string.
'''
from Bio import SeqIO

def round_nearest(x, a):
	return round(x/a)*a

seqs = [] # [seq_record.id, %GC content]

for seq_record in SeqIO.parse('rosalind_gc.txt', 'fasta'):
	print(seq_record.seq)
	g = str(seq_record.seq).count('G')
	c = str(seq_record.seq).count('C')
	gc_total = ((g+c)/len(seq_record.seq))*100
	seqs.append([seq_record.id, '{:.6f}'.format(gc_total)])
			
seqs.sort(key=lambda x:x[1],reverse=True)

new=open('GC.txt','w')
new.write(seqs[0][0])
new.write('\n')
new.write(seqs[0][1])
new.close()
