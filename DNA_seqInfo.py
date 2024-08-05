
Nucleotides = ["A","C","G","T"]
DNA_RComp = {"A":"T" ,"C":"G","G": "C","T": "A"}
 
def seq_check(dna_Seq):
    dna_Seq = dna_Seq.upper()
    for nt in dna_Seq:
        if nt not in Nucleotides:
            return False
    return dna_Seq



def countNucFreq(seq):
    freqSeq=  {"A": 0, "C": 0, "G" :0 , "T" : 0}
    for nt in seq:
        freqSeq[nt] +=1
    return freqSeq

def transcription(seq):
   return seq.replace ("T", "U")   

def complement(seq):
   return ''.join([DNA_RComp[nt] for nt in seq])

def reverseComplement(seq):
   return ''.join([DNA_RComp[nt] for nt in seq]) [::-1]

def GC_content(seq):
   return round((seq.count('C')+ seq.count('G'))/ len(seq)*100)