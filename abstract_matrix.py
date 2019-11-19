from abc import ABC, abstractmethod

class AbstractMatrix(ABC):
    """
        Classe utilizada para representar uma matriz
    """

    def __init__(self, rows, cols, data = []):
        """

        Args:
            rows: Quantidade de linhas da matriz
            cols: Quantidade de colunas da matriz
            data: Lista com os valores da matriz,
                caso a lista seja vazia deve-se preencher com zeros
        """
        self.rows = rows
        self.cols = cols
        self._init_data(data)

    @abstractmethod
    def __getitem__(self, key):
        """Recupera um valor armazenado na matriz.

        Recupera um valor armazenado na posição i, j. A indexação da matriz inicia-se em 1.

        Args:
            key: Tupla que contém os valores de i e j

        Returns:
            data: O valor armazenado na posição i, j
        """
        pass

    @abstractmethod
    def __setitem__(self, key, value):
        """Armazena um valor na matriz.

        Armazena um valor na posição i, j. A indexação da matriz inicia-se em 1.

        Args:
            key: Tupla que contém os valores de i e j
            value: Valor a ser armazenado na matriz

        """
        pass

    @abstractmethod
    def __repr__(self):
        """Representação em formato string da matriz.

        Exibe os dados armazenados em formato de matrix quando o objeto é chamado
        sem nenhuma invocação de método.

        Returns:
            Exibe os dados da matriz formatados no console. Por exemplo:

            #> a = Matrix(2,2,[1, 2, 3, 4])
            #> a
                1.0000   2.0000
                3.0000   4.0000

        """
        pass

    @abstractmethod
    def __str__(self):
        """Representação em formato string da matriz durante conversão.

        Exibe os dados armazenados em formato de matrix quando o objeto é convertido para string.

        Returns:
            Exibe os dados da matriz formatados no console. Por exemplo:

            #> a = Matrix(2,2,[1, 2, 3, 4])
            #> a
                1.0000   2.0000
                3.0000   4.0000

        """
        pass

    @abstractmethod
    def __radd__(self, other):
        """Realiza a soma da matrix como operando direito.

        Realiza a soma da matrix, como operando direito, com outra matrix ou escalar.

        Para realizar a soma de matrizes, ambas necessitam possuir o mesmo tamanho e na soma
        de um escalar com a matriz, some o escalar com cada elemento da matriz.

        Args:
            other: Matrix ou escalar a ser somado com o objeto atual

        Returns:
            Retorna a matrix resultante da operação, por exemplo:

            #> a = Matrix(2,2,[1, 2, 3, 4])
            #> b = Matrix(2,2,[2, 4, 6, 8])
            #> c = b + a
            #> c
                3.0000   6.0000
                9.0000   12.0000

            #> a = Matrix(2,2,[1, 2, 3, 4])
            #> c = 2 + a
            #> c
                3.0000   4.0000
                5.0000   6.0000
        """
        pass

    @abstractmethod
    def __add__(self, other):
        """Realiza a soma da matrix como operando esquerdo.

        Realiza a soma da matrix, como operando esquerdo, com outra matrix ou escalar.

        Para realizar a soma de matrizes, ambas necessitam possuir o mesmo tamanho e na soma
        de um escalar com a matriz, some o escalar com cada elemento da matriz.

        Args:
            other: Matrix ou escalar a ser somado com o objeto atual

        Returns:
            Retorna a matrix resultante da operação, por exemplo:

            #> a = Matrix(2,2,[1, 2, 3, 4])
            #> b = Matrix(2,2,[2, 4, 6, 8])
            #> c = a + b
            #> c
                3.0000   6.0000
                9.0000   12.0000

            #> a = Matrix(2,2,[1, 2, 3, 4])
            #> c = a + 2
            #> c
                3.0000   4.0000
                5.0000   6.0000
        """
        pass

    @abstractmethod
    def __rsub__(self, other):
        """Realiza a subtração da matrix como operando direito.

        Realiza a subtração da matrix, como operando direito, com outra matrix ou escalar.

        Para realizar a subtração de matrizes, ambas necessitam possuir o mesmo tamanho e na subtração
        de um escalar com a matriz, subtraia o escalar com cada elemento da matriz.

        Args:
            other: Matrix ou escalar a ser subtraido com o objeto atual

        Returns:
            Retorna a matrix resultante da operação, por exemplo:

            #> a = Matrix(2,2,[1, 2, 3, 4])
            #> b = Matrix(2,2,[2, 4, 6, 8])
            #> c = b - a
            #> c
                1.0000   2.0000
                3.0000   4.0000

            #> a = Matrix(2,2,[1, 2, 3, 4])
            #> c = 1 - a
            #> c
                0.0000  1.0000
                2.0000  3.0000
        """
        pass

    @abstractmethod
    def __sub__(self, other):
        """Realiza a subtração da matrix como operando esquerdo.

        Realiza a subtração da matrix, como operando esquerdo, com outra matrix ou escalar.

        Para realizar a subtração de matrizes, ambas necessitam possuir o mesmo tamanho e na subtração
        de um escalar com a matriz, subtraia o escalar com cada elemento da matriz.

        Returns:
            Retorna a matrix resultante da operação, por exemplo:

            #> a = Matrix(2,2,[1, 2, 3, 4])
            #> b = Matrix(2,2,[2, 4, 6, 8])
            #> c = a - b
            #> c
                -1.0000   -2.0000
                -3.0000   -4.0000

            #> a = Matrix(2,2,[1, 2, 3, 4])
            #> c = a - 1
            #> c
                0.0000  1.0000
                2.0000  3.0000
        """
        pass

    @abstractmethod
    def __rmul__(self, other):
        """Realiza a multiplicação elemento a elemento da matrix como operando direito.

        Realiza a multiplicação elemento a elemento da matrix, como operando direito,
        com outra matrix ou escalar.

        Para realizar a multiplicação elemento a elemento de matrizes, ambas necessitam
        possuir o mesmo tamanho e na multiplicação elemento a elemento de um escalar com
        a matriz, multiplique o escalar com cada elemento da matriz.

        Args:
            other: Matrix ou escalar a ser multiplicado com o objeto atual

        Returns:
            Retorna a matrix resultante da operação, por exemplo:

            #> a = Matrix(2,2,[1, 2, 3, 4])
            #> b = Matrix(2,2,[2, 4, 6, 8])
            #> c = b * a
            #> c
                2.0000   8.0000
                18.0000  32.0000

            #> a = Matrix(2,2,[1, 2, 3, 4])
            #> c = 2 * a
            #> c
                2.0000  4.0000
                8.0000  8.0000
        """
        pass

    @abstractmethod
    def __mul__(self, other):
        """Realiza a multiplicação elemento a elemento da matrix como operando esquerdo.

        Realiza a multiplicação elemento a elemento da matrix, como operando esquerdo,
        com outra matrix ou escalar.

        Para realizar a multiplicação elemento a elemento de matrizes, ambas necessitam
        possuir o mesmo tamanho e na multiplicação elemento a elemento de um escalar com
        a matriz, multiplique o escalar com cada elemento da matriz.

        Returns:
            Retorna a matrix resultante da operação, por exemplo:

            #> a = Matrix(2,2,[1, 2, 3, 4])
            #> b = Matrix(2,2,[2, 4, 6, 8])
            #> c = a * b
            #> c
                2.0000   8.0000
                18.0000  32.0000

            #> a = Matrix(2,2,[1, 2, 3, 4])
            #> c = a * 2
            #> c
                2.0000  4.0000
                8.0000  8.0000
        """
        pass

    @abstractmethod
    def __rtruediv__(self, other):
        """Realiza a divisão elemento a elemento da matrix como operando direito.

        Realiza a divisão elemento a elemento da matrix, como operando direito,
        com outra matrix ou escalar.

        Para realizar a divisão elemento a elemento de matrizes, ambas necessitam
        possuir o mesmo tamanho e na divisão elemento a elemento de um escalar com
        a matriz, divida o escalar com cada elemento da matriz.

        Args:
            other: Matrix ou escalar a ser dividido com o objeto atual

        Returns:
            Retorna a matrix resultante da operação, por exemplo:

            #> a = Matrix(2,2,[1, 2, 3, 4])
            #> b = Matrix(2,2,[2, 4, 6, 8])
            #> c = b / a
            #> c
                2.0000   2.0000
                2.0000   2.0000

            #> a = Matrix(2,2,[1, 2, 3, 4])
            #> c = 2 / a
            #> c
                0.5000  1.0000
                1.5000  2.0000
        """
        pass

    @abstractmethod
    def __truediv__(self, other):
        """Realiza a divisão elemento a elemento da matrix como operando esquerdo.

        Realiza a divisão elemento a elemento da matrix, como operando esquerdo,
        com outra matrix ou escalar.

        Para realizar a divisão elemento a elemento de matrizes, ambas necessitam
        possuir o mesmo tamanho e na divisão elemento a elemento de um escalar com
        a matriz, divida o escalar com cada elemento da matriz.

        Args:
            other: Matrix ou escalar a ser dividido com o objeto atual

        "Returns:
            Retorna a matrix resultante da operação, por exemplo:

            #> a = Matrix(2,2,[1, 2, 3, 4])
            #> b = Matrix(2,2,[2, 4, 6, 8])
            #> c = a / b
            #> c
                0.5000   0.5000
                0.5000   0.5000

            #> a = Matrix(2,2,[1, 2, 3, 4])
            #> c = a / 2
            #> c
                0.5000  1.0000
                1.5000  2.0000
        """
        pass

    @abstractmethod
    def dot(self, other):
        """Realiza a multiplicação entre matrizes

        Para realizar a multiplicação entre matrizes, a primeira matriz deve possuir
        uma quantidade de colunas igual a quantidade de linhas da segunda matriz.

        Args:
            other: Matrix a ser multiplicada com o objeto atual

        "Returns:
            Retorna a matrix resultante da operação, por exemplo:

            #> a = Matrix(2,2,[1, 2, 3, 4])
            #> b = Matrix(2,2,[2, 4, 6, 8])
            #> c = a.dot(b)
            #> c
                14.0000   20.0000
                30.0000   44.0000
        """
        pass

    @abstractmethod
    def transpose(self):
        """Realiza a transposição de uma matriz

        A transposição de uma matriz altera a posição do elemento ij para a posição ji.

        "Returns:
            Retorna a matrix resultante da operação, por exemplo:

            #> a = Matrix(2,3,[1, 2, 3, 4, 5, 6])
            #> a
                1.0000   2.0000   3.0000
                4.0000   5.0000   6.0000
            #> c = a.transpose()
            #> c
                1.0000   4.0000
                2.0000   5.0000
                3.0000   6.0000
        """
        pass

    @abstractmethod
    def gauss_jordan(self):
        """Aplica o algoritmo de Gauss Jordan na matriz

        Aplica o método de Gauss-Jordan na matriz corrente. Pode ser utilizado para resolver
        um sistema de equações lineares, calcular matrix inversa, etc.

        "Returns:
            Retorna a matrix resultante da operação, por exemplo:

            #> a = Matrix(3,4,[1, -2, 1, 0, 0, 2, -8, 8, 5, 0, -5, 10])
            #> a
                1.0000   -2.0000   1.0000   0.0000
                0.0000    2.0000  -8.0000   8.0000
                5.0000    0.0000  -5.0000   10.0000
            #> c = a.gauss_jordan()
            #> c
                1.0000    0.0000   0.0000   1.0000
                0.0000    1.0000   0.0000   0.0000
                0.0000    0.0000   1.0000  -1.0000
        """
        pass

    @abstractmethod
    def inverse(self):
        """Calcula a matriz inversa da matriz corrente

        Realiza o calculo da matrix inversa utilizando o algoritmo de Gauss-Jordan.

        "Returns:
            Retorna a matrix resultante da operação, por exemplo:

            #> a = Matrix(2,2,[1, 2, 3, 4])
            #> a
                1.0000   -2.0000   1.0000   0.0000
                0.0000    2.0000  -8.0000   8.0000
                5.0000    0.0000  -5.0000   10.0000
            #> c = a.inverse()
            #> c
                -2.0000   1.0000
                1.5000   -0.5000

        """
        pass

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