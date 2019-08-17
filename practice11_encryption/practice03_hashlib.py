import base64
import os
import hashlib

# print(hashlib.sha256(b'password').hexdigest())  # sha 알고리즘으로 표현
# print(hashlib.sha256(b'password').hexdigest())  # sha 알고리즘으로 표현

# 복원을 못하도록 하는 것
# 같은 문자열을 넣을경우 같은 결과가 나온다

# -> web 사이트에서 user 로그인 할 때 많이 쓰인다

user_name = 'user1'
user_pass = 'password'
db = {}

salt = base64.b64encode(os.urandom(32))

print(salt)  # 하나의 암호화


# salt값을 알지 못할 경우 hash table이 있더라도 알 수 없다 그러므로 암호화 할때 같이 쓰인다

def get_digest(password):
    password = bytes(user_pass, 'utf-8')
    digest = hashlib.sha256(salt + password).hexdigest()
    for _ in range(10000):
        digest = hashlib.sha256(bytes(digest, 'utf-8')).hexdigest()  # 다시 digest 하므로 10000이라는 값도 알아야 하므로 보안성 높아진다
    print(digest)

    return digest


digest = hashlib.pbkdf2_hmac('sha256', bytes(user_pass, 'utf-8'), salt, 10000)  # 위 코드를 실행하는 라이브러리

print("함수 실행 :", digest)

db[user_name] = get_digest(user_pass)


def is_loggin(user_name, password):
    return get_digest(password) == db[user_name]


print(is_loggin(user_name, user_pass))
