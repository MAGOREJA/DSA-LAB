def SumIterative(number):
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total

def SumRecursive(number):
    if number == 0:
        return 0
    else:
        return number % 10 + SumRecursive(number // 10)

number = int(input("Give Number: "))

sum_iterative = SumIterative(number)
sum_recursive = SumRecursive(number)

print(f"Sum using iterative method: {sum_iterative}")
print(f"Sum using recursive method: {sum_recursive}")