Nanxi Liu, 10/27/24

1. To run the algorithm, simply run main.py
2. Intepreting the output: The output consists of the total value of the backpack and a list of packages in the form of tuples. Each tuple in the output is in the format of (package index, weight, value)
3. The genetic algorithm evolves the population twenty times then return the combination with the highest fitness
4. the package class in utils: each package is initliazed with an index, a weight, and a value
5. the genome class in utils: each genome object consists of a series of genes (packages).
6. how the fringe operation works: the fringe operation of the algorithm tries to replace one gene of the genome by randomly selecting a gene that is not already in the genome. It also makes sure that the total weight of the gene doesn't exceed 250 after replacement.
7. the population is initliazed with 8 genomes.
8. the gm_pairs variable in main.py consists of (fitness, genome) to make ranking the genomes easier.