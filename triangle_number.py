def triangle_number(n):

    if n == 1:
        return 1

    else:
        return n + triangle_number(n - 1)

print(triangle_number(5))