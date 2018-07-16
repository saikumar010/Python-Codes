#Importing Libraries
import pandas as pd
import os

all_data=pd.DataFrame()
temp1=pd.DataFrame()
temp2=pd.DataFrame()

FL=os.listdir("**Path of files to be consolidated**")

for i in FL:
    temp1=pd.read_excel("**Path of files to be consolidated**"+i)
    temp2 = pd.concat([temp2,temp1], sort=False)

writer = pd.ExcelWriter("output file path\\file-name.xlsx", strings_to_urls=False)
temp2.to_excel("output file path\\file-name.xlsx", index=False)

