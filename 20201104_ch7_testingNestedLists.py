list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for list in list_of_lists:
                                        # Sequentially access each `list`
    for element in list:
                                        # Sequentially access each `element`
        print(element)


# The reason why this is not helpful is that
# it iterates through EVERY element in the nested list
# I only want to access **some** of the elements.

# https://www.kite.com/python/answers/how-to-iterate-through-a-nested-list-in-python