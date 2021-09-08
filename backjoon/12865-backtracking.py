def knap(i,t) :
    global mp
    if t<=0 or i>=N:
        return
    v=0
    for j in range(0,i):
        if x[j]==1:
            v+=stuff[j][1]
    #해당 차례 포함 할때
    if stuff[i][0]<=t:
        #frac돌려서 가능성있으면 내려가고=>다음 차례, 남은 크기
        if v+stuff[i][1]+frac(i+1,t-stuff[i][0])>=mp:
            x[i]=1
            mp=max(v+stuff[i][1],mp)
            knap(i+1,t-stuff[i][0])
    #해당 차례 포함하지않을때
    x[i]=0
    knap(i+1,t)

def frac(a,b):
    reason=[]
    for i in stuff[a:]:
        reason.append(i)
    reason = sorted(reason, key=lambda x: x[1] / x[0])
    size=[]
    val=[]
    result=0
    for i in reason:
        size.append(i[0])
        val.append(i[1])
    for i in range(len(reason)):
        if val[i]<b:
            b-=val[i]
            result+=reason[i][1]/reason[i][0]
        elif val[i]==b:
            result+=reason[i][1]/reason[i][0]
            break
        else :
            result+=(reason[i][1]/reason[i][0])*b
    return result

N, K = map(int, input().split()) #N은 갯수, K는 가방이 버틸 수 있는 크기
stuff = [] #stuff의 0은 크기, 1은 가치
for i in range(N):
    stuff.append(list(map(int, input().split())))
mp=0
x=[0]*N
knap(0,K) #노드번호, 가방의 남은 크기
print(mp)