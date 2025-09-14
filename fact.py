def fact(n):
    product = 1
    for i in range(1, n+1):
        product = product * i
    return product
print(fact(4))


