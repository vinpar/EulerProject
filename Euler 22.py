
with open('E:\Vincent\Documents\Programming\Python\EulerProblems\p022_names.txt','r') as f:
    read_data = f.readline()
    f.closed
names= read_data.split('","',)
#remove odd " from first and last name
names[0]='MARY'
names[names.__len__()-1]='ALONSO'
names.sort()
print(names)
total=0
nameValue=[]
for n in range (0 ,names.__len__()):
    nameValue.append(0)
    for i in range (0,names[n].__len__()):
        nameValue[n]+=ord(names[n][i:i+1])-64
    total+=(n+1)*nameValue[n]
    print(names[n], n+1 ,nameValue[n],total)






