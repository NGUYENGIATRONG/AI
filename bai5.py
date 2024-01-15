n = int(input("Nhập số nguyên dương : "))
while n < 0:
    n = int(input("Nhập số nguyên dương : "))

gamma = 0.9
lamda = 0.95
delta = 0.5


def tinh(number):
    tong = 0
    for i in range(number + 1):
        tong += (gamma * lamda) ** i * delta
    return tong


print(f"Giá trị biểu thức là {tinh(n)}")
