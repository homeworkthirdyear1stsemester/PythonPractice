import io

with open('a.txt', 'w') as f:
    f.write('test test')

with open('a.txt', 'r') as f:
    print(f.read())

f = io.BytesIO()
f.write(b'string io test')
f.seek(0)

print(f.read())
