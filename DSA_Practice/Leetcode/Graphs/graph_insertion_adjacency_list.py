def add_node(v):
    if v in graph:
        print("v is already present in the graph")
    else:
        graph[v] = []

def add_edge_undirected_unweighted(v1, v2):
    if v1 not in graph:
        print(v1, "not in graph")
    elif v2 not in graph:
        print(v2, "not in graph") 
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)

def add_edge_undirected_weighted(v1, v2, cost):
    if v1 not in graph:
        print(v1, "not in graph")
    elif v2 not in graph:
        print(v2, "not in graph") 
    else:
        v1_cost = [v1, cost]
        v2_cost = [v2, cost]
        graph[v1].append(v2_cost)
        graph[v2].append(v1_cost)

def add_edge_directed_weighted(v1, v2, cost):
    if v1 not in graph:
        print(v1, "not in graph")
    elif v2 not in graph:
        print(v2, "not in graph") 
    else:
        v1_cost = [v2, cost]
        # v2_cost = [v2, cost]
        graph[v1].append(v1_cost)
        # graph[v2].append(v1_cost)

def add_edge_directed_unweighted(v1, v2):
    if v1 not in graph:
        print(v1, "not in graph")
    elif v2 not in graph:
        print(v2, "not in graph") 
    else:
        graph[v1].append(v2)

graph = {}
add_node("A")
# add_node("A")
add_node("B")
add_node("C")
# add_edge_undirected_unweighted("A", "B")
# add_edge_undirected_weighted("A", "B", 10)
# add_edge_undirected_weighted("A", "C", 5)
# add_edge_directed_weighted("A", "B", 10)
# add_edge_directed_weighted("A", "C", 5)
add_edge_directed_unweighted("A", "B")
add_edge_directed_unweighted("A", "C")
print(graph)
