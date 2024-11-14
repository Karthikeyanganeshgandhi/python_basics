# reading in zip file

# import zipfile
# with zipfile.ZipFile("new_text.zip","w")as f:
#     f.write("new_csv1.csv")
#     f.write("new_csv2.csv")

# import zipfile
# with zipfile.ZipFile("new_text.zip","r")as f:
#     f.extractall("documents")
#     list1=f.namelist()
#     print(list1)

# import zipfile
# with zipfile.ZipFile("new_file.zip","w")as f:
    # f.write("my_program.csv")
    # f.write("my_program1.csv")

import zipfile
with zipfile.ZipFile("new_file.zip","r")as f:
    f.extractall("my info")
    operation=f.namelist()
    print(operation)