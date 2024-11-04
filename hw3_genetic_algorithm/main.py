from utils.package import package 
from utils.genome import genome
import random
from operator import itemgetter


class selection():
    # all_packages are a list of tuples in the form of (weight, value)
    def __init__(self, all_packages) -> None:
        self.genes = [package(p[0], p[1], p[2]) for p in all_packages]
        self.gm_pairs = self.get_genomes()

    
    # generate all the genomes. Each genome is a tuple consisting of the fitness of the genome and the genome itself. eg (fitness, genome)
    def get_genomes(self):
        pop = []
        # randomly select some genomes as the initial population. Initial population is 8
        for _ in range(8):
            temp = []
            temp_weight = 0 
            # keep adding genes to the genome till the genome's weight approaches 250
            for gene in self.genes:
                if random.choices([True, False],weights = (50,50), k = 1)[0] and temp_weight < 250:
                    temp_weight += gene.get_weight()
                    if temp_weight <= 250:
                        temp.append(gene)
                elif temp_weight >= 250:
                    break
            new = genome(temp)
            pop.append((new.fitness(),new))
        # print(pop)
        return pop
    
    # cull the population by 50%
    def cull(self):
        # cutting by 50%
        # print(self.print_all_genomes())
        length = len(self.gm_pairs)
        # print('length before culling:',length)
        self.gm_pairs = sorted(self.gm_pairs,key=lambda x: x[0], reverse=True)[:length//2]
        temp_len = len(self.gm_pairs)
        # print('length after culling',temp_len)
        # generate an offspring for each remaining genome
        for i in range(0,temp_len):
            # check if genetic mutation is needed
            g = self.gm_pairs[i]
            genes = [package(p.get_package()[0],p.get_package()[1],p.get_package()[2]) for p in g[1].get_gen_seq()]
            child = genome(genes)
            if random.choices([True, False],weights = (20,80), k = 1)[0]:
                # attempts a mutation
                child.mutate(self.genes)
            self.gm_pairs.append((child.fitness(), child))

    # returns the most fit genome
    def get_most_fit(self):
        # keep culling till 20 tries is done
        tries = 20
        while tries > 0:
            # print('culling in progress')
            self.cull()
            tries -= 1
        max_gn = max(self.gm_pairs, key = itemgetter(0))
        # print(self.print_all_genomes())
        return 'value: '+str(max_gn[0]) + '. packages: '+str(max_gn[1].get_genome())
    # prints out the current population
    def print_all_genomes(self):
        result = ''
        for g in self.gm_pairs:
            result += str(g[0]) + ' '+str(g[1].get_genome()) + '\n'
        return result

def main():
    all_packages = [(1, 20, 6),(2, 30,5),(3,60,8),(4,90,7),(5,50,6),(6,70,9),(7,30,4),(8,30,5),(9,70,4),(10,20,9),(11,20,2),(12,60,1)]
    sel = selection(all_packages)
    return sel.get_most_fit()


if __name__ == '__main__':
    print(main())




''' references
1. https://sparkbyexamples.com/python/sort-list-of-tuples-in-python/#:~:text=You%20can%20sort%20a%20list%20of%20tuples%20in%20descending%20order,by%20using%20the%20key%20parameter.
2. https://www.geeksforgeeks.org/python-get-first-element-with-maximum-value-in-list-of-tuples/
'''
