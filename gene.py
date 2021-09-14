import random

chemicals = ["A", "T","C","G"]

start = "ATG"

end = ["TAG","TAA","TGA"]



def make_codon():
    codon = ""
    for x in range(3):
        codon += chemicals[random.randint(0,len(chemicals)-1)]
    return codon
    

#print(codon)

#gene = [start]
#for x in range(random.randint(10,100)):
#    codon = make_codon()
#    while codon == start or codon in end:
#        codon = make_codon()
        #print("NG!!!")
#    if codon in end:
#        print("end")
#    gene.append(codon)

#print(gene)

class Gene:
    def __init__(self,na,nu):
        self.name = na
        self.codon_list = [start]
        for x in range(nu):
            codon = make_codon()
            while codon == start or codon in end:
                codon = make_codon()
        #print("NG!!!")
#    if codon in end:
#        print("end")
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

gene = Gene("ABC",100)

gene.codon_list[5] = "TTT"
gene.codon_list[6] = "AAA"

print(gene.codon_list)
#print(gene.Has_Codon("ATG"))
#print(gene.Has_Codon("CCC"))


#print(gene.Count_Codon("GGG"))
#print(gene.Count_Codon("GAA"))
print(gene.Has_Codon("TTT"))
print(gene.Has_Codon("AAA"))
print(gene.Has_Pattern(["TTT","AAA"]))
