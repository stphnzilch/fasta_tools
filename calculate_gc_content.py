#!/usr/bin/env python

# Command line script to calculate base frequency from a .fasta file

import sys

a_count = 0.00
c_count = 0.00
g_count = 0.00
t_count = 0.00

with open(sys.argv[1], 'r') as fasta:
    for line in fasta:
        if line.startswith(">"):
            # Header line, skip it
            continue
        a_count += line.count("A")
        c_count += line.count("C")
        g_count += line.count("G")
        t_count += line.count("T")

print("Base counts for file %s:" % sys.argv[1])
print("A: %d" % a_count)
print("C: %d" % c_count)
print("G: %d" % g_count)
print("T: %d" % t_count)

nucleotide_count = (a_count + g_count + c_count + t_count)
GC_percentage = ((g_count + c_count)/nucleotide_count ) * 100
A_percentage = (a_count/nucleotide_count) * 100
C_percentage = (c_count/nucleotide_count) * 100
G_percentage = (g_count/nucleotide_count) * 100
T_percentage = (t_count/nucleotide_count) * 100

print "\n___Percentages___"
print "GC: ",GC_percentage,"%" 
print "A: ",A_percentage, "%"
print "C ",C_percentage, "%"
print "G: ",G_percentage, "%"
print "T: ",T_percentage, "%"