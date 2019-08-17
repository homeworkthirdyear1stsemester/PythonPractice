import string
import random
from Crypto.Cipher import AES

key = ''.join(random.choice(string.ascii_letters) for _ in range(AES.block_size))  # radom으로 문자열 을 가진다
iv = ''.join(random.choice(string.ascii_letters) for _ in range(AES.block_size))  # 초기 백터

with open('plaintext', 'r') as f, open('enc.dat', 'wb') as e:
    printtext = f.read()
    cipher = AES.new(key, AES.MODE_CBC, iv)  # 암호화 하는 코드 생성
    padding_length = AES.block_size - len(printtext) % AES.block_size
    printtext += chr(padding_length) * padding_length
    cipher_text = cipher.encrypt(printtext)  # 암호화 코드 생성
    e.write(cipher_text)

with open('enc.dat', 'rb') as f:
    cipher2 = AES.new(key, AES.MODE_CBC, iv)
    decrypted_text = cipher2.decrypt(f.read())
    print(decrypted_text[:-decrypted_text[-1]].decode('utf-8'))  # padding 만큼 빼준 문자열
