N, K = map(int, input().split())
stuff = [[0, 0]]
knapsack = [[0 for _ in range(K+1)] for _ in range(N+1)]
for _ in range(N):
    stuff.append(list(map(int, input().split())))

for i in range(0,N+1):
    for j in range(0,K+1):
        if j>=stuff[i][0]:
            knapsack[i][j]=max(stuff[i][1]+knapsack[i-1][j-stuff[i][0]],knapsack[i-1][j])
        else:
            knapsack[i][j]= knapsack[i-1][j]
            #비교하는 줄에서 가치보다 작은 값은 그 윗줄의 값 그대로 받아온다

print(knapsack[N][K])

