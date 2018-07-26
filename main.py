#!/usr/bin/python36

import cgi
import subprocess as sp
print("content-type: text/html")
print("")


form=cgi.FieldStorage()
train_num=form.getvalue("train_num")
coach_num=form.getvalue("coach_num")
date=form.getvalue("date")

print("""<b>YOUR SUBMISSION:</b><br> 
TRAIN NUMBER: {}<br>""".format(train_num))
print("	DATE OF HAPPENING: {}<br>".format(date))
print("COACH NUMBER: {}<br>".format(coach_num))
feedback=form.getvalue("feedback")
print("FEEDBACK: {}<br>".format(feedback))
print("<marquee><h1>THANKYOU!</h1></marquee>")
f=open("data.csv","w")
f.write("""train,coach,date,feedback
{},{},{},{}""".format(train_num,coach_num,date,feedback))
f.close()
f=open("feedback.txt","w")
f.write("""train number: {}
coach number: {}
date of occurence: {}
feedback: {}""".format(train_num,coach_num,date,feedback))
f.close()

sp.getoutput("python36 train.py")
