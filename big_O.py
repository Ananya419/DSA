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

# Space complexity

"""

# Different terms for input - Add vs Multiply

def items(n):
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)

items(4)

# it has O(n) time complexity because O(n) + O(n) = O(2n) we will drop the constant value so it has  O(n) time complexity
def items(a,b):
    for i in range(a):
        print(i)

    for j in range(b):
        print(j)
# It has O(a+b)


def items(a,b):
    for i in range (a):
        for j in range (b):
            print(i,j)
#It has O(a*b) time complexity because we are doing a for each time of doing b

"""