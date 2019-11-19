import copy
from abstract_matrix import AbstractMatrix

class Matrix(AbstractMatrix):
    def __init__(self, rows, cols, data = []):
       
        self.rows = rows
        self.cols = cols
        self._init_data(data)

        if data:
            data = (self.rows+self.cols) * [0]

    def _has_zero_on_list(lista):
        if 0 in lista:
            return True
        else:
            return False

    def __divisor_invalido(self, divisor):
        if divisor == 0:
            raise ZeroDivisionError("Divisão por zero")
    
    def __multiplicacao_invalida(self, matrix2):
         if(self.cols != matrix2.rows ):
                raise ValueError("Matrizes invalidas!!")

    def __gauss_invalido(self):
        if self.rows+1 != self.cols:
            raise ValueError("Matrix invalida, tem que ser uma matrix NxN+1")
    
    def __matrix_diferentes(self, other):
        if self.rows == other.rows and self.cols == other.cols:
            pass
        else:
            raise ValueError("Matriz invalida, de tamanhos diferentes")

    def __valor_invalido(self,i,j):
        if i > self.rows:
            raise Exception("Valor de rows invalido")

        elif j > self.cols:
            #print(j, self.cols)
            raise Exception("Valor cols invalido")

        elif self.rows <= 0:
            raise Exception("Valor de rows menor que 0 invalido")

        elif self.cols <= 0:
                raise Exception("Valor de cols menor que 0 invalido")

    def __getitem__(self, key):
    
        if type(key) == tuple:
            i, j = key
            self.__valor_invalido(i,j)
            return self.data[(j-1) + (i-1) * self.cols]
        else:
            return self.return_list_rows(key)
        
    def __setitem__(self, key, value):

        if type(key) == tuple:
            i, j = key
            self.__valor_invalido(i,j)
            self.data[(j-1) + (i-1) * self.cols ] = value
        else:
            self.__insert_row(key,value)

    def __repr__(self):
        s = str()
        for i in range(1, self.rows + 1):
            for j in range(1, self.cols + 1):
                s += " {:^5.1f}".format(self[i, j])
            s += "\n"

        return s

    def __str__(self):
       return self.__repr__()

    def __radd__(self, other):
        res = Matrix(self.rows, self.cols)

        if type(other) is int:
            for i in range(1,self.rows + 1):
                for j in range(1,self.cols + 1):
                    res[i, j] = self[i, j] + other
        else:
            self.__matrix_diferentes(other)
            for i in range(1,self.rows + 1):
                for j in range(1,self.cols + 1):
                    res[i, j] = self[i, j] + other[i, j]
        
        return res
    
        
    def __add__(self, other):
        res = Matrix(self.rows, self.cols)

        if type(other) is int:

            for i in range(1,self.rows + 1):
                for j in range(1,self.cols + 1):
                    res[i, j] = self[i, j] + other

        else:
            self.__matrix_diferentes(other)
            for i in range(1,self.rows + 1):
                for j in range(1,self.cols + 1):
                    res[i, j] = self[i, j] + other[i, j]
            
        return res
    
    def __rsub__(self, other):
        new_matrix = self.__sub__(other)
        return new_matrix

    def __sub__(self, other):
        res = Matrix(self.rows, self.cols)
        if type(other) is int:

            for i in range(1,self.rows + 1):
                for j in range(1,self.cols + 1):
                    res[i, j] = self[i, j] - other
        else:
            self.__matrix_diferentes(other)
            for i in range(1,self.rows + 1):
                for j in range(1,self.cols + 1):
                    res[i, j] = self[i, j] - other[i, j]
        return res

    def __rmul__(self, other):
        res = Matrix(self.rows, self.cols)
        if type(other) is int:

            for i in range(1,self.rows + 1):
                for j in range(1,self.cols + 1):
                    res[i, j] = other * self[i, j]
        else:
            self.__matrix_diferentes(other)
            for i in range(1,self.rows + 1):
                for j in range(1,self.cols + 1):
                    res[i, j] = other[i, j] * self[i, j] 
        
        return res
        
    def __mul__(self, other):
        res = Matrix(self.rows, self.cols)
        if type(other) is int:

            for i in range(1,self.rows + 1):
                for j in range(1,self.cols + 1):
                    res[i, j] = self[i, j] * other
        else:
            self.__matrix_diferentes(other)
            for i in range(1,self.rows + 1):
                for j in range(1,self.cols + 1):
                    res[i, j] = self[i, j] * other[i, j]
        
        return res
    
    def __rtruediv__(self, other):
        res = Matrix(self.rows, self.cols)
        if type(other) is int:

            for i in range(1,self.rows + 1):
                for j in range(1,self.cols + 1):
                    self.__divisor_invalido(self[i,j])
                    res[i, j] = self[i, j] / other 
        else:
            self.__matrix_diferentes(other)
            for i in range(1,self.rows + 1):
                for j in range(1,self.cols + 1):
                    self.__divisor_invalido(self[i,j])
                    res[i, j] = self[i, j] / other[i, j]
        
        return res
        

    def __truediv__(self, other):
        res = Matrix(self.rows, self.cols)
        if type(other) is int:

            for i in range(1,self.rows + 1):
                for j in range(1,self.cols + 1):
                    self.__divisor_invalido(other)
                    res[i, j] = self[i, j] / other
        else:
            self.__matrix_diferentes(other)
            for i in range(1,self.rows + 1):
                for j in range(1,self.cols + 1):
                        self.__divisor_invalido(other[i,j])
                        res[i, j] = self[i, j] / other[i, j]
                    
        return res

    def dot(self, b):
            self.__multiplicacao_invalida(b)
            new_matrix = Matrix(self.rows,b.cols)
            for i in range(1,new_matrix.rows + 1):
                for j in range(1,new_matrix.cols + 1):
                    list_rows = self.return_list_rows(i)
                    list_cols = b.return_list_cols(j)
                    value = 0
                    for x1, x2 in zip(list_cols, list_rows):
                        value += x1*x2
                    new_matrix[i,j] = value
            
            return new_matrix


    def transpose(self):
        new_matrix = Matrix(self.cols, self.rows, [])
        for i in range(1,self.rows + 1):
            for j in range(1,self.cols + 1):
                new_matrix[j, i] = self[i, j]
        
        return new_matrix

               


    def _init_data(self, data):
        if data:
            try:
                if len(data) == self.rows * self.cols:
                    self.data = data
                else:
                    raise Exception('Init error', 'The data is incompatible with matrix size')
            except Exception as e:
                print(e)
        else:
            self.data = [0] * (self.rows * self.cols)

    def __insert_row(self,desteny,lista):
        for k in range(1,self.cols+1):
            self[desteny,k] = lista[k-1]

    

    def return_list_rows(self, index):
        rows = list()

        for i in range(1,self.cols + 1):
            rows.append(self[index,i])
        
        return rows

    def return_list_cols(self,index):
        cols = list()
        for i in range(1,self.rows + 1):
            cols.append(self[i,index])

        return cols



    def get_first_one(self,posx,posy):
        #print(posy,posx)
        #print(posy < posx)
        if posy < posx:
            for x in range(1, self.rows):
                if self[x,posy] == 1:
                    return self[x]
        elif posy > posx:
            for x in range(self.rows, 0 , -1):
                if self[x,posy] == 1:
                    return self[x]

            
        
                    


