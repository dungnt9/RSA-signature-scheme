from utils import hash_function

def decrypt(public_key, signature):
    N, b = public_key  # Khóa công khai (n, b)
    # Giải mã chữ ký sử dụng khóa công khai
    decrypted_hash = ''.join([chr(pow(char, b, N)) for char in signature])
    return decrypted_hash

def verify_signature(public_key, received_signature, original_message):
    # Giải mã chữ ký để lấy giá trị băm của thông điệp gốc
    decrypted_hash = decrypt(public_key, received_signature)
    # Băm lại thông điệp gốc
    expected_hash = hash_function(original_message)

    # So sánh giá trị băm của thông điệp gốc và giá trị băm đã giải mã từ chữ ký
    if decrypted_hash == expected_hash:
        print("Xác thực thành công!")
    else:
        print("Xác thực thất bại!")
