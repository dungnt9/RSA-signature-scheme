import math
from hashlib import sha256

def coprime(a, b):
    # Kiểm tra hai số có nguyên tố cùng nhau hay không bằng thuật toán Euclid
    while b != 0:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    # Thuật toán Euclid mở rộng để tìm nghịch đảo modular
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def modinv(a, m):
    # Tính nghịch đảo modular của a theo modulo m
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('Nghịch đảo mod không tồn tại')
    return x % m

def is_prime(num):
    # Kiểm tra một số có phải là số nguyên tố hay không
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5) + 2, 2):
        if num % n == 0:
            return False
    return True

def hash_function(message):
    # Hàm băm sử dụng SHA-256 để băm thông điệp => băm thành 64 ký tự
    return sha256(message.encode("UTF-8")).hexdigest()
