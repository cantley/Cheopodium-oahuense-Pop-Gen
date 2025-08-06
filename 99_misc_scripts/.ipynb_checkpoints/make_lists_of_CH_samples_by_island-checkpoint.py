import pandas as pd
# This script...
# imports the renaming file for all follow-on applications; and
# makes text files with strings of sample names from each island

# path of the rename file
names_in_file = "../00_data/Chenopodium DNA Extraction CH population - Martine 2017 - Renaming for R.csv"

#import the CSV
names = pd.read_csv(names_in_file)
islands = []                   # empty list of islands
for island in names['Island']: # cycle through the list
    if island not in islands:  # is it in the list? if not...
        islands.append(island) # makes a list of islands, with no duplicates
        filename = f"{island}_samples.txt" # makes empty text files for each island
        with open(f"../00_data/CH_pop_lists/{filename}", "w") as file_handle: 
            subset = names[names['Island']==island] # makes a subset from the specific island we're looking at
            sample_list = f'' # makes an empty string
            for sample in subset['Old Name']: # iterates over the samples in the island subset
                sample_list+=f'{sample},'     # adds samples as we go
            sample_list_trimmed=f'{sample_list[:-1]}'
            file_handle.write(sample_list_trimmed) # adds the carat, slices off the last comma, writes the list
            print(f'{sample_list_trimmed} written to {filename}.')