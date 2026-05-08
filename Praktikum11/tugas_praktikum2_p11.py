from collections import defaultdict 
graph = defaultdict(list) 
graph["A"].append("B") 
graph["A"].append("C") 
graph["B"].append("A")
graph["B"].append("D")
graph["C"].append("A")
graph["C"].append("D")
graph["D"].append("B")
graph["D"].append("C")

print(dict(graph))

'''
Kita membuat dictionary dan kita mendefinisikan key A, B, C, dan D
serta mendefinisikan value A, B, C, dan D. Disini kita menambah key
dan value berdasarkan vertex yang berhubungan. Setelah memasukkan semua
vertex, didapatkanlah dictionary yang berisi keys berupa vertex dan value
berupa vertex-vertex yang berhubungan dengan key.
'''