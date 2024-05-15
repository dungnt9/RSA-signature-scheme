from key_generation import generate_keypair
from signing import sign_message
from verification import verify_signature

def main():
    p = int(input("Hãy nhập một số nguyên tố (17, 19, 23, v.v...): "))
    q = int(input("Hãy nhập một số nguyên tố khác (Không phải số đầu tiên): "))

    public_key, private_key = generate_keypair(p, q)
    print("Khóa Public là: ", public_key)
    print("Khóa Private là: ", private_key)

    message = 'Lớp Toán tin K63'
    print("Tin nhắn cần gửi: ", message)
    signature = sign_message(private_key, message)
    print("Chữ ký số: ", signature)

    print("Kiểm tra chữ ký...")
    verify_signature(public_key, signature, message)

if __name__ == "__main__":
    main()
