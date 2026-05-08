def createGraph(V, edges):
    adj = [[] for _ in range(V)]

    for it in edges:
        u = it[0]
        v = it[1]
        adj[u].append(v)

    return adj


if __name__ == "__main__":
    V = 7

    edges = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6]]

    adj = createGraph(V, edges)

    print("Adjacency List Representation:")
    for i in range(V):

        print(f"{i}:", end=" ")
        for j in adj[i]:

            print(j, end=" ")
        print()



from collections import defaultdict 
graph = defaultdict(list) 
graph["Node 0"].append("Node 1") 
graph["Node 0"].append("Node 2") 
graph["Node 0"].append("Node 3")
graph["Node 0"].append("Node 4")
graph["Node 0"].append("Node 5")
graph["Node 0"].append("Node 6")
graph["Node 1"]
graph["Node 2"]
graph["Node 3"]
graph["Node 4"]
graph["Node 5"]
graph["Node 6"]

print(dict(graph))