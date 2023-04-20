import os
print(os.getcwd())
folder = os.getcwd()
fileName = folder + "sales.csv"
file = open(fileName, "r")

def load_sales_data():
    salesdata = []
    fileinput = input("Please enter your file name: ")
    if fileinput != "sales.csv":
        print("invalid file name")
    elif fileinput == "sales.csv":
        print("Valid file")
        return
    
    
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


import matplotlib.pyplot as plt
import os 

def graph():

    fig, ax = plt.subplots()
    bar_container = ax.bar(first, mph_speed)
    ax.set(ylabel='Frequency (%)', title='First Digit', ylim=(0, 80))
    ax.bar_label(
    bar_container, fmt=lambda x: '{:.1f} km/h'.format(x * 1.61)
    x_numbers = []
    y_numbers = []

    for num in (1,10):
        x_numbers.append(str(num))
        y_numbers.append(digFreqCalc(digCount(num)))


    a = plt.plot(x_numbers, y_numbers)

    plt.title(" Benford's Law First Digit Frequency")
    plt.xlabel(" first digit")
    plt.ylabel(" Frequency (%)") 

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
showGraph = "3"
exportDataOption = "4"
exitCondition = "9"