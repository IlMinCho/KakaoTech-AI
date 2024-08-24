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