# File created by Arun Durvasula: https://gist.github.com/arundurvasula/30727385d4605fb26770
# Modified by Yassine Souilmi in May 2018




import gzip
import csv
import argparse
import sys

parser = argparse.ArgumentParser(description="script to convert an all sites vcf to sweepfinder format. FASTA description will be the sample name in the VCF header.Only does one chromosome/region at a time.")
parser.add_argument("-v", "--vcf", action="store", required=True, help="Input VCF file. Should be a multisample vcf, though it should theoretically work with a single sample.")
parser.add_argument("-o", "--out", action="store", required=True, help="Output filename")
parser.add_argument("-c", "--chromosome", action="store", required=True, help="Chromosome to output. Should be something in the first column of the vcf.")
parser.add_argument("-g", "--gzip", action="store_true", required=False, help="Set if the VCF is gzipped.")
parser.add_argument("-p", "--phased", action="store_true", required=False, help="Speficy if the genotypes are phased.")
args = parser.parse_args()

vcf_in = args.vcf
out_name = args.out
out_chr = args.chromosome

sample_names = []
sample_seqs = []

# Printing output information
print "Generating SFS"
print "**************"
print "From: ",vcf_in
print "For chrmosome: ",out_chr

if args.phased:
	sep = "|"
	print "The input VCF is phased"
else:
	sep =  "/"
	print "The input VCF is not phased"

print "Writing the output to: ",out_name
print "**************"

if args.gzip:
    opener = gzip.open
else:
    opener = open

sweep_out = open(out_name, 'w')
sweep_out.write("position\tx\tn\tfolded\n") # write header
folded = "1"

with opener(vcf_in, 'r') as tsvin:
    tsvin = csv.reader(tsvin, delimiter='\t')

    for row in tsvin:

        if any('##' in strings for strings in row):
            continue
        if any('#CHROM' in strings for strings in row):
            sample_names = row[9:]

        chrom,pos,id,ref,alt,qual,filter,info,format=row[0:9]
        haplotypes = row[9:]
        location = pos
    
    	if chrom == out_chr:
        	alt_list = alt.split(",")
        	x = 0
        	n = 0
        	for index,haplotype in enumerate(haplotypes):
            		if haplotype.split(sep)[0] != '.':
                		n = n + 1 # count up the non missing calls
            		if haplotype.split(sep)[0] != "1" and haplotype.split(sep)[0] != ".":
                		x = x + 1 # count reference alleles.
                
        	if x != 0 and x != n:    
           		sweep_out.write(location+"\t"+str(x)+"\t"+str(n)+"\t"+folded+"\n")
       	else:
             	continue

print "Done!"
print "**************"
