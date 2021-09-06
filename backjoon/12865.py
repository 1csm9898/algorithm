# def knapsack(i,k):
#
#
#
# k는 주어진 좌표
def frac(k,weight,size, number) :
    if k>number:
        return

def frac(n, size, value, k):
    if k <= 0:
        return 0
    reason = []
    for i in range(n):
        reason.append([value[i], size[i]])
    reasonable = sorted(reason, key=lambda x: x[1] / x[0])
    pro = []
    si = []
    for re in reasonable:
        pro.append(re[0])
        si.append(re[1])
    s,p=0,0
    for i in range(n):
        if s + si[i] <= k:
            p += pro[i]
            s += si[i]
        else:
            p += (k - s) * (pro[i] / si[i])
            break
    return p



number, weight = map(int, input().split())
li=[]
value=[]
x=[0]*number
mp=0
size=[]
for i in range(number):
    li.append(list(map(int, input().split())))
    value.append(li[i][1]/li[i][0])
    size.append(li[i][1])
print(li)
print(value)
print(size)