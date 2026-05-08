def createGraph(V, edges):
    mat = [[0 for _ in range(V)] for _ in range(V)]

    # Add each edge to the adjacency matrix
    for it in edges:
        u = it[0]
        v = it[1]
        mat[u][v] = 1

        # since the graph is undirected
        mat[v][u] = 1
    return mat

if __name__ == "__main__":
    V = 4

    # List of edges (u, v)
    edges = [[0, 1], [0, 2], [1, 2], [2, 3]]

    # Build the graph using edges
    mat = createGraph(V, edges)

    print("Adjacency Matrix Representation:")
    for i in range(V):
        for j in range(V):
            print(mat[i][j], end=" ")
        print()

# Jadi, 
# Di baris pertama, vertex 0 berhubungan dengan vertex 1 dan 2 tapi tidak dengan vertex 0 dan 3
# Di baris kedua, vertex 1 berhubungan dengan vertex 1 dan 2 tapi tidak dengan vertex 1 dan 3
# Di baris ketiga, vertex 2 berhubungan dengan vertex 0, 1, dan 3 tapi tidak dengan vertex 2 
# Di baris keempat, vertex 3 berhubungan dengan vertex 2 tapi tidak dengan vertex 0, 1, dan 3

