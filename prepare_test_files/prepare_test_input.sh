#!/bin/bash

write_input(){

vcf_link="https://data.cyverse.org/dav-anon/iplant/home/maulik88/test_data/chr${1}_cattle_impute_reheader.vcf.gz"
idx_link="https://data.cyverse.org/dav-anon/iplant/home/maulik88/test_data/chr${1}_cattle_impute_reheader.vcf.gz.tbi"
chrom="chrom${1}"

echo "${chrom}","${vcf_link}","${idx_link}"

}

echo chrom,vcf,vcf_idx


for z in {1..29}
do
	write_input "${z}"
done

