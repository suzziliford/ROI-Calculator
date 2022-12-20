# Write an anonymous function that sorts this list by the last name...
# Hint: Use the ".sort()" method and access the key"

Output: ['Victor aNisimov', 'Gary A.J. Bernstein', 'Joel Carter', 'Andrew P. Garfield', 'David hassELHOFF']

def sort_names ():
    output_list = ['Victor aNisimov', 'Gary A.J. Bernstein', 'Joel Carter', 'Andrew P. Garfield', 'David hassELHOFF']
# for names in output:
    # for x in output_list.items:
    #     x.split
        

    # output_list == sorted(output_list)
    # output_list = [x.title() for x in output_list]
    # for x in output_list:
    #     x.split()[-1]



    # for x in output_list:
    #     str.capitalize(x)
    output_list = [x.title() for x in output_list]
    output_list.sort(key=lambda x: x.split()[-1])

    # output_list = [b for pairs, b in output_list()  if pairs == 'types']
    # for element in output_list:
    #     print(element, end=' ')
    print (output_list)

    # x = sorted(output_list)[-2]
    # print (x)






sort_names()