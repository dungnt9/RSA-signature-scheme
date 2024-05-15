import random
from utils import is_prime, coprime, modinv

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Cả 2 số p và q đều phải là số nguyên tố.')
    elif p == q:
        raise ValueError('2 số p và q phải khác nhau')

    N = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(1, phi)
    g = coprime(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = coprime(e, phi)

    d = modinv(e, phi)
    return ((N, e), (N, d))
