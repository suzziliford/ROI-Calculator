# Convert the list below from Celsius to Farhenheit, using the map function with a lambda...
# F = (9/5)*C + 32

# (celsius *1.8) + 32
outp = [('Nashua', 89.6), ('Boston', 53.6), ('Los Angeles', 111.2), ('Miami', 84.2)]

# nums = [x for x in outp if isinstance(x, int)]

# print(nums())

# nums = filter_by_type(outp, int)
# strs = filter_by_type(outp, str)
# print(nums, strs)

# (100-32)/1.8

# a, b  = map(list, zip(*outp))
# print(a, b)

# a = [tup[1] for tup in outp]
# # a = (a - 32)/1.8 
# # print(a)
# list(map(lambda))

outp = list(map(lambda x: ((x[1] -32) //1.8), outp))
print(outp)

# print(list(map(lambda x, y: a,b((b-32)*1.8))))
# print(list(map(lambda x:  a,b((b-32)*1.8))))

# print(a,b)

# for x in b:
#     x = ((x-32)*1.8)
# print(x)


# output_list: [tuple(map(lambda x: x.split()[0]))]

# print(output_list)

# list(filter(lambda num: Ture if num > mean(random_nums) else False, random_nums))

# print [item for sublist in [[x] if x.isdigit() else list(x) for x in s.split(" ")] for item in sublist]
