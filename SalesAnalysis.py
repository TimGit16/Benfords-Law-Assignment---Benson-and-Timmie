def load_sales_data():
    salesdata = []
    fileinput= input("Please enter the file name: ")
    if fileinput != "sales.csv":
        print("invalid file name")
    elif fileinput == "sales.csv":
        print("Valid file")
        return
    
    try:
        open("sales.csv" , "r")
        return False

    except:
        print("sales.csv does not exist ")
        
    
    with open("sales.csv" , "r"):
        for line in fileinput:
            salesdata.append(line) 




            