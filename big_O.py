# O(1) time complexity:
def multiply_no(n):
    return n*n

print(multiply_no(2))


# O(N) time complexity:
def items(n):
    for i in range(n):
        print(i)

items(10)


# Drop constants
def items(n):
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)

items(5)



# O(n^2) time complexity
def items(n):
    for i in range (n):
        for j in range (n):
            print(i,j)

items(8)

# if we have 3 value which is i,j,k then also the time complexity will be o(n^2)


# drop non dominant terms
def items(n):
    for i in range (n):
        for j in range (n):
            print(i,j)
    for k in range (n):
        print(k)

items(8)

#