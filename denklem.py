
matrix = [[0,5,8,6,14], [3,1,-6,-3,5], [1,2,5,9,7]]
def solve(matris):
    size = len(matris)
    for i in range(len(matris)):
        for j in range(len(matris) - 1, i, -1):
            if (matris[i][i] == 0):
                return
            temp = matris[j][i] / matris[i][i]
            for k in range(len(matris[0])):
                matris[j][k] = -temp * matris[i][k] + matris[j][k]

    for i in range(len(matris) - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            if (matris[i][i] == 0):
                return
            temp2 = matris[j][i] / matris[i][i]
            for k in range(len(matris[0])):
                matris[j][k] = -temp2 * matris[i][k] + matris[j][k]
                
    for l in range(size):
        matris[l][size] = matris[l][size] / matris[l][l]
        matris[l][l] = matris[l][l] / matris[l][l]
    return matris


print(solve(matrix))