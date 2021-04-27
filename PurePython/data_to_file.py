import pprint

def display_categories(out=False):
    '''
    Show the categories\n
    out: True or False, print out the references
    '''
    ref_cat_value = [(0, "salary"),
                     (1, "fixed - must pay"),
                     (2, "saving"),
                     (3, "food"),
                     (4, "beverage"),
                     (5, "flower"),
                     (6, "transport"),
                     (7, "shopping"),
                     (8, "others")]
    if out == True:
        pprint.PrettyPrinter().pprint([i for i in ref_cat_value])
    return ref_cat_value



def write_data(txtfile):
    '''
    Input and write new data to designated file\n
    txtfile: designated file 
    '''
    with open(txtfile, "a+") as f:
        correct_input = True
        while correct_input:
            try:
                expense = float(input("Enter the amount:"))
                category = int(input("Enter the category:"))
                date = int(input("Enter the date:"))
                description = str(input("Enter additional description:"))
                if category in range(10) and date in range(32):
                    correct_input = False
            except:
                print("Wrong input type. Please enter again. Refer to DEFINITIONS.")
        
        ref_cat_value = display_categories()
        for i in ref_cat_value:
            if i[0] == category:
                cat_explain = i[1]
        if category == 0:
            input_format = f"\n{expense},{category},{cat_explain},{date},{description}"
        else:
            input_format = f"\n{-expense},{category},{cat_explain},{date},{description}"
        f.write(input_format)
        print("Data added.")