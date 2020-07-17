import datetime 
def date_validation(day, month, year): 
    isValidDate = True
    try: 
        datetime.datetime(int(year), int(month), int(day)) 
    except ValueError: 
        isValidDate = False
    if(isValidDate): 
        print ("Yes") 
    else: 
        print ("No")
date_validation(10,12,2020)  
date_validation(31,4,2020) 