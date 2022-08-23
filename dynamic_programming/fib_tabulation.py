def fib_tab(n):
    # 코드를 작성하세요.
    fib_cache = {}

    for i in range(1, n + 1):
        if i < 3:
            fib_cache[i] = 1

        else:
            fib_cache[i] = fib_cache[i - 1] + fib_cache[i - 2]

    return fib_cache[n]

# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))