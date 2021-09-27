import random

chemicals = ["A", "T","C","G"]

start = "ATG"

end = ["TAG","TAA","TGA"]



def make_codon():
    codon = ""
    for x in range(3):
        codon += chemicals[random.randint(0,len(chemicals)-1)]
    return codon
    

class Gene:
    def __init__(self,na,nu):
        self.name = na
        self.codon_list = [start]
        for x in range(nu):
            codon = make_codon()
            while codon == start or codon in end:
                codon = make_codon()
            self.codon_list.append(codon)
        self.codon_list.append(end[random.randint(0,len(end)-1)])
    def Has_Codon(self,co):
        if co in self.codon_list:
            return True
        else:
            return False
    def Count_Codon(self,co):
        count = 0
        for codon in self.codon_list:
            if codon == co:
                count += 1
        return count
    def Has_Pattern(self,pattern):
        if not pattern[0] in self.codon_list:
            return False
        else:
            for codon in self.codon_list:
                if codon == pattern[0] and self.codon_list.index(codon) + len(pattern) > len(self.codon_list):
                    return False
                elif codon == pattern[0]:
                    index = self.codon_list.index(codon)
                    for p in pattern:
                        if p != self.codon_list[index]:
                            return False
                        index += 1
                    return True
                else:
                    pass
    def CountPattern(self,pattern):
        if not pattern[0] in self.codon_list:
            return 0
        else:
            count = 0
            for codon in self.codon_list:
                if codon == pattern[0] and self.codon_list.index(codon) + len(pattern) > len(self.codon_list):
                    break
                elif codon == pattern[0]:
                    index = self.codon_list.index(codon)
                    test = []
                    for x in range(len(pattern)):
                        test.append(self.codon_list[index+x])
                    if test == pattern:
                        count +=1
                else:
                    pass
            return count

gene = Gene("ABC",50)

print(gene.codon_list)
print(gene.Has_Codon("TTT"))
print(gene.Count_Codon("TTT"))
print(gene.Has_Codon("AAA"))
print(gene.CountPattern(["TTT","AAA"]))

class DNA:
    def __init__(self, na, nu):
        self.name = na
        self.gene_list = []
        for x in range(nu):
            gene = Gene("A" + str(x), random.randint(100, 600))
            self.gene_list.append(gene)

flu = DNA("Influenza", 8)

fluATT = 0
for g in flu.gene_list:
    #print(g.codon_list)
    fluATT += g.Count_Codon("ATT")


covid = DNA("Covid-19", 9)

covidATT = 0
for g in covid.gene_list:
    #print(g.codon_list)
    covidATT += g.Count_Codon("ATT")

mers = DNA("MERS", 11)

mersATT = 0
for g in mers.gene_list:
    #print(g.codon_list)
    mersATT += g.Count_Codon("ATT")

print("flu " + str(fluATT))
print("covid " + str(covidATT))
print("mers " + str(mersATT))
