#  komperasi (true, false)
# > < >= <= == != is is-not
# Nama: Amrina Rosyada
# Nim: 25241075
# x = # (2 digit nim pertama)
# y = # (2 digit nim akhir)
x = 6
y = 5
hasil = x > 5
print(x, ">", 5, "=", hasil)

x = 6
y = 5
hasil = y < 6
print(y, "<", 6, "=", hasil)

x = 6
y = 5
hasil = x >= 5
print(x, ">=", 5, "=", hasil)

x = 6
y = 5
hasil = y <= 6
print(y, "<=", 6, "=", hasil)


x = 6
y = 6
hasil = y == 6
print(y, "==", 6, "=", hasil)

x = 6
y = 5
hasil = y != 6
print(y, "!=", 6, "=", hasil)

x = 5
y = 5
hasil = y is 5
print(y, "is", 5, "=", hasil)

x = 6
y = 4
hasil = y is not 6
print(y, "is not", 6, "=", hasil)

# TUGAS
x = 25
y = 75

print("========== lebih dari (>)")
hasil = x > 24
print(x, ">", 24, "=", hasil)
hasil = x > 26
print(x, ">", 26, "=", hasil)

print("========== kurang dari (<)")
hasil = y < 76
print(y, "<", 276, "=", hasil)
hasil = y < 70
print(y, "<", 770, "=", hasil)

print("========== lebih dari sama dengan (>=)")
hasil = x >= 24
print(x, ">=", 24, "=", hasil)
hasil = x >= 76
print(x, ">=", 76, "=", hasil)

print("========= kurang dari sama dengan (<=)")
hasil = 75 <= 76
print(y, "<=", 76, "=", hasil)
hasil = y <= 25
print(y, "<=", 25, "=", hasil)

print("========== sama dengan sama dengan (==)")
hasil = 25 == 25
print(25, "==", 25, "=", hasil)
hasil = 25 == 26
print (25, "==", 26, "=", hasil)

print("=========== tidak sama dengan(!=)")
hasil = 75 != 76
print(75, "!=", 76, "=" , hasil )
hasil = 75 != 75
print(75, "!=", 75, "=", hasil)

print("=========== is (is)") 
hasil = 25 is 25
print(25, "is", 25, "=", hasil)
hasil = 25 is 24
print(25, "is", 24, "=", hasil)

print("========== is-not (is not)")
hasil = 75 is not 76
print(75, "is-not", 76, "=", hasil)
hasil = 75 is not 75
print(75, "is-not", 75, "=", hasil)







