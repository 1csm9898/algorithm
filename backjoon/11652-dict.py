num=int(input())
dic={}
for i in range(num):
    k=int(input())
    if k in dic:
        dic[k]+=1
    else:
        dic[k]=1
dic=sorted(dic.items(),key=lambda x:(-x[1],x[0]))
print(dic[0][0])