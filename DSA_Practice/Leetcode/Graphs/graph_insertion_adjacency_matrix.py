def add_node(v):
    global node_count
    if v in nodes:
        print(v, "is already present in the graph")

    else:
        node_count += 1
        nodes.append(v)
        for n in graph:
            n.append(0)
        temp = []
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)

def add_edge_undirected_unweighted(v1, v2):
    if v1 not in nodes:
        print(v1, "not in graph")
    elif v2 not in nodes:
        print(v2, "not in graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = graph[index2][index1] = 1

def add_edge_undirected_weighted(v1, v2, cost):
    if v1 not in nodes:
        print(v1, "not in graph")
    elif v2 not in nodes:
        print(v2, "not in graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = graph[index2][index1] = cost

def add_edge_directed_unweighted(v1, v2):
    if v1 not in nodes:
        print(v1, "not in graph")
    elif v2 not in nodes:
        print(v2, "not in graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = 1


def add_edge_directed_weighted(v1, v2, cost):
    if v1 not in nodes:
        print(v1, "not in graph")
    elif v2 not in nodes:
        print(v2, "not in graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = cost


def del_node(v):
    

def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(format(graph[i][j], "<3"), end=" ")
        print()

nodes = []
graph = []
node_count = 0
# print("Before adding nodes")
# print(nodes)
# print(graph)
add_node("A")
# add_node("A")
add_node("B")
add_node("D")
# add_edge_undirected_unweighted("A", "B")
# add_edge_undirected_unweighted("A", "C")
# add_edge_undirected_unweighted("A", "D")
# add_edge_undirected_weighted("A", "B", 10)
# add_edge_undirected_weighted("A", "D", 5)
# add_edge_directed_unweighted("A", "B")
# add_edge_directed_unweighted("A", "D")
add_edge_directed_weighted("A", "B", 5)
add_edge_directed_weighted("A", "D", 10)
print("After adding nodes")
print("nodes:", nodes)
print(graph)
print_graph()
