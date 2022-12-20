# Write a recursion function to perform the fibonacci sequence up to the number passed in.

# Output for fib(5) => 
# Iteration 0: 0
# Iteration 1: 1
# Iteration 2: 1
# Iteration 3: 2
# Iteration 4: 3
# Iteration 5: 5
# Iteration 6: 8

# fib = [0,1,2,3,4,5,6,7,8]

    # # return_value = num
    # if num < 8:      
    #     return (fibonacci(num-1) + (num-2))
    # num = (2)

    # fibo_series = []

    # for i in range (0, num):
    #     fibo_series.append(fibonacci(i))
    # if num < 0:
    #     print("Incorrect input")
    # elif num < len(fib):
    #     return fib
    # else:
    #     fib.append(fibonacci (num - 1) + fib (num - 2))
    #     return fib 

    # nterms = 10

def fibonacci(num):
    if num <= 1:
        return num
    else:
        return (fibonacci(num-1) + fibonacci(num-2))

numbers = 8

if numbers <= 0:
    for i in range(numbers):
        print(f"Iteration {i}: {fibonacci(i)}")

fibonacci()

