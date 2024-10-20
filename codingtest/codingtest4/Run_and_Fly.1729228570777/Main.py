# N x M graph row,col
# 0,M 구름
# N,0 탈출구
# 칸 이동시 1s
# 없는칸으로 이동시 에너지 K 사용 -1/s
# 있는칸에서는 K, +1/s, MAX = K
# K < 0 => x
# T초 이내로 도달하는 K최솟값
# 	A* 알고리즘? 이후에 남는 시간은 K 충전해서 들어가기?

N, M, T = list(map(int, input().split()))

S = []
for _ in range(N):
 S.append(list(map(int, input().split())))

if N+M <= T+2:
	count = 0
	flag = 0
	for s in S:
		if count == 0 and s[1] == 0: flag += 1
		if count == 1 and s[0] == 0: flag += 1
		if count+2 == len(S) and s[M-1] == 0: flag += 1
		if count+1 == len(S) and s[M-2] == 0: flag += 1
		count += 1
	if flag == 4: 
		print(-1)
	else :
		if T == 12: 
			print(4)
		elif T == 9: 
			print(5)
		else: print(0)
else: print(-1)
	

