a=input()
l=[]
s=''
for i in a:
    s=s+i
    if(len(s)==3):
        l.append(s)
        s=''
t='Protines : '
for i in l:
    if(i=='AUG'):
        t=t+"Methionine ,"
    elif(i=='UUU' or i=='UUC'):
        t=t+"Phenylalanine ,"
    elif(i=='UUA' or i=='UUG'):
        t=t+"Leucine ,"
    elif(i=='UCU' or i=='UCC' or i=='UCA' or i=='UCG'):
        t=t+"Serine ,"
    elif(i=='UAU' or i=='UAC'):
        t=t+"Tyrosine ,"
    elif(i=='UGU' or i=='UGC'):
        t=t+"Cysteine ,"
    elif(i=='UGG'):
        t=t+"Tryptophan ,"
    elif(i=='UAA' or i=='UAG' or i=='UGA'):
        break
    else:
        print("Invalid Codon", i)
        break
print(t.replace(t[-1],' '))
print(t)
    
        
        
        
