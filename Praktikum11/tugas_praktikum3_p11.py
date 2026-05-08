matrix = [[0, 1, 1, 0], 
          [1, 0, 1, 0], 
          [1, 1, 0, 1], 
          [0, 0, 1, 0]]

def createGraph(V, adj_matrix):
    adj_list = [[] for _ in range(V)]

    for i in range(V):          
        for j in range(V):      
            if adj_matrix[i][j] == 1:
                adj_list[i].append(j)
                
    return adj_list

if __name__ == "__main__":
    V = 4
    adj = createGraph(V, matrix)

    print("Adjacency List Representation:")
    for i in range(V):
        print(f"{i}: {' '.join(map(str, adj[i]))}")

'''
Kode ini mengonversi representasi graf dari bentuk adjacency matrix menjadi adjacency list dengan cara 
menelusuri setiap sel matriks dan menyimpan indeks kolom sebagai tetangga jika ditemukan nilai satu.
'''