import random

print("=== Sayı Tahmin Oyunu ===")

sayi = random.randint(1, 50)

tahmin = int(input("1 ile 50 arasında bir sayi tahmin et: "))

if tahmin == sayi:
    print("Tebrikler! Doğru bildin!")
else:
    print(f"Yanlış tahmin! Doğru sayı: {sayi}")
