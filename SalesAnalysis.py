def load_sales_data():
    salesdata = []
    fileinput= input("Please enter you file name: ")
    if fileinput != "sales.csv":
        print("invalid file name")
    elif fileinput == "sales.csv":
        print("Valid file")
        return
    
    
    with open("sales.csv" , "r"):
        for line in fileinput:
            salesdata.append(fileinput) 

            