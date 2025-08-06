import pandas as pd

# path of the rename file, which contains lists of samples and their islands of origin
names_in_file = "../00_data/Chenopodium DNA Extraction CH population - Martine 2017 - Renaming for R.csv"

#import the CSV
names = pd.read_csv(names_in_file)

# This section of the script...
# imports the renaming file for all follow-on applications; and
# makes text files with strings of CH sample names from each island

islands = []                   # empty list of islands
for island in names['Island']: # cycle through the list
    if island not in islands:  # is it in the list? if not...
        islands.append(island) # makes a list of islands, with no duplicates
        filename = f"{island}_samples.txt"
        # makes empty text files for each island
        with open(f"../00_data/CH_pop_lists/{filename}", "w") as file_handle: 
            subset = names[names['Island']==island] # makes a subset from the specific island we're looking at
            sample_list = f'' # makes an empty string
            for sample in subset['Old Name']: # iterates over the samples in the island subset
                sample_list+=f'{sample},'     # adds samples as we go
            sample_list_trimmed=f'{sample_list[:-1]}'
            file_handle.write(sample_list_trimmed) # adds the carat, slices off the last comma, writes the list
            print(f'Written to {filename}: {sample_list_trimmed}')


# this portion of the script is for building EXCLUSIVE strings; e.g., all herbarium samples not from Oahu.
# this is for subsetting using the exclusive feature of VCFtools, 
#    which excludes samples based on a string list.
#    so if we give it a string of samples not from (e.g.) Oahu,
#    we will retain only Oahu samples.

for is_island in islands:
    not_islands = []
    for not_island in islands: 
        if not_island is not is_island:
            not_islands.append(not_island)
    not_island_str=''                  #this is the empty string we'll be building in the format CO-CH-XX,CO-CH-XY,CO-CH-XZ
    for not_island in not_islands:
        with open(f"../00_data/CH_pop_lists/{not_island}_samples.txt", "r") as not_island_file:
            not_island_str+=f'{not_island_file.read()},'
    filename = f'{is_island}-exclusive_samples.txt'
    not_island_str_trimmed = not_island_str[:-1]
    with open(f"../00_data/CH_pop_lists/{filename}", "w") as except_is_island_file:
        print(f'Written to {filename}: {not_island_str_trimmed}')
        except_is_island_file.write(not_island_str_trimmed)