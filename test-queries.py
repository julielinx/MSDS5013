import csv, sqlite3,matplotlib
#from pylab import *
#import numpy as np
#import matplotlib.pyplot as plt
#import matplotlib.cbook as cbook
import matplotlib
import pylab
# experimental test code is for testing purposes only, TLW 2017

conn = sqlite3.connect( "mycsv35.db" )
conn.text_factory = str  #bugger 8-bit bytestrings
cur = conn.cursor()


#cur.execute('select

#conn.commit()
cur = conn.cursor()
print "sql queries"
#select mytable3.field2,mytable4.field1 from mytable3 left outer join mytable4 on mytable3.field1=mytable4.field1;!!!

q1=cur.execute("select mytable3.field2,mytable4.field1 from mytable3 left outer join mytable4 on mytable3.field1=mytable4.field1;")
data1 = cur.fetchone() #retrieve the first row
print(data1[0:1])
print(data1[0:1])
data_all=cur.fetchall()
print(data_all[1:40])

print q1
#select mytable4.field2,mytable5.field1 from mytable5 left outer join mytable4 on mytable4.field2=mytable5.field2;

#select mytable4.field1,mytable5.field1 from mytable5 left outer join mytable4 on mytable4.field2=mytable5.field2;!!!
q2=cur.execute("select mytable4.field1,mytable5.field1 from mytable5 left outer join mytable4 on mytable4.field2=mytable5.field2;")
data1 = cur.fetchone() #retrieve the first row
print(data1[0])

data_all=cur.fetchall()
print(data_all[1:40])

print q2

conn.commit()
#q3=cur.execute("select mytable3.field2,mytable5.field1 from mytable3 inner join mytable4 on mytable3.field1=mytable4.field1 inner join mytable5 on mytable4.field2=mytable5.field2;")

q3=cur.execute("select mytable3.field2 from mytable3 inner join mytable4 on mytable3.field1=mytable4.field1 inner join mytable5 on mytable4.field2=mytable5.field2;")


#[data3,data4]=cur.fetchall();
bp=cur.fetchall();



q3=cur.execute("select mytable5.field1 from mytable3 inner join mytable4 on mytable3.field1=mytable4.field1 inner join mytable5 on mytable4.field2=mytable5.field2;")


age=cur.fetchall();
conn.commit()


matplotlib.pyplot.scatter(age,bp)

matplotlib.pyplot.savefig("bp-vs-age-boran.pdf")
