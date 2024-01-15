n = int(input("Nhập số lượng phần tử của danh sách: "))
while n < 0:
    n = int(input("Nhập số lượng phần tử của danh sách: "))
listA = []

for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i + 1}: "))
    listA.append(x)

print("listA: ", listA)

listB = []

for i in listA:
    if i not in listB:
        listB.append(i)

print("List A sau khi loại bỏ phần tử trùng lặp:", listB)

listC = sorted(listB)

print("List B sau khi sap xep: ", listC)


def check(number: int):
    count = 0
    for j in range(number):
        if number % (j + 1) == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False


listD = []

for i in listC:
    if check(i):
        listD.append(i)

print("Các số nguyên tố trong listC là: ", listD)

listE = listD[::-1]
print("ListE= ", listE)


def tbc(mylist):
    tong = sum(mylist)
    spt = len(mylist)
    tb = tong / spt
    return tb


print(f"{tbc(listA)}")
