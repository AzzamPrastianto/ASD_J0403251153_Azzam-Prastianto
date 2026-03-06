# Kita pakai bubble sort
def bubbleSortPakBudi(data):
    for passnum in range(len(data)-1, 0, -1):
        for i in range(passnum):
            if data[i]<data[i+1]: 
# Tukar dua data bersebelahan yang urutannya salah
                temp = data[i]
                data[i] = data[i+1]
                data[i+1] = temp

data = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]
bubbleSortPakBudi(data)

# Skor lima kandidat tersebut dari yang paling tinggi hingga terendah.
x = 0
for i in range(1,6):
    print("Rangking", x+1, ":", data[x])
    x+=1

# Yang lolos kandidat dengan nilai 98, 89, 76, 68, dan 57

