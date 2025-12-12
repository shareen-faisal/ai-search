from flask import Flask, render_template, request, jsonify
import heapq

app = Flask(__name__)

# 1. GRAPH DATA (Romania Map)
graph = {
    'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
    'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Drobeta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
    'Giurgiu': [('Bucharest', 90)],
    'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
    'Iasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Iasi', 87)]
}

# 2. ALGORITHMS
def bfs(start, goal):
    queue = [[start]]
    visited = set()
    steps = 0
    while queue:
        path = queue.pop(0)
        node = path[-1]
        steps += 1
        if node == goal: return path, calculate_cost(path), steps
        if node not in visited:
            visited.add(node)
            for neighbor, _ in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    return [], 0, steps

def dfs(start, goal):
    stack = [[start]]
    visited = set()
    steps = 0
    while stack:
        path = stack.pop()
        node = path[-1]
        steps += 1
        if node == goal: return path, calculate_cost(path), steps
        if node not in visited:
            visited.add(node)
            for neighbor, _ in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)
    return [], 0, steps

def ucs(start, goal):
    pq = [(0, [start])]
    visited = set()
    steps = 0
    while pq:
        cost, path = heapq.heappop(pq)
        node = path[-1]
        steps += 1
        if node == goal: return path, cost, steps
        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(pq, (cost + weight, path + [neighbor]))
    return [], 0, steps

def calculate_cost(path):
    total = 0
    for i in range(len(path) - 1):
        for neighbor, weight in graph[path[i]]:
            if neighbor == path[i+1]:
                total += weight
                break
    return total

# 3. ROUTES (Connecting to Frontend)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    data = request.json
    start, goal, algo = data['start'], data['goal'], data['algo']
    
    if algo == 'BFS': path, cost, steps = bfs(start, goal)
    elif algo == 'DFS': path, cost, steps = dfs(start, goal)
    else: path, cost, steps = ucs(start, goal)
    
    return jsonify({'path': path, 'cost': cost, 'steps': steps})

if __name__ == '__main__':
    app.run(debug=True)