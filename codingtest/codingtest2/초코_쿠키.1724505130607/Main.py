# def cookie_order (n, taste_values):
# 	index_taste_values = [(taste_values[i], i+1) for i in range(n)]
	
# 	index_taste_values.sort(key=lambda x: (-x[0], x[1]))
	
# 	order = [index for _, index in index_taste_values]
	
# 	return order
	
# n = int(input())
# taste_values = list(map(int, input().split()))

# order = cookie_order(n,taste_values)

# print(' '.join(map(str, order)))

import sys
input = sys.stdin.readline

N = int(input().strip())
cookie = list(map(int, input().strip().split()))

result = sorted((value, idx + 1) for idx, value in enumerate(cookie))

# 곱을 최대화 해야하기 때문에 0예외 처리를 해줘야함.
for i, (value, idx) in enumerate(result):
    if value - i <= 0:
        print(' '.join(map(str, range(1, N + 1))))
        break
else:
    print(' '.join(map(str, [idx for value, idx in result])))