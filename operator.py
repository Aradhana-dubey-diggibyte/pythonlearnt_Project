#arithematic 
a = 10
b = 3

print("Addition:", a + b)        # 13
print("Subtraction:", a - b)     # 7
print("Multiplication:", a * b)  # 30
print("Division:", a / b)        # 3.333...
print("Floor Division:", a // b) # 3
print("Modulus:", a % b)         # 1
print("Exponentiation:", a ** b) # 1000

#Comparison
x = 5
y = 10
print("x == y:", x == y)   # False
print("x != y:", x != y)   # True
print("x > y:", x > y)     # False
print("x < y:", x < y)     # True
print("x >= y:", x >= y)   # False
print("x <= y:", x <= y)   # True

#logical
a = True
b = False
print("a and b:", a and b)   # False
print("a or b:", a or b)     # True
print("not a:", not a)       # False

#Assignment
num = 10
num += 5
print("After += :", num)     # 15
num -= 3
print("After -= :", num)     # 12
num *= 2
print("After *= :", num)     # 24
num /= 4
print("After /= :", num)     # 6.0
num %= 5
print("After %= :", num)     # 1.0

#Identity
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print("x is y:", x is y)     # True
print("x is z:", x is z)     # False
print("x == z:", x == z)     # True

#Membership 
items = [1, 2, 3, 4, 5]

print("3 in items:", 3 in items)     # True
print("6 not in items:", 6 not in items) # True

#Bitwise 
a = 5    # 0101
b = 3    # 0011

print("a & b:", a & b)   # 1
print("a | b:", a | b)   # 7
print("a ^ b:", a ^ b)   # 6
print("~a:", ~a)         # -6
print("a << 1:", a << 1) # 10
print("a >> 1:", a >> 1) # 2



