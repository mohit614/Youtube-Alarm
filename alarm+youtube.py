#the programe need a text file having a list of youtube videos links ,line-by-line
from datetime import datetime
from time import sleep
from random import randint
import webbrowser
import os
x= datetime.now().time();
print "CURRENT TIME IS =="
print (unicode(x))[:-7];

t=raw_input("ENTER time FOR ALARM=")
hh=t[0:2];
mm=t[3:5];
ss=t[6:8]
while x.hour!=int(hh) or x.minute!=int(mm) or x.second!=int(ss):
    x= datetime.now().time();
    sleep(1)
    print unicode(x)[:-7];
   
    
f=open('file2.txt','r')
lines=f.readlines()
n=randint(0,len(lines));
print n;
webbrowser.open_new(lines[n]);


        