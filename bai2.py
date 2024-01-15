n = int(input("Nhập số nguyên dương : "))
while n < 0:
    n = int(input("Nhập số nguyên dương : "))


def gt(number: int):
    if number == 0 or number == 1:
        return 1
    else:
        return number * gt(number - 1)


def shh(number: int):
    t = 0
    for i in range(1, number):
        if number % i == 0:
            t += i
    return t == number


def check(number: int):
    tong = 0
    dem = 0
    for i in range(1, gt(number)):
        if shh(i) == 1:
            dem += 1
            print(i)
            tong += i
    print(f"Có {dem} số hoàn hảo trong khoảng từ 1 đến {gt(n)} ")
    print(f"Tổng các số hoàn hảo là: {tong} ")


print(f"{n} ! = {gt(n)}")

check(n)
