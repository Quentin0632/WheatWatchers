"""
create a CSV file out of an array
"""
import csv

def arrayToCSV(file,header,data):  
    with open(file, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
    
        # write the header
        writer.writerow(header)
    
        # write multiple rows
        writer.writerows(data)



"""    EXEMPLE OF HEADER AND DATA

header = ['name', 'area', 'country_code2', 'country_code3']
data = [
        ['Albania', 28748, 'AL', 'ALB'],
        ['Algeria', 2381741, 'DZ', 'DZA'],
        ['American Samoa', 199, 'AS', 'ASM'],
        ['Andorra', 468, 'AD', 'AND']s,
        ['Angola', 1246700, 'AO', 'AGO']
       ]

"""