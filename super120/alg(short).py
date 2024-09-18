import heapq

road_graph = {
    'Arad': {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Pitesti': 97, 'Craiova': 146},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101}
}

heuristic_cost = {
    "Arad": {"Bucharest": 366},
    "Bucharest": {"Bucharest": 0},
    "Craiova": {"Bucharest": 160},
    "Dobreta": {"Bucharest": 242},
    "Eforie": {"Bucharest": 161},
    "Fagaras": {"Bucharest": 176},
    "Giurgiu": {"Bucharest": 77},
    "Hirsowa": {"Bucharest": 151},
    "Lasi": {"Bucharest": 226},
    "Lugoj": {"Bucharest": 244},
    "Mehadia": {"Bucharest": 241},
    "Neamt": {"Bucharest": 234},
    "Oradea": {"Bucharest": 380},
    "Pitesti": {"Bucharest": 100},
    "Rimnicu Vilcea": {"Bucharest": 193},
    "Sibiu": {"Bucharest": 253},
    "Timisoara": {"Bucharest": 329},
    "Urziceni": {"Bucharest": 80},
    "Vaslui": {"Bucharest": 199},
    "Zerind": {"Bucharest": 374}
}


def heuristic_cost_estimate(node, goal):
    return heuristic_cost[node][goal]


def a_star(graph, start, goal):
    open_set = [(0, start)]
    came_from = {}
    g_score = {city: float('inf') for city in graph}
    g_score[start] = 0

    while open_set:
        current_cost, current_city = heapq.heappop(open_set)

        if current_city == goal:
            path = reconstruct_path(came_from, goal)
            return path

        for neighbor, cost in graph[current_city].items():
            tentative_g_score = g_score[current_city] + cost

            if tentative_g_score < g_score.get(neighbor, float('inf')):
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic_cost_estimate(neighbor, goal)
                heapq.heappush(open_set, (f_score, neighbor))
                came_from[neighbor] = current_city

    return None


def reconstruct_path(came_from, current):
    total_path = [current]

    while current in came_from:
        current = came_from[current]
        total_path.insert(0, current)

    return total_path


def calculate_distance(graph, path):
    total_distance = 0

    for i in range(len(path) - 1):
        total_distance += graph[path[i]][path[i + 1]]

    return total_distance


sc = 'Arad'
gc = 'Bucharest'

path = a_star(road_graph, sc, gc)
if path:
    di = calculate_distance(road_graph, path)
    print("Shortest path from {} to {}: {}".format(sc, gc, path))
    print("The distance from Arad to Bucharest is", di)
else:
    print("No path found from {} to {}.".format(sc, gc))
