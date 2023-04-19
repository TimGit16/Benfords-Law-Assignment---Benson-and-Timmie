import matplotlib.pyplot as plt
import os 
def createfile():
    filepath = os.getcwd()
    filename = "results.csv"

    filecreate = filepath + filename 

    open(filecreate , "a")
        #------

def graph():
    x_numbers = [ 1 , 2 , 3 , 4 , 5 , 6 ,7 , 8 , 9, 0 ]

    plt.title(" Benford's Law distribution for sales data")
    plt.xlabel(" first digit")
    plt.ylabel(" Frequency") 

    
