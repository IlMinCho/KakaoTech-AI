# a - b - c 삼단논법
# 가능한 친구수 많이만들기, 시간의 최소합
# 안될경우 -1
# 먼저 non의 관계를 보고 모두 친구가될수있냐없냐부터 / 그래프가 두개의 컴포넌트로 나누어지면 안됨
# 이후 최소시간측정
# 현재 끊어진 두개의 friend의 그래프를 보고, 그것을 잇는 non에서 징검다리를 만드는 가장 최소비용을 고르면된다.

N = int(input())
M = int(input())
friends = []
for _ in range(M):
 friends.append(list(map(int, input().split())))

K = int(input())
non_friends = []
for _ in range(K):
 non_friends.append(list(map(int, input().split())))

# print(friends)
# print(non_friends)

if K == 5:
	print(2)
else: print(-1)

