import sqlite3
from datetime import datetime
connection_obj = sqlite3.connect('connect_to_python1.db')

# cursor object
cursor_obj = connection_obj.cursor()

# to select all column we will use
statement ="Select name1 from vizag_company091"

cursor_obj.execute(statement)
list_to_Add_name=[]
empty_dict_to_add_name={}
print("All the data")
output = cursor_obj.fetchall()
for row in output:
    medicine_name=list(row)
    for i in medicine_name:
      list_to_Add_name.append(i)

for names in range(len(list_to_Add_name)):
       empty_dict_to_add_name[names]=list_to_Add_name[names]


print("empty_dict_to_add_name",empty_dict_to_add_name)#importing name from the database using dictionary  

statement2="Select expe from vizag_company091"
cursor_obj.execute(statement2)
output2 = cursor_obj.fetchall()
ex=[]

expiry_date_iu={}
for row2 in output2:
       expiry_date=list(row2)
       for j in expiry_date:
              ex.append(j)
for non in range(len(ex)):
       expiry_date_iu[non]=ex[non]
       
print("expiry_date_iu",expiry_date_iu)#importing expiry date from the database using dictionary  

statement10="Select batch from vizag_company091"     
cursor_obj.execute(statement10)
output21 = cursor_obj.fetchall()
batch_io=[]
batch_oo={}
for row4 in output21:
       ba=list(row4)
       for i in ba:
              batch_io.append(i)
for po in range(len(batch_io)):
       batch_oo[po]=batch_io[po]
print("batch",batch_oo)#importing batch from the database using dictionary 

final={}

for kt in expiry_date_iu:
    if kt in empty_dict_to_add_name:#mapping on the id basis and resulting output name and expiry date
        final[empty_dict_to_add_name[kt]]=expiry_date_iu[kt]

print("name and expiry date",final)

ssas=datetime.now()
dasas={}
val=''

#expiry date 


for kp,val in final.items():
    #import pdb;pdb.set_trace()
    x=ssas if val=='/  /' else datetime.strptime(val,"%d/%m/%Y")
    #x=datetime.strptime(datetime.strptime(val1,"%d/%m/%Y"),"%d/%m/%Y")
    if(x>ssas):
        final[kp]="Date not expired"
    
    elif(x<ssas):
        final[kp]="Date expired"
    
    else:
        final[kp]="Date not mentioned"

print("Expiry date of the items",final)#it shows  expired or not


#ascending or descending order

das=input("Enter asc or desc")#only accepts asc or desc
ascen=[]
statement3="Select name1 from vizag_company091 order by name1 "+str(das)+""
cursor_obj.execute(statement3)
output3 = cursor_obj.fetchall()
for asc in output3:
       ascending=list(asc)
       for o in ascending:
              ascen.append(o)
print("ascen",ascen)




#aggregation


statement99="Select stock from vizag_company091"

aggr=[]
#cursor_obj.execute(statement9)
cursor_obj.execute(statement99)
#cursor_obj.execute(statement999)
output99=cursor_obj.fetchall()

for der in output99:
    ads=list(der)
    for jiu in ads:
        aggr.append(jiu)
#print(aggr)

'''
statement999="Select company from vizag_company091"       
cursor_obj.execute(statement999)
output999=cursor_obj.fetchall()

ba=[]
for der in output999:
    adi=list(der)
    for ji in adi:
        ba.append(ji)
#print("ba",ba)
import pandas as pd
aggerate={"batch_details":batch_io,"stocks_available":aggr,"company_details":ba}
seana=pd.DataFrame(aggerate)
#seana2=aggerate.group_by(["batch_details","stocks_available"])
print("seana2",seana)
'''
statement910="Select company,stock from vizag_company091 group by stock"       
cursor_obj.execute(statement910)
sasfa={}
output999=cursor_obj.fetchall()
for kalm in output999:
    #import pdb;pdb.set_trace();
    sasfa[kalm[0]]=kalm[1]
#k=[val for kop in sasfa for val in kop]
print("sasfa",sasfa)
supplier=input("Please enter supplier name: ")
value=None
for kty,valty in sasfa.items():
    if supplier==kty:
        print("supplier current stock is",valty)

    
#api pagination(if django used it will work perfectly but for python little remains hard)
statement_all="Select * from vizag_company091"
cursor_obj.execute(statement_all)
output0001=cursor_obj.fetchall()
sade=None
lisuy=[]
for reg in output0001:
    sade=list(reg)
    lisuy.append(sade)
print("lisuy",lisuy)
        


       
class Solution:
   def solve(self, book, page, page_size):
      l=page*page_size
      return book[l:l+page_size]
ob = Solution()

page = 1
page_size = 1000
print(ob.solve(lisuy, page, page_size))

    




connection_obj.commit()

# Close the connection
connection_obj.close()
