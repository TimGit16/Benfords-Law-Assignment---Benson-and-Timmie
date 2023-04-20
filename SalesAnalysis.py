import os
import matplotlib.pyplot as plt
print(os.getcwd())
folder = os.getcwd()
fileName = folder + "sales.csv"
file = open(fileName, "r")

def load_sales_data():
    salesdata = []
    fileinput = input("Please enter the file name: ")
    if fileinput != "sales.csv":
        print("invalid file name")
    elif fileinput == "sales.csv":
        print("Valid file")
        return salesList
    
    
    with open("sales.csv" , "r"):
        for line in fileinput:
            salesdata.append(line) 



salesList = file.read() # Assigns all the text from sales.csv to variable as a string
salesList = salesList.splitlines() # Splits lines marked by \n to create a list wihtout \n
salesList.pop(0) # Removes "Postal Code, Sales" line
for i in range(len(salesList)): # Iterates through salesList to make each item be only the number after the comma
    salesList[i] = salesList[i].split(",")[1] # Replaces item at index i to be the second item after splitting with delimiter ,


def digCount(num):
    '''
    Parameter: num, should be a single digit number
    Function: Takes in a number and counts how many times it occurs as the first digit in salesList
    Return: Returns numcount, the number of times num is the first digit
    '''
    numcount = 0 # Creates numcount variable
    for j in salesList: # iterates through salesList
        if j[0] == str(num): # compares the first character of item and value parameter
            numcount += 1 # if equivalent add one to numcount
    return numcount # returns the final value of numcount

def digFreqCalc(count):
    '''
    Parameter: count, should be a number representing how many times a first digit occurs
    Function: Calculates the frequency of a first digit's occurence in salesList as a percentage
    Return: Returns the frequency
    '''
    return round(count/len(salesList)*100, 1) # returns the frequency of a digit as percentage in a string

def reportFreq(digit):
    '''
    Parameter: digit, should be a single digit
    Function: Prints out the frequency of digit in a sentence including its percentage
    '''
    print("The first digit frequency for",digit,"is:",str(digFreqCalc(digCount(digit))))+"%" # prints digit frequency of parameter value digit

for k in range(1,10): # iterates through numbers 1 to 9 and prints their first digit frequency
     reportFreq(k)

file.close()

def graph():

    x_numbers = []
    y_numbers = []

    fig, ax = plt.subplot()
    
    for num in (1,10):
        x_numbers.append(str(num))
        y_numbers.append(digFreqCalc(digCount(num)))


    a = plt.plot(x_numbers, y_numbers)
    bar_container = ax.bar(x_numbers, y_numbers)

    plt.title(" Benford's Law First Digit Frequency")
    plt.xlabel(" first digit")
    plt.ylabel(" Frequency (%)") 
    plt.bar_label(bar_container)


    plt.hist(a)


def createfile():
    filepath = os.getcwd()
    filename = "\results.csv"

    filecreate = filepath + filename 

    open(filecreate , "a")
    filecreate.append(graph)

def printMenu():
    print ('''
            Sales Fraud Check \n 
            1. Load Data \n
            2. Benford's Law Compliance Check
            3. Show Graph \n
            4. Export Data \n
            9. Quit \n
            Enter Menu Option (1-9)
            ''')

userInput = ""
loadDataOption = "1"
BLCOption = "2" 
showGraphOption = "3"
exportDataOption = "4"
exitCondition = "9"

while userInput != exitCondition:
    printMenu()

    userInput = input()

    if userInput == loadDataOption:
        salesList = load_sales_data()

    elif userInput == BLCOption:
        for num in range (1,10):
            reportFreq(num)

    elif userInput == showGraphOption:
        x_numbers = []
        y_numbers = []

        for num in range (1,10):
            x_numbers.append(str(num))
            y_numbers.append(digFreqCalc(digCount(num)))

        graph()

    elif userInput == exportDataOption:
        exportData()

    elif userInput == exitCondition:
        continue

    else: print(" Please type in a valid option (A number from 1-9)")

