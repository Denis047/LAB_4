m = 7
n = 10
two_dim_array = [[i * j for j in range(n)] for i in range(m)]

del two_dim_array[1]

for row in two_dim_array:
    del row[1]
element_m11 = two_dim_array[0][0]
element_m14 = two_dim_array[0][3]

print(f"\nЕлемент m11: {element_m11}")
print(f"Елемент m14: {element_m14}")

elements_m11_to_m14 = [row[0:4] for row in two_dim_array]


def factorial(n):
    if n < 0:
        return -1
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


print(factorial(5))
