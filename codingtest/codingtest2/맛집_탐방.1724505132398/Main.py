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