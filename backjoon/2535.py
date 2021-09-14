num=int(input())
li=[]
for i in range(num):
    li.append(list(map(int,input().split())))
for i in range(num):
    li.sort(key=lambda x:x[2],reverse=True)
cnt=[0]*100
c=0
for i in range(num):
    if cnt[li[i][0]-1]==2:
        li.append(li.pop(i))
    else:
        cnt[li[i][0]-1]+=1
        c+=1
    if sum==3:
        break
for i in li[:3]:
    print(*i[:2])
