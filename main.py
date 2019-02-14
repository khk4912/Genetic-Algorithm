import random
import time
class gene:
    def __init__(self):
        self.genes = []
        self.tg = "1111111"
        self.len_tg = len(self.tg)

    def create_gene(self):
        for _ in range(20):
            gene = ''.join(str(random.randint(0,9)) for _ in range(self.len_tg))
            self.genes.append(gene)

        return self.genes

    def check_gene(self, genes):
        temp = {}
        for gene in genes:
            temp[gene] = 0
            for i in range(self.len_tg):
                
                if gene[i] == self.tg[i]:
                    temp[gene] += 1

        print(temp, "\n\n")
        result = temp
        temp = dict()
        return result

    def match(self, parents):
        temp = []
        for key, value in parents.items():
            temp += [key] * value

        parents = random.sample(temp,4)
        print(parents,"\n\n")
        result = []
        for _ in range(20):
            if random.random() < 0.1:
                result.append(''.join(str(random.randint(0,9)) for _ in range(self.len_tg)))
            else:
                a,b = random.sample(parents,2)
                gyocha = random.randint(0,6)
                # result.append(''.join(random.choice(random.choice([a,b])) for _ in range(self.len_tg)) )
                result.append(''.join(a[0:gyocha] + b[gyocha:]))
        
        return result
        

gene = gene()

first = gene.create_gene()
count = 0
while True:
    print("###Gene%d###" %(count))
    a = gene.check_gene(first)
    b = gene.match(a)
    if gene.tg in b:
        print("###Finished! Final gene: %s" %(b))
        break
    first = b
    count+=1