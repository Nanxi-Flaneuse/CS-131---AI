# a genome can be of any length as long as the total weight of the genes don't exceed 250 and there are no duplicate genes
import random

class genome():

    # packages is a list of objects of the class package
    def __init__(self, packages) -> None:
        self.gen_sequence = packages
        self.fit = self.fitness()
        self.weight = self.get_total_weight()

    def fitness(self):
        # return total value
        fit = 0
        for p in self.gen_sequence:
            fit += p.get_value()
        return fit
    
    # calculates the total weight of the genome
    def get_total_weight(self):
        weights = 0
        for p in self.gen_sequence:
            weights += p.get_weight()
        return weights
    
    # Fringe operation: single point mutation of a genome. Given an index and a new package, replace the package at the index in self.gen_sequence with the new package. Leaves self.gen_sequence unchanged if new package makes the genome heavier than 250.
    def mutate(self, packages): #ind, new_package):
        
        # # check if the total weight will still be <= 250 after replacement
        # if self.weight - self.gen_sequence[ind].get_weight() + new_package.get_weight() <= 250:
        #     # check if the package already exists in the sequence
        #     repetition = False
        #     for p in self.gen_sequence:
        #         if p.get_index() == new_package.get_index():
        #             repetition = True
        #     if not repetition:
        #         self.gen_sequence[ind] = new_package
        #         return True
        #     return False
        # else:
        #     print('can not add new package due to its heavy weight')
        #     return False

        # get a list of the id of genes in the genome
        id_list = [p.get_index() for p in self.gen_sequence]
        possible_gene_mutations = []

        # pick out genes that are not already in the genome
        for p in packages:
            if p.get_index() not in id_list:
                possible_gene_mutations.append(p)

        # randomly pick a gene in the genome to replace
        replacement_index = random.randint(0,len(self.gen_sequence)-1)
        # keeps performing the mutation action till a mutation succeeds or runs out of tries
        while len(possible_gene_mutations) > 0:
            # randomly picks a replacement gene from possible_gene_mutations
            new_gene_index = random.randint(0,len(possible_gene_mutations)-1)
            new_package = possible_gene_mutations[new_gene_index]
            del possible_gene_mutations[new_gene_index]
            if self.weight - self.gen_sequence[replacement_index].get_weight() + new_package.get_weight() <= 250:
                self.gen_sequence[replacement_index] = new_package
                break
        

    def get_gen_seq(self):
        # print(type(self.gen_sequence))
        return self.gen_sequence

    def get_genome(self):
        return [p.get_package() for p in self.gen_sequence]
    
    # return a list of the id of genes in the genome
    def get_id(self):
        return []


    