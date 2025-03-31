# def factorial(n):
#     # Base case
#     if n == 0 or n == 1:
#         return 1
#     # Recursive case
#     else:
#         return n * factorial(n - 1)

# print(factorial(4))

# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 

# def fibonacci_recursive(n):
#     if n == 0:
#         return []
#     elif n == 1:
#         return [0]
#     elif n == 2:
#         return [0, 1]
#     else:
#         sequence = fibonacci_recursive(n - 1)
#         sequence.append(sequence[-1] + sequence[n-2])
#         return sequence

# print(fibonacci_recursive(6))

# def fib(n):
#     if n <= 1:
#         return n
#     while(n>=1):
#         n = n -1
#         print( ( fib(n-1) + fib(n-2)))
    
    
# print(fib(6))      