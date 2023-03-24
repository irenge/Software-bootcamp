# define function

def grid(z, i, j, x):
    neigh = [] # to hold list of interesting neighbours
    if i > 0:
        neigh.append(z[i-1][j])
        if j > 0:
            neigh.append(z[i-1][j-1])
        if j < x:
            neigh.append(z[i-1][j+1])
    if j > 0:
        neigh.append(z[i][j - 1])
        if i < x:
            neigh.append(z[i+1][j-1])
    if j < x:
        neigh.append(z[i][j+1])
        if i < x:
            neigh.append(z[i+1][j+1])
    if i < 4:
        neigh.append(z[i + 1][j])
    return str(sum(1 for i in neigh if i == '#'))

#initialise variables

matrix = [ ["-", "-", "-", "#", "#"],
["-", "#", "-", "-", "-"],
["-", "-", "#", "-", "-"],
["-", "#", "#", "-", "-"],
["-", "-", "-", "-", "-"] ]

a = 4

# compute, replace and print 

for i, values in enumerate(matrix, start = 0):
    for j, value in enumerate(values, start = 0):
        if value == '-':
            value = grid(matrix,i,j,a)
        print(value, end=" ")
    print()                                                                                                                                                                                           
