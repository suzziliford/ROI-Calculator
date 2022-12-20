# Create a generator that takes a number argument and yields that number squared, then prints each number squared until zero is reached.

# def my_gen(number):
#     pass
# def num in my_gen(10)
#     print(num)


def num_in_my_gen():
    num = 0
    while True:
        yield num
        num += num**2
        print(num)
    
.......

num_in_my_gen()

# gen = infinite_sequence()
# next(gen)

