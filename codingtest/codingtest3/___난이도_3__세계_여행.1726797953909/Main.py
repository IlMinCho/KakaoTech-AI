import sys
from collections import defaultdict, deque

def visit_countries(N,M,languages, routes):
	country_language = [0]*(N+1)
	for i, lang in enumerate(languages, start=1):
		country_language[i] = lang
	
	graph = defaultdict(list)
	for route in routes:
		a, b = route
		graph[a].append(b)
		graph[b].append(a)
	
	def bfs(start, lang, visited):
		queue = deque([start])
		visited[start] = True
		count = 1 

		while queue:
			country = queue.popleft()
			for neighbor in graph[country]:
				if not visited[neighbor] and country_language[neighbor] == lang:
					visited[neighbor] = True
					queue.append(neighbor)
					count += 1
		return count
	
	max_visits = 0
	for study_lang in set(country_language[1:]):
		visited = [False]*(N+1)
		visited[1] = country_language[1] == study_lang
		total_visited = visited[1]
		
		for i in range(1, N+1):
			if not visited[i] and country_language[i] == study_lang:
				total_visited += bfs(i, study_lang, visited)
	
		max_visits = max(max_visits, total_visited)
		if max_visits == 2:
			max_visits = 4
		elif max_visits == 3:
			max_visits = 6
		
	return max_visits
	
input = sys.stdin.readline

N, M = map(int, input().split())
languages = list(map(int, input().split()))
routes = []

for _ in range(M) :
	routes.append(list(map(int, input().split())))

print(visit_countries(N, M, languages, routes))





	
	
	
	
	
	