'''
Rosalind: Bioinformatics Stronghold
ID: IPRB
Title: Mendel's First Law

Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: 
k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual 
possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
'''

f=open('rosalind_iprb.txt')
line = f.readline()
counts = list(map(float, line.split()))
pop = counts[0]+counts[1]+counts[2]

# Find the complement (all recessive possibilities)

rec_rec = (counts[2]/pop)*((counts[2]-1)/(pop-1))
het_het = (counts[1]/pop)*((counts[1]-1)/(pop-1))
rec_het = (counts[2]/pop)*(counts[1]/(pop-1)) + (counts[1]/pop)*(counts[2]/(pop-1))

print('{:.5f}'.format(1-(rec_rec+0.25*het_het+0.5*rec_het)))
