#!/bin/bash

SCRIPT="/usr/nfs/923643692/cheno_popgen/vcf2phylip/vcf2phylip-2.8/vcf2phylip.py"

#paths
miss60_full="/usr/nfs/923643692/cheno_popgen/filtering/tetraploid/final_outputs/chenopodium_20250304b-tetraploid.indivmiss60.locimiss50.thin10.maf0.01.LD0.8-1000.vcf.gz"
miss60_OAM="/usr/nfs/923643692/cheno_popgen/subsets/chenopodium_20250304b-tetraploid.indivmiss60.locimiss50.thin10.maf0.01.LD0.8-1000.no-CH-AR.vcf.gz"

#list of files to process
FILES=($miss60_full $miss60_OAM)

for FILE in "${FILES[@]}"; do
	PREFIX=$(basename "$FILE" ".vcf.gz")
	python $SCRIPT -n   \
		-i $FILE \
		-o ../$PREFIX
done