# def my_func(a, b):
#     print(f"b: {b}, a: {a}")
#     res = a + b
#     print(res)

# my_func(b=12, a=10)   

# def my_func():
#     return

# print(my_func())


def my_func(a, b):
    res = f"{a + b}"
    return res

ans = my_func(b=12, a=10)
print(type(ans))


