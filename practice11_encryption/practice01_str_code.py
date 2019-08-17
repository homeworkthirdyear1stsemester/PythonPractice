import string
import random
from Crypto.Cipher import AES

print("size :", AES.block_size)
print(string.ascii_letters)
key = ''.join(random.choice(string.ascii_letters) for _ in range(AES.block_size))  # radom으로 문자열 을 가진다
print("random data :", key)

iv = ''.join(random.choice(string.ascii_letters) for _ in range(AES.block_size))  # 초기 백터

printtext = 'afdsafasdfasdfdasfasfasfasf'

cipher = AES.new(key, AES.MODE_CBC, iv)  # 암호화 하는 코드 생성
padding_length = AES.block_size - len(printtext) % AES.block_size
printtext += chr(padding_length) * padding_length
cipher_text = cipher.encrypt(printtext)  # 암호화 코드 생성
print(cipher_text)

cipher2 = AES.new(key, AES.MODE_CBC, iv)
decrypted_text = cipher2.decrypt(cipher_text)

print(decrypted_text)
print(decrypted_text[-1])
print(decrypted_text[:-decrypted_text[-1]])  # padding 만큼 빼준 문자열
