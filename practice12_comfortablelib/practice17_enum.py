import enum


class Perm(enum.IntFlag):
    R = 4
    W = 2
    X = 1


print(Perm.R | Perm.W)
print(repr(Perm.R | Perm.W))

# db = {
#     'stack1': 1,
#     'stack2': 2
# }


# STATUS_ACTIVE = 1
# STATUS_INACTIVE = 2
#
# if db['stack1'] == STATUS_ACTIVE:
#     print('shutdown')
# elif db['stack1'] == STATUS_INACTIVE:
#     print('terminate')
#
# @enum.unique  # 같은 값이 존재 하지 않는다는 것을 보장을 해 주는 어노테이션
# class Status(enum.Enum):
#     ACTIVE = 1
#     # RENAME_ACTIVE = 1
#     INACTIVE = 2
#     RUNNING = 3


# IntEnum 일 경우 Status.ACTIVE == 1 하면 True 가 나온다
# print(Status.ACTIVE)
# print(repr(Status.ACTIVE))
# print(Status.ACTIVE.value)
#
# for s in Status:
#     print(s)
#     print(type(s))
#
# print(Status(1))

# if Status(db['stack1']) == Status.ACTIVE:
#     print('shutdown')
# elif Status(db['stack1']) == Status.INACTIVE:
#     print('terminate')
