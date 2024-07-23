# N, M의 행렬로 격자모양에 K개 판다가 있다
# 목적은 판다로부터 가장 불만족도가 낮은 칸에 들어가는 것이다.
# 불만족도는 모든 판다와의 거리를 모두 합한 값이다. (멘하튼거리)

# 격자에서 그래프탐색으로 판단할수도 있지만 모든 판다에대한 정확한 점수를 구해야하기에 완전탐색문제임.

# Edge case
#     모든 칸에 판다가 있고. 단한칸만 들어갈수있음
#     100x100 크기의 공간에 판다가 한마리만 있음

# 굳이 격자를 선언할 필요는없고, 판다들의 위치를 모두 저장한 변수를 선언하면됨
# 완전 탐색으로 모든위치에 대하여 판다가 없다면 현재 좌표에대한 모든 판다의 거리를 구한후 불만족도 계산
# 만약 범위가 100x100을 넘는 구조였다면, 다른알고리즘이나, 이분탐색을 통해 최적화필요함

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
list_K = list()
# panda_set = set()

matrix = [[0 for _ in range(M+1)] for _ in range(N+1)]
for _ in range(K):
    x, y = map(int, input().split())
    list_K.append([x, y])
	# panda_set.add((x, y))

total = 10e9
# total = float('inf')

for i in range(1, N+1):
    for j in range(1, M+1):
        temp_score = 0
        if [i, j] not in list_K:
            for panda in list_K:
                temp_score += ((i - panda[0])**2 + (j - panda[1])**2)
            total = min(total, temp_score)

print(total)

# N,M,K = map(int, input().split())
# pandas = []
# for _ in range(K):
# 	pandas.append(list(map(int, input().split())))

# def cal_non_sat(r,c,panda):
# 	return (((r-panda[0])*(r-panda[0])) + ((c-panda[1])*(c-panda[1])))
	
# def far_distance(N,M,onepandas):
# 	cal_matrix = []
# 	for i in range(1,N+1):
# 		for j in range(1,M+1):
# 			cal_matrix.append(cal_non_sat(i,j,onepandas))
# 	return cal_matrix

# ans = []
# for q in range(N*M):
# 	ans.append(0)

# for k in range(len(pandas)):
# 	list_ans = far_distance(N,M,pandas[k])
	
# 	for index in range(len(list_ans)):
# 		ans[index] += list_ans[index]

# print(min(ans))