# 1
# matematik.py
def qoshish(a, b):
    return a + b

def ayirish(a, b):
    return a - b

def kopaytirish(a, b):
    return a * b


# main
import matematik

print(matematik.qoshish(10, 5))
print(matematik.ayirish(10, 5))
print(matematik.kopaytirish(10, 5))


# 2
# geometriya.py
import math

def doira_yuzi(r):
    return math.pi * r * r

def kvadrat_yuzi(a):
    return a * a

def uchburchak_yuzi(a, h):
    return (a * h) / 2


# main
import geometriya

print(geometriya.doira_yuzi(7))
print(geometriya.kvadrat_yuzi(5))
print(geometriya.uchburchak_yuzi(6, 4))


# 3
# matn_utils.py
def katta_harf(matn):
    return matn.upper()

def teskari(matn):
    return matn[::-1]

def sozlar_soni(matn):
    return len(matn.split())


# main
import matn_utils

text = "Salom Python"
print(matn_utils.katta_harf(text))
print(matn_utils.teskari(text))
print(matn_utils.sozlar_soni(text))


# 4
# harorat.py
def celsius_fahrenheit(c):
    return c * 9/5 + 32

def fahrenheit_celsius(f):
    return (f - 32) * 5/9

def celsius_kelvin(c):
    return c + 273.15


# main
import harorat

print(harorat.celsius_fahrenheit(25))
print(harorat.celsius_kelvin(25))
print(harorat.fahrenheit_celsius(77))


# 5
# talaba.py
def ortacha_baho(baholar):
    return sum(baholar) / len(baholar)

def eng_yuqori(baholar):
    return max(baholar)

def eng_past(baholar):
    return min(baholar)


# main
import talaba

grades = [85, 90, 78, 92, 88]
print(talaba.ortacha_baho(grades))
print(talaba.eng_yuqori(grades))
print(talaba.eng_past(grades))
