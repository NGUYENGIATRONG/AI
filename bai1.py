import math

a = int(input("Nhập cạnh thứ nhất: "))
b = int(input("Nhập cạnh thứ hai: "))
c = int(input("Nhập cạnh thứ ba: "))

while a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
    a = int(input("Nhập cạnh thứ nhất: "))
    b = int(input("Nhập cạnh thứ hai: "))
    c = int(input("Nhập cạnh thứ ba: "))


def check(x: int, y: int, z: int):
    angle_a = math.degrees(math.acos((y ** 2 + z ** 2 - x ** 2) / (2 * y * z)))
    angle_b = math.degrees(math.acos((x ** 2 + z ** 2 - y ** 2) / (2 * x * z)))
    angle_c = math.degrees(math.acos((y ** 2 + x ** 2 - z ** 2) / (2 * y * x)))
    if angle_a == angle_b == angle_c:
        print("Đây là tam giác đều")
    elif angle_a == angle_b != angle_c or angle_a != angle_b == angle_c or angle_a == angle_c != angle_b:
        print("Đây là tam giác cân")
    elif angle_a == 90 or angle_b == 90 or angle_c == 90:
        print("Đây là tam giác vuông")
    else:
        if angle_a < 90 and angle_b < 90 and angle_c < 90:
            print("Đây là tam giác nhọn")
        if angle_a > 90 or angle_b > 90 or angle_c > 90:
            print("Đây là tam giác tù")


def cv(x: int, y: int, z: int):
    return x + y + z


def dt(x: int, y: int, z: int):
    p = cv(x, y, z) / 2
    return math.sqrt(p * (p - x) * (p - y) * (p - z))


check(a, b, c)
print(f"Chu vi tam giác là {cv(a, b, c)}")
print(f"Diện tích tam giác là {dt(a, b, c)}")
