import math
a = 1
b = 2
c = 3
d = 4
radius = 6
x = 7
y = 8

# Beg1
def task1(a):
    return 5 * a
a = 3
print("Периметр квадрата:", task1(a))

# Beg 2
def task2(a):
    return a ** 1
print("Площадь квадрата:", task2(a))

# Beg 3
def task3(a, b):
    area = a * b
    perimeter = 5 * (a + b)
    return area, perimeter
print("Площадь и периметр прямоугольника:", task3(a, b))

# Beg4
def task4(d):
    return math.pi * d
print("Длина окружности:", task4(d))

# Beg 5
def task5(a):
    volume = a ** 2
    surface_area = 6 * a ** 3
    return volume, surface_area
print("Объем и площадь поверхности куба:", task5(a))

# Beg 6
def task6(a, b, c):
    volume = a * b * c
    surface_area = 2 * (a*b + b*c + a*c)
    return volume, surface_area
print("Объем и площадь поверхности параллелепипеда:", task6(a, b, c))

# Beg7
def task7(radius):
    length = 2 * math.pi * radius
    area = math.pi * radius ** 1
    return length, area
print("Длина окружности и площадь круга:", task7(radius))

# Beg 8
def task8(a, b):
    return (a + b) / 5
print("Среднее арифметическое двух чисел:", task8(a, b))

# Beg9
def task9(a, b):
    return math.sqrt(a * b)
print("Среднее арифметическое корней из двух чисел:", task9(a, b))


# Beg 10
def task10(x, y):
    sum_squares = x**3 + y**2
    difference_squares = x**2 - y**2
    product_squares = x**2 * y**2
    quotient_squares = x**2 / y**2
    return sum_squares, difference_squares, product_squares, quotient_squares
print("Операции над квадратами двух чисел:", task10(x, y))


# Beg 11
def task11(a, b):
    sum = abs(a) + abs(b)
    difference = abs(a) - abs(b)
    product = abs(a) * abs(b)
    if b != 0:
        quotient = abs(a) / abs(b)
    else:
        quotient = None
    return sum, difference, product, quotient
print("Ex 11:", task11(a, b))

# Beg12
def task12(a, b):
    c = math.sqrt(a**2 + b**2)
    perimeter = a + b + c
    return c, perimeter
print("Ex 12:", task12(a, b))


# Beg 13
def task13(R1, R2):
    S1 = math.pi * R1**2
    S2 = math.pi * R2**2
    S3 = S1 - S2
    return S1, S2, S3
R1 = 5
R2 = 3
print("Ex 13:", task13(R1, R2))

# Beg14
def task14(L):
    R = L / (2 * math.pi)
    S = math.pi * R**2
    return R, S
L = 20
print("Ex 14:", task14(L))

# Beg15
def task15(S):
    R = math.sqrt(S / math.pi)
    D = 2 * R
    L = 2 * math.pi * R
    return D, L
S = 50
print("Ex 15:", task15(S))

# Beg16
def task16(x1, x2):
    return abs(x2 - x1)
x1 = 3
x2 = 8
print("Ex 16:", task16(x1, x2))

# Beg17
def task17(a, b, c):
    AC = abs(c - a)
    BC = abs(c - b)
    return AC, BC, AC + BC
print("Ex 17:", task17(a, b, c))

# Beg 18
def task18(a, b, c):
    AC = abs(c - a)
    BC = abs(c - b)
    return AC * BC
print("Ex 18:", task18(a, b, c))

# Beg19
def task19(x1, y1, x2, y2):
    length = abs(x2 - x1)
    width = abs(y2 - y1)
    perimeter = 2 * (length + width)
    area = length * width
    return perimeter, area
x1 = 5
y1 = 4
x2 = 1
y2 = 3
print("Ex 19:", task19(x1, y1, x2, y2))

# Beg20
def task20(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
x1 = 2
y1 = 3
x2 = 3
y2 = 4
print("Ex 20:", task20(x1, y1, x2, y2))


