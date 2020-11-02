# This was a function to manually add dictionary values,
# replace with loop to add from lists
def add_values_1(myDict):															
	# year, population, number of change, percent change
	myDict[1950] = [1322, 0, 0]
	myDict[1951] = [1585, 263, format((263/1585), '.0%')]
	return myDict

# This function tests the dictionary key
def test_dictionary_key(dict_key):	
	index = 0
	for x in dict_key:
		print(dict_key[index])
		index += 1 

# This function is the first one I built to print
# formatted outupt <----- replace with updated
def value_printer_1(myDict):
	for key, value in myDict.items():
		print(key, '\t', format(value[0], ',.0f'), '\t\t', \
					format(value[1], ',.0f'), '\t\t\t', value[2])



###################################################################
# Active functions:

# This function makes an empty dictionary.
def make_dictionary():
	my_dict = {}
	return my_dict

# This function makes the list of values that will populate
# the key for your dictionary.				
def key_list_maker():
	# set range to (start year, end year + 1), so 1950, 1990+1
	key_list = list(range(1950,1990+1))
#	print(key_list)			# uncomment to test
	return key_list

# This function turns the file object strings into floats:
def make_float(numbers):
    list_of_floats = []
    for item in numbers:
        list_of_floats.append(float(item))
    return list_of_floats

# THIS FUNCTION ADDS LISTS INTO AN EMPTY DICTIONARY
def add_lists(myDict, dict_key, numbers):

    for i in range(len(dict_key)):
        myDict[dict_key[i]] = [numbers[i], 0, 0]
    return myDict
	# This loop matches the key year with the population data
	# (names with professions)
#	for i in range(len(names)):
#		myDict[names[i]] = [professions[i], other[i], percent_change[i]]

    # This function adds the gross change in population numbers year-over-year.
#    myDict = calculate_population_change(myDict)

def calculate_population_change(myDict, dict_key):
#    for i in range(1, (len(dict_key))):
#        myDict[dict_key[i]] = [numbers[i], 0, 0]

#   print(key, '\t', format(value[0], ',.0f'), '\t', value[1], '\t\t', value[2])
    for i in range(1, (len(dict_key))):
        value[i] = 7
        myDict[key[i]] = [value[i], 0, 0]

    return myDict   


    # This function adds the percent change in population numbers year-over-year.
#    myDict = calculate_percent_change(myDict)

# def calculate_percent_change(myDict):



    # This function calculates the year with the lowest population change.
#    min_year, min_percent = calculate_min(myDict)

# def calculate_min(myDict):



    # This function calculates the year with the highest population change.
#    max_year, max_percent = calculate_max(myDict)

# def calculate_max(myDict):

    # This function calculates the average population change during this period.
#    average_change, average_percent = calculate_average_change(myDict)	
	
# def calculate_average_change(myDict):
	
	
	
	

def main():
    # Open USPopulation.txt, contains midyear population data from 1950 to 1990:
    # File object stuff
    infile = open(r'#', 'r')    # add link to USPopulationdata            

    # Make a file object.
    numbers = infile.readlines()

    # R strip the newlines from the file object
    with open(r'#') as f:       # add link to USPopulationdata
        alist = [line.rstrip() for line in f]

    # Call make_float to turn file object into a float.
    numbers = make_float(alist)

	# Call the function that makes a dictionary.
    myDict = make_dictionary()
	
	# Call to get the list that will be your dictionary's key values.
    dict_key = key_list_maker()
	
	# start with empty dictionary and dict key,
	# add the key values list to the dictionary with for loop
    myDict = add_lists(myDict, dict_key, numbers)

    # This function adds the gross change in population numbers year-over-year.
    myDict = calculate_population_change(myDict, dict_key)

    # This function adds the percent change in population numbers year-over-year.
#    myDict = calculate_percent_change(myDict)

    # This function calculates the year with the lowest population change.
#    min_year, min_percent = calculate_min(myDict)

    # This function calculates the year with the highest population change.
#    max_year, max_percent = calculate_max(myDict)

    # This function calculates the average population change during this period.
#    average_change, average_percent = calculate_average_change(myDict)

    ##############################################################################
    # Print Statements:                                                          #

    print('This chart contains US population data from 1950 to 1990:')
    print()
#    print('The year with the greatest population change was:', min_year, min_percent)            # list percent change
#    print('The year with the least change was:', max_year, max_percent)                          # list percent change
#    print('The average annual change over this period was:', average_change, average_percent)

    print()
    # heading:
    print('This is the full chart of values:')
    print('Year\tPopulation\tChange\t\t% Change')

    # Full chart of values
    for key, value in myDict.items():
        print(key, '\t', format(value[0], ',.0f'), '\t', value[1], '\t\t', value[2])

    # Close the file object
    infile.close()
			
main()


# Reference for R-stripping
# https://stackoverflow.com/questions/15233340/getting-rid-of-n-when-using-readlines



    # Some tests I gues:####################################################
	# For loop to print the keys (years) from the dictionary -- and
	# their list items (pop data, gross change, and % change, 
	# with values referenced by index)
	# UNCOMMENT TO SEE HOW FORMATTED DICT/LIST IS PRINTING :D
#	value_printer_1(myDict)
	
	# Uncomment to test the dictionary key
#	test_dictionary_key(dict_key)
    #######################################################################