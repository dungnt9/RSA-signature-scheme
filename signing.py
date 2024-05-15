from utils import hash_function

def sign_message(private_key, message):
    N, d = private_key
    hashed_message = hash_function(message)
    signature = [pow(ord(char), d, N) for char in hashed_message]
    return signature
