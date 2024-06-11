import random
from utils import is_prime, coprime, modinv

def generate_keypair(p, q):
    # Kiểm tra tính nguyên tố của p và q
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Cả 2 số p và q đều phải là số nguyên tố.')
    elif p == q:
        raise ValueError('2 số p và q phải khác nhau')

    # Tính N và phi(n)
    N = p * q
    phi = (p - 1) * (q - 1)

    # Chọn b ngẫu nhiên sao cho b và phi(n) nguyên tố cùng nhau
    b = random.randrange(1, phi)
    g = coprime(b, phi)
    while g != 1:
        b = random.randrange(1, phi)
        g = coprime(b, phi)

    # Tính nghịch đảo modular của b để lấy a
    a = modinv(b, phi)
    return ((N, b), (N, a))
