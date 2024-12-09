def add(matrix_a , matrix_b):
    result = [];
    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_a)):
            element = matrix_a[i][j] + matrix_b[i][j]
            row.append(element)
        result.append(row)
    print("Addition of matrix is : ",result)

def sub(matrix_a,matrix_b):
    result = []
    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_b)):
            element = matrix_a[i][j] - matrix[i][j]
            row.append(element)
        result.append(row)
    print("Substraction of matrix is :",result)

def mul(matrix_a,matrix_b):
    result=[]
    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_b)):
            element = 0
            for k in range(len(matrix_a)):
                element = element + matrix_a[i][k] * matrix_b[k][j]
            row.append(element)
        result.append(row)
    print("Multiplication of matrix :",result)

def transpose(matrix_a):
    result = []
    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_a)):
            element = matrix_a[j][i]
            row.append(element)
        result.append(row)
    print(result)

def matrix():
    result = []
    print("Enter number of rows in matrix:")
    rows = int(input())
    columns = int(input("Enter total number of columns:"))
    for i in range(rows):
        temp = []
        for j in range(columns):
            element = int(input("Enter the element at "))
            temp.append(element)
        result.append(temp)
    return result;

matrix_a = matrix();
#matrix_b = matrix();
#add(matrix_a,matrix_b)
#mul(matrix_a,matrix_b)
transpose(matrix_a)