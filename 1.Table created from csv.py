import pandas as pd
import sql,csv,sqlite3

'''
#for replacing extra comma present in supplier column which shows error in table creation so the below code is written 
s=pd.read_csv("C:/Users/admin/Downloads/samples.csv - sample_inventory.csv")
s['supplier']=s['supplier'].str.replace(",","")
s.to_csv('outputfile2.csv', 
                 index = False)

'''
#Table creation
conn=sqlite3.connect('connect_to_python1.db')

print("Opened database successfully")



conn.execute(
        '''CREATE table vizag_company091
         (code CHAR,
         name  CHAR,
         batch CHAR,
         stock CHAR,
         deal CHAR,
         free CHAR,
         mrp CHAR,
         rate CHAR,
         exp CHAR,
         company CHAR,
         supplier CHAR
         );''')

print("Table created successfully")
cursor=conn.cursor()
with open("C:/Users/admin/Desktop/dds/outputfile2.csv","r") as file:
    no=0
    for row in file:
        cursor.execute("INSERT INTO vizag_company091  VALUES(?,?,?,?,?,?,?,?,?,?,?)",row.split(","))
        conn.commit()
        no+=1
conn.close()
print("created")
print('record transfered')
# Table created
