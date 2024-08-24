# MOD = 10**9 + 7

# def count_paths (N, M, K, rests):
# 	dp = [[0]*(M+1) for _ in range(N+1)]
# 	dp[1][1] = 1
	
# 	rest_positions = set((r,c) for r,c in rests)
	
# 	for i in range (1, N+1):
# 		for j in range(1, M+1):
# 			if (i,j) == (1,1):
# 				continue
# 			if (i,j) in rest_positions:
# 				dp[i][j] = 0
# 			else:
# 				if i > 1:
# 					dp[i][j] += dp[i-1][j]
# 				if j > 1:
# 					dp[i][j] += dp[i][j-1]
# 				dp[i][j] %= MOD

# 	return dp[N][M]

# def main():
# 	N, M, K = map(int, input().split())
	
# 	rests = []
# 	for _ in range(K):
# 		r, c = map(int, input().split())
# 		rests.append((r,c))
		
# 	result = count_paths(N,M,K, rests)
	
# 	print(result)

# if __name__ == "__main__":
# 		main()
	
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

dp = [[0 for _ in range(max(N, M)+1)] for _ in range(max(N, M)+1)]

for _ in range(K):
    x, y = map(int, input().split())
    dp[x-1][y-1] = -1
# 출발 지점
dp[0][0] = 1


#경우의 수 찾기
MOD = int(1e9 + 7)
for i in range(N):
    for j in range(M):
        if dp[i][j] == -1:
            continue
        for k in range(1, 7, 1):
            if i - k >= 0 and dp[i-k][j] != -1:
                dp[i][j] = (dp[i][j] + dp[i - k][j]) % MOD
            if j - k >= 0 and dp[i][j-k] != -1:
                dp[i][j] = (dp[i][j] + dp[i][j - k]) % MOD


print(dp[N-1][M-1])