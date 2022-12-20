# Exercise #1
# Filter out all of the empty strings from the list below

# Output: ['Argentina', 'San Diego', 'Boston', 'New York']

def alph_order ():
    places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]
    # print("Original list is : " + str(places))
    # while (" " in places):
    #     places.remove(" ")
    # print("Modified list is : " + str(places))

    # places = list(filter(None, places))
    # print("Modified list is : " + str(places))
    
    take_away = lambda x: len(x)>2

    places = list(filter(take_away, places))
    print(places)

    # for x in str(places):
    #     if x
    
    # for x in len(str(places)):
    #     if x > 2:
    #         places.remove

    # print(str(places))

    # places = [i for i in places if i]
    # print(str(places))


    # places = list(filter(None, places))
    # print (str(places))

alph_order()


    