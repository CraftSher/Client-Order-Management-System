class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]  # Инициализация матрицы 0

    def add(self, other):
        # Сложение матриц
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Размеры матриц не совпадают!")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def subtract(self, other):
        # Вычитание матриц
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Размеры матриц не совпадают!")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] - other.data[i][j]
        return result

    def multiply(self, other):
        # Умножение матриц
        if self.cols != other.rows:
            raise ValueError("Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы!")
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                result.data[i][j] = sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
        return result

    def transpose(self):
        # Транспонирование матрицы
        result = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[j][i] = self.data[i][j]
        return result

    def __str__(self):
        # Вывод матрицы в виде строки
        return '\n'.join(' '.join(map(str, row)) for row in self.data)


# Примеры работы с классом:

# Создание экземпляров класса Matrix
m1 = Matrix(2, 3)
m1.data = [[1, 2, 3], [4, 5, 6]]

m2 = Matrix(2, 3)
m2.data = [[7, 8, 9], [10, 11, 12]]

# Тестирование операций
print("Матрица 1:")
print(m1)

print("Матрица 2:")
print(m2)

print("Сложение матриц:")
print(m1.add(m2))

print("Вычитание матриц:")
print(m1.subtract(m2))

m3 = Matrix(3, 2)
m3.data = [[1, 2], [3, 4], [5, 6]]

print("Умножение матриц:")
print(m1.multiply(m3))

print("Транспонирование матрицы 1:")
print(m1.transpose())