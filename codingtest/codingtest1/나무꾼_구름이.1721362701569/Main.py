# 요구사항
# N개의 나무가 원형으로 배열, 매 벌목과정단 1만큼자람
# 높이가 M이상일 경우 벌목가능,높이만큼 목재량이 늘어남
# L,R,S 3개의 방법으로 이동 Q 만큼 움직임

# 알고리즘 정리
# 기본적으로 시뮬레이션으로써 구현문제, N^2로는 풀리지 않기에 최적화필요

# Edge case
# 	어떤 나무도 캐지못하는경우
# 	M = 0인 경우

import sys
input = sys.stdin.readline

N,M,X = map(int, input.split())
trees = list(map(int, input.split()))
Q = int(input())
commands = list(map(str, input().split()))

cur_idx = X-1
ans = 0

def moving(cur_idx, command, N):
	if command == 'L':
		return (cur_idx - 1 + N) % N
	elif command == 'R':
		return (cur_idx + 1) % N
	else: return cur_idx

# L,R 명령어를 수행하고 나무의 높이를 1씩 증가시키는 코드를 작성하면될것같지만
# 나무의 범위가 100000이 될수도있기에 N^2되는 순간 10^12를 넘어 타임아웃이 생길수있다.
# 인덱스를 활용하여 높이를 다룬다면 몇번째 이동에따라 인덱스를 활용해 벌목량을 결정하여 간단하게 해결가능함
for i in range(Q):
	if trees[cur_idx] + i >= M:
		ans += trees[cur_idx] + i
		trees[cur_idx] -= (trees[cur_idx] + i) # 0으로 다시 줄이는것이 아닌 인덱스활용하여 진행
	cur_idx = moving(cur_idx, commands[i], N)

print(ans)

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