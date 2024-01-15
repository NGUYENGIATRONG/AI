m = int(input('Nhập số hàng m: '))
n = int(input('Nhập số cột n: '))
while m < 1 or n < 1:
    m = int(input('Nhập số hàng m: '))
    n = int(input('Nhập số cột n: '))


def print_matrix(mt: list):
    for a in mt:
        print(a)


matrixA = []

for i in range(m):
    hang = []
    for j in range(n):
        value = int(input(f'Nhập giá trị cho phần tử thứ ({i}, {j}): '))
        hang.append(value)
    matrixA.append(hang)

print("Ma trận vừa nhập là: ")
print_matrix(matrixA)
s = 0
for i in range(m):
    for j in range(n):
        s += matrixA[i][j]
print(f"Tổng các số hạng trong ma trận là {s}")
t = 1
for i in range(m):
    for j in range(n):
        if i == j:
            t *= matrixA[i][j]
print(f"Tích các số hạng trong đường chéo chính là  là {t}")
x = int(input("Nhap vao so x: "))
matrixB = []
for i in range(m):
    hang = []
    for j in range(n):
        hang.append(matrixA[i][j] * x)
    matrixB.append(hang)
print(f"Tích của  {x} với ma trận A = ")
print_matrix(matrixB)


def check(number):
    if number < 0:
        return False
    a, b = 0, 1
    while a < number:
        tg = a
        a = b
        b = tg + b
    return a == number


for i in range(m):
    for j in range(n):
        if check(matrixA[i][j]) == 1:
            print(matrixA[i][j])
            print(f"Vi trí ({i}, {j})")
