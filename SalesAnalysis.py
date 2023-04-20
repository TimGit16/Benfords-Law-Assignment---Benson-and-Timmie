import os
import matplotlib.pyplot as plt
import numpy as np
print(os.getcwd())
folder = os.getcwd()

def load_sales_data():
    while True:
        csvName = "sales.csv"
        fileinput = input("Please enter your file name (eg. sales.csv): ")
        if os.path.isfile(folder+"\\"+fileinput):
            if fileinput != csvName:
                print("Invalid File Name")
            elif fileinput == csvName:
                print("Valid File")
                # fileName = folder + "\\" + csvName
                with open(fileinput) as file:
                    salesData = file.read() # Assigns all the text from sales.csv to variable as a string
                    salesData = salesData.splitlines() # Splits lines marked by \n to create a list wihtout \n
                    salesData.pop(0) # Removes "Postal Code, Sales" line
                    for i in range(len(salesData)): # Iterates through salesList to make each item be only the number after the comma
                        salesData[i] = salesData[i].split(",")[1] # Replaces item at index i to be the second item after splitting with delimiter ,
                return salesData
        else:
            print("File Does Not Exist In Current Working Directory")

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
    print("The first digit frequency for",digit,"is:",str(digFreqCalc(digCount(digit)))+"%") # prints digit frequency of parameter value digit

def graph():
    x_numbers = []
    y_numbers = []
    for n in range(1,10):
        x_numbers.append(str(n))
        y_numbers.append(digFreqCalc(digCount(n)))

    fig, ax = plt.subplots()
    bar_container = ax.bar(x_numbers, y_numbers)
    ax.set(xlabel = "Digit", ylabel='Frequency (%)', title="Benford's Law First Digit Frequency")
    ax.bar_label(bar_container)

    plt.show()


def createfile():
    resultName = folder + "\\results.csv"
    try: 
        resultFile = open(resultName, "a")
        resultFile.write("Digit,Frequency\n")
        resultFile.close()
    except:
        resultFile = open(resultName, "w")
        resultFile.write("Digit,Frequency\n")
        resultFile.close()

    yList = []
    xList = []
    for num in range(1,10): # iterates through numbers 1 to 9 and prints their first digit frequency
        xList.append(str(num))
        yList.append(digFreqCalc(digCount(num)))

    for item in range(len(xList)):
        resultFile = open(resultName, "a")
        resultFile.write(xList[item] + "," + str(yList[item])+"\n")
    resultFile.close()

def printMenu():
    print ('''
            Sales Fraud Check \n 
            1. Load Data \n
            2. Benford's Law Compliance Check \n
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

salesList = load_sales_data()
while userInput != exitCondition:
    printMenu()
    userInput = input()

    if userInput == loadDataOption:
        salesList = load_sales_data()

    elif userInput == BLCOption:
        for num in range (1,10):
            reportFreq(num)
        if 29 <= digFreqCalc(digCount(1)) <= 32:
            print("This data set is likely not to be fraudulent")
        else:
            print("This data set is likely to be fraudulent")

    elif userInput == showGraphOption:
        graph()

    elif userInput == exportDataOption:
        createfile()
        
    elif userInput != exitCondition: 
        print(" Please type in a valid option (A number from 1-9)")

print("Program Terminated")