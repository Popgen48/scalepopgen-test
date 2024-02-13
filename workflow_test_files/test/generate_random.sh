#!/bin/bash


for i in {1..10000}
	do
		seed=$(($RANDOM*3+$RANDOM))
		echo $seed
		if [[ "$seed" -gt 29953 && "$seed" -lt 300000 ]]
		then
		    echo "${seed}" >> random_number.txt
		fi
	done
sort -n random_number.txt|uniq > random_number_unique.txt
awk 'NR==FNR{a[$1];next}{if(FNR in a){print $1,$2}}' random_number_unique.txt $2 > $3
