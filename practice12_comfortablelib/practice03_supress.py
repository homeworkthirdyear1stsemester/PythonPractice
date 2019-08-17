import contextlib
import os

try:
    os.remove('somefile.tmp')
except FileNotFoundError:
    pass

with contextlib.suppress(FileNotFoundError):  # 위 코드와 동일 -> 깔끔하게 코드 작성 가능
    os.remove('somefile.tmp')
