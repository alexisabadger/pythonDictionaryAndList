# Name: E. A. McIntire
# Date: 2020 November 1

# NOTE: I was able to get it to display a list of values
# I haven't figured out yet how to get it to do the calculation
# and put the value in value[1] of the list in the dictionary.


# Exercise 7.9 - Population Data

# If you have downloaded the source code you will find a file 
# named USPopulation.txtPreview the document in the Chapter 07 folder. 
# The file contains the midyear population of the United State, in thousands, 
# during the years 1950 through 1990. The first line in the file contains the 
# population for 1950, the second line contains the population for 1951, 
# and so forth.

# Write a program that reads the file's contents into a list. The program 
# should display the following data:

# The average annual change in population during the time period
# The year with the greatest increase in population during the time period
# The year with the smallest increase in population during the time period  



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

# def calculate_population_change(myDict, dict_key):
#    for i in range(1, (len(dict_key))):
#        myDict[dict_key[i]] = [numbers[i], 0, 0]

#    for year in myDict:
#        if year != 1950:
        #Calculate the difference in population of two consecutive years.
#            myDict[year][1] = myDict[year][0]-myDict[str(int(year)-1)][0]

        #Calculate the difference as a percentage
#            myDict[year][2] = (1-myDict[year][1]/myDict[str(int(year)-1)][1])*100
#    return myDict

#   print(key, '\t', format(value[0], ',.0f'), '\t', value[1], '\t\t', value[2])
#    for i in range(1, (len(dict_key))):
#        value[i] = 7
#        myDict[key[i]] = [value[i], 0, 0]
  


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
#    myDict = calculate_population_change(myDict, dict_key)

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