def factorial(n):
    result = n
    for i in range(1,n):
        result *=i
    return result



    def factorial(m):
        if m == 1:
            return 1
        else:
            return m * factorial(m-1)
