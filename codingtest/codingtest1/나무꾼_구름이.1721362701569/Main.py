# 1 ~ N 나무
	#원형의 형태
	 # M 이상이면 벌목 목재량 x의 나무높이  L R S  높이는 1씩추가됨
		# 총 Q회 반복함

		

# def moving(index, p, N):
# 	if p == 'L':
# 		if index == 0: return N-1
# 		return index-1
# 	elif p == 'R':
# 		if index == N-1: return 0
# 		return index+1
# 	else: return index
		
# N,M,x = map(int, input().split())
# H = list(map(int, input().split()))
# Q = int(input())
# D = list(map(str, input().split()))

# index = x-1
# ans = 0

# for i in range(Q):
# 	if H[index] >= M: 
# 		ans += H[index]
# 		H[index] = 0
# 	for j in range(len(H)):
# 		H[j] += 1
# 	index = moving(index, D[i], N)

# print(ans)



import sys
input = sys.stdin.readline

N, M, X = map(int, input().split())
trees = list(map(int, input().split()))
Q = int(input())
commands = list(map(str, input().split()))

cur_idx = X - 1
total = 0
for i in range(Q):
    if trees[cur_idx] + i >= M:
        total += (trees[cur_idx] + i)
        trees[cur_idx] -= (trees[cur_idx] + i)

    if commands[i] == 'L':
        cur_idx = (cur_idx - 1 + N) % N
    elif commands[i] == 'R':
        cur_idx = (cur_idx + 1) % N
print(total)