def cookie_order (n, taste_values):
	index_taste_values = [(taste_values[i], i+1) for i in range(n)]
	
	index_taste_values.sort(key=lambda x: (-x[0], x[1]))
	
	order = [index for _, index in index_taste_values]
	
	return order
	
n = int(input())
taste_values = list(map(int, input().split()))

order = cookie_order(n,taste_values)

print(' '.join(map(str, order)))
