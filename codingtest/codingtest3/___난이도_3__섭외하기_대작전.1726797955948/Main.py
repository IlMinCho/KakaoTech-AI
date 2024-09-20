import sys

def vaild_combinations(N, S):
	S.sort()
	count = 0
	
	# for i in range(N-2):
	# 	for j in range(i+1, N-1):
	# 		for k in range(j+1, N):
	# 			if S[k] <= S[i] + S[j]:
	# 				count += 1
	# 			else:
	# 				break
	
	for k in range(N-1, 1, -1):
		i = 0
		j = k - 1
		while i < j:
				if S[k] <= S[i] + S[j]:
						count += (j - i)
						j -= 1
				else:
						i += 1
	return count

input = sys.stdin.readline

N = int(input())
S = list(map(int, input().split()))

print(vaild_combinations(N,S))

