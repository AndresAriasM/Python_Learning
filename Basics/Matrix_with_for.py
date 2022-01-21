#Trabajar la matriz como una lista de listas 
#Sumar los valores de dos matrices distintas 

X = [[2, 4, 6], [8, 10, 12], [14, 16, 18]]
Y = [[1, 3, 5], [7, 9, 11], [ 13, 15 ,17]]
S = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(len(X)):
  for j in range(len(X[0])):
    S[i][j] = X[i][j] + Y[i][j]

for r in S:
  print(r)

