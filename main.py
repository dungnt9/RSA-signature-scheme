from key_generation import generate_keypair
from signing import sign_message
from verification import verify_signature
from utils import is_prime

def main():
    # Nhập số nguyên tố p từ người dùng và kiểm tra tính nguyên tố
    while True:
        p = int(input("Hãy nhập một số nguyên tố (vd. 17, 19, 23, v.v...): "))
        if is_prime(p):
            break
        else:
            print(f"Số {p} không phải là số nguyên tố. Hãy thử lại.")
    
    # Nhập số nguyên tố q từ người dùng, kiểm tra tính nguyên tố và phải khác p
    while True:
        q = int(input("Hãy nhập một số nguyên tố khác (Không phải số đầu tiên): "))
        if is_prime(q) and q != p:
            break
        elif not is_prime(q):
            print(f"Số {q} không phải là số nguyên tố. Hãy thử lại.")
        else:
            print("p và q phải khác nhau. Hãy thử lại.")

    # Tạo khóa công khai và khóa bí mật
    public_key, private_key = generate_keypair(p, q)
    print("Khóa Public là: ", public_key)
    print("Khóa Private là: ", private_key)

    # Hiển thị các bước tính toán
    print("\nThông tin các bước tính toán:")
    print(f"Chọn p = {p}, q = {q}")
    N = p * q
    phi = (p - 1) * (q - 1)
    b = public_key[1]
    a = private_key[1]
    print(f"Tính n = p * q = {p} * {q} = {N}")
    print(f"Tính φ(n) = (p-1) * (q-1) = {p-1} * {q-1} = {phi}")
    print(f"Chọn b ngẫu nhiên sao cho 1 < b < φ(n) và b nguyên tố cùng nhau với φ(n), được b = {b}")
    print(f"Tính a là nghịch đảo modular của b theo φ(n), được a = {a}")

    # Nhập thông điệp và ký thông điệp đó
    message = input("\nNhập thông điệp của bạn: ")
    print("Tin nhắn cần gửi: ", message)
    signature = sign_message(private_key, message)
    print("Chữ ký số: ", signature)

    # Xác thực chữ ký
    print("\nKiểm tra chữ ký...")
    verify_signature(public_key, signature, message)

if __name__ == "__main__":
    main()
