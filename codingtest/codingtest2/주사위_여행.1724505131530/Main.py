MOD = 10**9 + 7

def count_paths (N, M, K, rests):
	dp = [[0]*(M+1) for _ in range(N+1)]
	dp[1][1] = 1
	
	rest_positions = set((r,c) for r,c in rests)
	
	for i in range (1, N+1):
		for j in range(1, M+1):
			if (i,j) == (1,1):
				continue
			if (i,j) in rest_positions:
				dp[i][j] = 0
			else:
				if i > 1:
					dp[i][j] += dp[i-1][j]
				if j > 1:
					dp[i][j] += dp[i][j-1]
				dp[i][j] %= MOD

	return dp[N][M]

def main():
	N, M, K = map(int, input().split())
	
	rests = []
	for _ in range(K):
		r, c = map(int, input().split())
		rests.append((r,c))
		
	result = count_paths(N,M,K, rests)
	
	print(result)

if __name__ == "__main__":
		main()
	