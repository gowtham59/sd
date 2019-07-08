n1=int(input())
n2=2**n1
list3=[]
for i in range(0,n2):
    l=bin(i)[2:].zfill(n1)
    if(len(l)<len(bin(2**n1-1)[2:])):
        list3.append([l.count("1"),l])
    else:
        list3.append([l.count("1"),l])
list3.sort()
for i in range(len(list3)):
    print(list3[i][1])
