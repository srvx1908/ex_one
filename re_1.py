import csv 
with open ('data.csv',mode='w',newline='')as file:
    writer=csv.writer(file)
    writer.wrterow(['name','age'])
    writer.writerow(['alice',30])