import pandas as pd
#enter in the correct filename to sort
orig_file = input("What file do you want to sort? Include the file extension. \n")
xlsx = pd.ExcelFile(orig_file)
sheet1 = xlsx.parse(0)

OS_type = input("What is the OS type? Case sensitive \n\n")

sheet1['gene'] = (
    sheet1['description']
    .str.split('OS=' + OS_type).str[1]
    .str.split().str[0]
)

sortedsheet = sheet1.sort_values('gene')

#enter in the desired filename to output
writer = pd.ExcelWriter("sorted_" + orig_file)
sortedsheet.to_excel(writer,'Sheet1')
writer.save()

print('\n The sorting is now done!')