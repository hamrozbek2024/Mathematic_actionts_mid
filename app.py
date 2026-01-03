import random
import math
import string

print("=" * 50)

# 1. FIBONACCI KETMA-KETLIGI
n = int(input("Fibonacci uchun N ni kiriting: "))
fib = [0, 1]
for i in range(2, n):
    fib.append(fib[i-1] + fib[i-2])
print("Fibonacci:", fib[:n])

print("=" * 50)

# 2. TUB SONLAR
n = int(input("N ni kiriting (tub sonlar uchun): "))
print("Tub sonlar:")
for son in range(2, n + 1):
    tub = True
    for i in range(2, int(son ** 0.5) + 1):
        if son % i == 0:
            tub = False
            break
    if tub:
        print(son, end=" ")
print()

print("=" * 50)

# 3. RO'YXATNI SARALASH (sort ishlatilmagan)
nums = list(map(int, input("Raqamlarni kiriting (bo‘sh joy bilan): ").split()))
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
print("Saralangan:", nums)

print("=" * 50)

# 4. ENG KO'P UCHRAYDIGAN ELEMENT
lst = list(map(int, input("Ro'yxat kiriting: ").split()))
eng_kop = max(set(lst), key=lst.count)
print("Eng ko‘p uchraydigan:", eng_kop)

print("=" * 50)

# 5. SO'ZLARNI SANASH
gap = input("Jumla kiriting: ")
print("So'zlar soni:", len(gap.split()))

print("=" * 50)

# 6. PAROL GENERATORI
uzunlik = int(input("Parol uzunligini kiriting: "))
belgilar = string.ascii_letters + string.digits + "!@#$%^&*"
parol = "".join(random.choice(belgilar) for _ in range(uzunlik))
print("Yangi parol:", parol)

print("=" * 50)

# 7. LOTO O'YINI
loto = random.sample(range(1, 51), 6)
print("Loto raqamlari:", loto)

print("=" * 50)

# 8. MATN FAYL O‘QISH
fayl_nomi = input("Matn fayl nomini kiriting (example.txt): ")
try:
    with open(fayl_nomi, "r", encoding="utf-8") as f:
        sozlar = f.read().lower().split()
        top5 = sorted(set(sozlar), key=sozlar.count, reverse=True)[:5]
        print("Eng ko‘p ishlatilgan 5 ta so‘z:", top5)
except:
    print("Fayl topilmadi!")

print("=" * 50)

# 9. DUBLIKATLARNI O‘CHIRISH
lst = list(map(int, input("Ro'yxat kiriting: ").split()))
natija = []
for i in lst:
    if i not in natija:
        natija.append(i)
print("Dublikatlarsiz:", natija)

print("=" * 50)

# 10. SONNI SO‘Z BILAN YOZISH (0–999)
birlik = ["nol","bir","ikki","uch","to'rt","besh","olti","yetti","sakkiz","to'qqiz"]
onlik = ["","o'n","yigirma","o'ttiz","qirq","ellik","oltmish","yetmish","sakson","to'qson"]

son = int(input("0–999 oralig‘ida son kiriting: "))
if son < 10:
    print(birlik[son])
elif son < 100:
    print(onlik[son//10], birlik[son%10])
else:
    print(birlik[son//100], "yuz", onlik[(son%100)//10], birlik[son%10])

print("=" * 50)

# 11. ANAGRAMMA
s1 = input("1-so'z: ").lower()
s2 = input("2-so'z: ").lower()
print("Anagramma" if sorted(s1) == sorted(s2) else "Anagramma emas")

print("=" * 50)

# 12. KVADRAT TENGLAMA
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
d = b*b - 4*a*c

if d > 0:
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    print("Ildizlar:", x1, x2)
elif d == 0:
    x = -b / (2*a)
    print("Bitta ildiz:", x)
else:
    print("Haqiqiy ildiz yo‘q")

print("=" * 50)

# 13. MATRITSALARNI QO‘SHISH (3x3)
print("1-matritsa:")
A = [[int(input()) for _ in range(3)] for _ in range(3)]
print("2-matritsa:")
B = [[int(input()) for _ in range(3)] for _ in range(3)]

C = [[A[i][j] +]()]()
