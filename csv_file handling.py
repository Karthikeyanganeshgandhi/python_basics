# import csv
# with open("survey.csv","w",newline='')as f:
#     writer=csv.writer(f)
#     writer.writerow(["name"," age"," place"])
#     writer.writerow(["aswin"," 20"," alpy"])
#     writer.writerow(["akash"," 23"," alpy"])

# # for read this file 
  
# f=open("survey.csv","r")
# reader=csv.reader(f)
# for r in reader:
#     print(r)

import csv
with open("food item.csv","w",newline='')as f:
    writer=csv.writer(f)
    writer.writerow(["itm.no.","  food","  rate"])
    writer.writerow(["1","  porotta","  10-1"])
    writer.writerow(["2","  biriyani","  80"])
    writer.writerow(["3","  mandhi","  900"])
    writer.writerow(["4","  pathiri","  10"])


f=open("food item.csv","r")
reader=csv.reader(f)
for r in reader:
    print(r)
