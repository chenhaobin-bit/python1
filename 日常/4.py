class Matrix:
    def __init__(self,m,n):
        self.m = m
        self.n = n
        self.data = []
        for i in range(m):
            row = []
            for j in range(n):
                row.append(0)
            self.data.append(row)

    def set_data(self,data):
        index = 0
        for i in range(self.m):
            for j in range(self.n):
                self.data[i][j] = data[index]
                index += 1
    def transpose(self):
        tr = Matrix(self.n,self.m)
        for i in range(self.n):
            for j in range(self.m):
                tr.data[i][j] = self.data[j][i]
        return tr;
    def __str__(self):
        rows_str = [" ".join(map(str, row)) for row in self.data]
        return "\n".join(rows_str)
    
m = int(input())
n = int(input())    
data = eval(input())
mat1 = Matrix(m,n)
mat1.set_data(data)
print(mat1)
print(mat1.transpose())