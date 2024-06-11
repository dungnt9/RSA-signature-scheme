from utils import hash_function

def sign_message(private_key, message):
    N, a = private_key  # Khóa bí mật (n, a)
    hashed_message = hash_function(message)  # Băm thông điệp
    # Ký từng ký tự của thông điệp băm bằng khóa bí mật
    signature = [pow(ord(char), a, N) for char in hashed_message]
    return signature
