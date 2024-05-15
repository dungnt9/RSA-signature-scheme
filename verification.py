from utils import hash_function

def decrypt(public_key, signature):
    N, e = public_key
    decrypted_hash = ''.join([chr(pow(char, e, N)) for char in signature])
    return decrypted_hash

def verify_signature(public_key, received_signature, original_message):
    decrypted_hash = decrypt(public_key, received_signature)
    expected_hash = hash_function(original_message)

    if decrypted_hash == expected_hash:
        print("Xác thực thành công!")
    else:
        print("Xác thực thất bại!")
