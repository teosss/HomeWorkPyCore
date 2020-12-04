
file = open('zen.txt', 'r') # add file with zen python
zen = file.read() # read file
file.close() # close file
print(type(zen),"\n -----------") # type of variable 

# FIND WORDS IN THE TEXT
number_better = zen.find("better")
number_never = zen.find("never")
number_is = zen.find("is")

print("Better entered %d, number_never - %d, number_is - %d \n -----------" %(number_better,number_never,number_is))
print("Better entered %d, number_never - %d, number_is - %d \n -----------" %(zen.find("better"),zen.find("never"),zen.find("is"))) # v2 with no variables
print("Better entered {bet}, number_never - {nev}, number_is - {i} \n -----------".format(bet=number_better,nev=number_never,i=number_is)) # v3 with format

# END FIND WORDS

print(zen.upper(),"\n -----------") # upperCase ALL SYMBOLS

print(zen.replace("i","&"),"\n -----------") # replace symbols "i"

