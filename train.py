#!/usr/bin/python36

import numpy as np
import pandas as pd
import subprocess as sp

#print("content-type: text/html")
#print("")
project=pd.read_csv('data.csv')
#print(project.values[0][3])

row=project.index.size
#print(row)

food=["food","taste","healthy","burnt","kitchen","oily","cooked","overcooked","dinner","breakfast","lunch","meal","tasty","health","hygienic","veg","yummy","vegetarian","serving","served","ordered","chef","non-vegetarian"]

maintain=["washroom","toilet","clean","water","maintain","maintenance","not working","cleanliness","seats","charging","mosquito","teared","washrooms","dirty","birth","smelly","smell","stingy","ac","fans","fan","seat","AC"]

theft=["theft","theive","snachers","secure","unsafe","snached","teasing","teaser","bully","safe","safety","female","harrasment","sexual","torture","bullying","annoying","theives","rape","raped","assaulted","stole","missing"] 

ticket=["ticket","refund","cashback","moneyback","e-ticket","eticket","tickets","online","tatkal","net","netbanking","net banking","debit","debited","debitcard","money","credited","credit","creditcard","card","paid","paytm","mobile"]
i=0
while i<row:
    j=0
    while j<len(maintain):
        ans=food[j] in project.values[i][3]
        ans1=maintain[j] in project.values[i][3]
        ans2=theft[j] in project.values[i][3]
        ans3=ticket[j] in project.values[i][3]
        if ans == True:
            break
        elif ans1 == True:
            break
        elif ans2 == True:
            break
        elif ans3 == True:
            break
        else:
            j=j+1
    if ans == True:
        print("<h3><u>Mailed to IRCTC Catering Department</h3></u>")
        sp.getoutput("ansible-playbook food.yml")
    elif ans1 == True:
        print("<h3><u>Mailed to IRCTC Maintenance Department</h3></u>")
    elif ans2 == True:
        print("<h3><u>Mailed to IRCTC Security Department</h3></u>")
    elif ans3 == True:
        print("<h3><u>Mailed to IRCTC ticket and fund Department</h3></u>")
    i=i+1
