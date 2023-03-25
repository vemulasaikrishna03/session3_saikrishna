from collections import Counter
from textwrap import wrap
s="AUGUUUUCUUAAAUG"
l= wrap(s,3)
a=[]
for i in l:
    if i=="AUG" in l:
        a.append("Methionine")
    elif i=="UUU" or i=="UUC" in l:
        a.append("Phenylalanine")
    elif i=="UUA" or i=="UUG" in l:
        a.append("Leucine")
    elif i=="UCU" or i=="UCC" or i=="UCA" or i=="UCG" in l:
        a.append("Serine")
    elif i=="UAU" or i=="UAC" in l:
        a.append("Tyrosine")
    elif i=="UGU" or i=="UGC" in l:
        a.append("Cysteine")
    elif i=="UUG" in l:
        a.append("Tryptophan")
    elif i=="UAA" or i=="UAG" or i=="UGA" in l:
        pass
    else:
        pass
print(list(set(a)))
