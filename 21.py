# Створення класу для роботи з матрицями

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.num_rows = len(matrix)
        self.num_cols = len(matrix[0])

    # Зовнішній вигляд матриці
    def __str__(self):
        matrix_string = ""
        for row in self.matrix:
            matrix_string += " ".join(str(elem) for elem in row) + "\n"
        return matrix_string

    # Приведення матриць за розмірністю для додавання та віднімання
    def resize(self, num_rows, num_cols):
        if num_rows == self.num_rows and num_cols == self.num_cols:
            return self
        new_matrix = []
        for i in range(num_rows):
            row = []
            for j in range(num_cols):
                if i < self.num_rows and j < self.num_cols:
                    row.append(self.matrix[i][j])
                else:
                    row.append(0)
            new_matrix.append(row)
        return Matrix(new_matrix)

    # Додавання матриць
    def __add__(self, other):
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            common_num_rows = max(self.num_rows, other.num_rows)
            common_num_cols = max(self.num_cols, other.num_cols)
            self_resized = self.resize(common_num_rows, common_num_cols)
            other_resized = other.resize(common_num_rows, common_num_cols)
        else:
            self_resized = self
            other_resized = other
        result_matrix = []
        for i in range(self_resized.num_rows):
            row = []
            for j in range(self_resized.num_cols):
                row.append(self_resized.matrix[i][j] + other_resized.matrix[i][j])
            result_matrix.append(row)
        return Matrix(result_matrix)

    # Віднімання матриць
    def __sub__(self, other):
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            common_num_rows = max(self.num_rows, other.num_rows)
            common_num_cols = max(self.num_cols, other.num_cols)
            self_resized = self.resize(common_num_rows, common_num_cols)
            other_resized = other.resize(common_num_rows, common_num_cols)
        else:
            self_resized = self
            other_resized = other
        result_matrix = []
        for i in range(self_resized.num_rows):
            row = []
            for j in range(self_resized.num_cols):
                row.append(self_resized.matrix[i][j] - other_resized.matrix[i][j])
            result_matrix.append(row)
        return Matrix(result_matrix)

    # Множення матриць
    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            result_matrix = []
            for i in range(self.num_rows):
                row = []
                for j in range(self.num_cols):
                    row.append(self.matrix[i][j] * other)
                result_matrix.append(row)
            return Matrix(result_matrix)
        elif isinstance(other, Matrix):
            if self.num_cols != other.num_rows:
                raise ValueError("Розмірності матриць не збігаються")
            result_matrix = []
            for i in range(self.num_rows):
                row = []
                for j in range(other.num_cols):
                    total = 0
                    for k in range(self.num_cols):
                        total += self.matrix[i][k] * other.matrix[k][j]
                    row.append(total)
                result_matrix.append(row)
            return Matrix(result_matrix)

    def __rmul__(self, matr2):
        return self.__mul__(matr2)

    # Транспонування матриць
    def transpose(self):
        result = []
        for i in range(len(self.matrix[0])):
            row = []
            for j in range(len(self.matrix)):
                row.append(self.matrix[j][i])
            result.append(row)
        return Matrix(result)

    # Елементарні перетворення матриць - перестановка рядків
    def swap_rows(self, row1, row2):
        if row1 == row2:
            return self
        if row1 < 0 or row1 >= self.num_rows or row2 < 0 or row2 >= self.num_rows:
            raise IndexError("Індекс рядка поза діапазоном")
        new_matrix = [row[:] for row in self.matrix]
        new_matrix[row1], new_matrix[row2] = new_matrix[row2], new_matrix[row1]
        return Matrix(new_matrix)

    # Елементарні перетворення матриць - множення рядка на константу
    def multiply_row(self, row, scalar):
        if scalar == 0:
            raise ValueError("Неможливо помножити рядок на 0")
        if row < 0 or row >= self.num_rows:
            raise IndexError("Індекс рядка поза діапазоном")
        new_matrix = [row[:] for row in self.matrix]
        for j in range(self.num_cols):
            new_matrix[row][j] *= scalar
        return Matrix(new_matrix)

    # Елементарні перетворення матриць - додавання до рядка матриці іншого рядка, помноженого на ненульове число
    def add_rows(self, src_row, dest_row, scalar=1):
        if src_row == dest_row:
            return self
        if src_row < 0 or src_row >= self.num_rows or dest_row < 0 or dest_row >= self.num_rows:
            raise IndexError("Індекс рядка поза діапазоном")
        new_matrix = [row[:] for row in self.matrix]
        for j in range(self.num_cols):
            new_matrix[dest_row][j] += scalar * new_matrix[src_row][j]
        return Matrix(new_matrix)


# Приклад використання:
a = Matrix([[1, 2, 3], [4, 5, 6],[7, 8, 9]])
b = Matrix([[10, 11, 12], [13, 14, 15], [16, 17, 18]])

print('Матриця a:')
print(a)

print('Матриця b:')
print(b)

print('Додавання матриць a и b:')
print(a + b)

print('Віднімання матриць a и b:')
print(a - b)

print('Множення матриць a и b:')
print(a * b)

print('Множення матриці a на число 2:')
print(a * 2)

print('Транспонування матриці a:')
print(a.transpose())

print('Перестановка рядків a:')
print(a.swap_rows(0, 2))

print('Множення рядка на константу a:')
print(a.multiply_row(0, 10))

print('Додавання до рядка матриці іншого рядка, помноженого на ненульове число a:')
print(a.add_rows(0, 1, 10))
