# O(1) time complexity:
def multiply_no(n):
    return n*n

print(multiply_no(2))


# O(N) time complexity:
def items(n):
    for i in range(n):
        print(i)

items(10)