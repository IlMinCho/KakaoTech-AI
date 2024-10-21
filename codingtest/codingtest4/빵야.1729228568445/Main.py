# N, 1 ~ N enemy
# i -> Hi 
#.   g
# 1 ~ ...... N 
# ((i-1)mod 4) + 1 <= 0

# 0 mod 4 = 0, 1
# 1 mod 4 = 1, 1 = 2
# 2 mod 4 = 2 + 1 = 3 
# 3 mod 4 = 3 + 1 4  
# 4 mod 4 = 0 +1, 3
# 5 mod 4 = 1+1, 1
# 6mod 4

N = int(input())
H = list(map(int, input().split()))

shot = 0
h = 0

for i in H:
	while i > 0:
		if shot >= 4:
			h = (shot%4) + 1 
		else:
			if shot == 0: 
				h = 1
			elif shot == 1: 
				h = 2
			elif shot == 2: 
				h = 3
			elif shot == 3:
				h = 4
			
		i -= h
		shot += 1

print(shot)