# Pegar cada posicao for com 1,1 e continuar se ele for 1 continue se nao de swap

    def gauss_jordan(self):
        self.__gauss_invalido()
        new_matrix = Matrix(self.rows, self.cols, copy.deepcopy(self.data))

        for i in range(1, new_matrix.cols):
            if new_matrix[i,i] == 0 :
                for j in range(i+1, new_matrix.rows + 1):
                    if new_matrix[j,i] > new_matrix[i,i]:
                        new_matrix[i] ,new_matrix[j] =  new_matrix[j], new_matrix[i]
                        break

            if new_matrix[i,i] != 1:
                #faz a multiplicao pelo valor da linha sobre 1
                new_matrix[i]= [value * (1/new_matrix[i,i]) for value in new_matrix[i]]
            

            for j in range(i+1, new_matrix.rows+1):
                if new_matrix[j,i] != 0:
                    linha = [ ((-1*new_matrix[j,i]) * value) for value in new_matrix[i]]
                    new_matrix [j] = [x + y for x ,y in zip(new_matrix[j], linha)]

    
    #   faz no triangulo superior.
        for j in range(new_matrix.cols - 1, 0, -1):
             for i in range(j - 1, 0 , -1):
                if new_matrix[i,j] != 0:
                    linha = [ ((-1*new_matrix[i,j]) * value) for value in new_matrix[j]]
                    new_matrix [i] = [x + y for x ,y in zip(new_matrix[i], linha)]
                
        return new_matrix


    def __create_identity_matrix(self):
        new_matrix = Matrix(self.rows, self.cols)
        for i in range(1, new_matrix.cols+1):
            new_matrix[i,i] = 1

        return new_matrix

    def __marge_matrix(self, other):
        new_matrix = Matrix(self.rows, self.cols*2)
        for i in range(1, self.rows+1):
            for j in range(1, self.cols+1):
                new_matrix[i,j] = self[i,j]
        
        for k in range(1, self.rows+1):
            for l in range(self.cols+1, new_matrix.cols+1):
                new_matrix[k,l] = other[k,l-self.cols]
           

        return new_matrix


    def __demarge_matrix(self,matrix):
        size = int(matrix.cols / 2)
        #print(size)
        original = Matrix(matrix.rows, size)
        other =  Matrix(matrix.rows, size)
        for i in range(1, self.rows+1):
            for j in range(1, self.cols+1):
                original[i,j] = matrix[i,j]
            
        for k in range(1, self.rows+1):
            for l in range(self.cols+1, matrix.cols+1):
                other[k,l-self.cols] = matrix[k,l]

        return (original, other)





    def inverse(self):
        
        c =  self.__create_identity_matrix()

        d = self.__marge_matrix(c)

        cols = self.cols

        rows = self.rows


        new_matrix = Matrix(d.rows, d.cols, copy.deepcopy(d.data))

        for i in range(1, cols+1):

            if new_matrix[i,i] == 0 :
                for j in range(i+1, rows + 1):
                    if new_matrix[j,i] > new_matrix[i,i]:
                        new_matrix[i] ,new_matrix[j] =  new_matrix[j], new_matrix[i]
                        break

            if new_matrix[i,i] != 1:
                #faz a multiplicao pelo valor da linha sobre 1
                new_matrix[i]= [value * (1/new_matrix[i,i]) for value in new_matrix[i]]
            

            for j in range(i+1, rows + 1):
                if new_matrix[j,i] != 0:
                    linha = [ ((-1*new_matrix[j,i]) * value) for value in new_matrix.get_first_one(j,i)]
                    new_matrix [j] = [x + y for x ,y in zip(new_matrix[j], linha)]

    
    #   faz no triangulo superior.
        for j in range(cols - 1, 0, -1):
             for i in range(j - 1, 0 , -1):
                if new_matrix[i,j] != 0:
                    linha = [ ((-1*new_matrix[i,j]) * value) for value in new_matrix.get_first_one(i,j)]
                    new_matrix [i] = [x + y for x ,y in zip(new_matrix[i], linha)]
                
        _, inversa = self.__demarge_matrix(new_matrix)

        return inversa

        # troca de matriz
        # self[max_row], self[i] = self[i], self[max_row]
                    


