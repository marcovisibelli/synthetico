#!/bin/env python
#----------------------------------------------------------------------------
# Name:         Main.py
# Purpose:      Create systetic data for testing machine learning machines
#
# Author:       Marco Visibelli
# Contact:      https://github.com/marcovisibelli
#
# Created:      02/04/2017
# Copyright:    (c) 2018 by Marco Visibelli
# Licence:      MIT license
#----------------------------------------------------------------------------

from modules.data import *
from modules.utils import *
from modules.synthetico import *

#----------------------------------------------------------------------------

def main():
    print(" --- Syntetic data generator --- ")

    project = "ERP"

    synth = synthetico()

    context = {
    "language": "en",
    "country": [("es",0.20),("uk",0.20),("fr",0.20),("it",0.20),("gr",0.20)],
    "company": "happycompany",
    "number" : 1
    }

    structure_table ={
    "name": "employee_table",
    "structure":[
     {"enity":"country","type":"context","name":"main_country"},
    {"enity":"name","type":"choice","name":"name"},
    {"enity":"surname","type":"choice","name":"surname"},  
    {"enity":"email","type":"function","name":"email"},  
    {"enity":"phone_number","type":"phone_number","name":"phone number","pattern":"+011-XX-XXX-XXX"},  
    {"enity":"id_employ", "type":"progressive" ,"name":"id","index_start" : 100},  
    {"enity":"id_employ2", "type":"progressive" ,"name":"employeed_id" , "index_start" : 1500}, 
    {"type":"random_range","name":"seniority", "range":(1,10)}, 
    {"type":"random_range","name":"Age", "range":(26,55)}, 
    {"type":"choice_stat","name":"Division","range":[("Engineering",0.3),("Consulting",0.2),("Marketing",0.2),("Sales",0.2),("Other",0.03),("Executive",0.07)]}]
    }

    df = synth.process_numb(1200,context,structure_table)

    df.to_csv("data/"+str(project)+"/"+str(structure_table["name"])+".csv")

    print(df)

    structure_table_2 ={
    "name": "reimbourse",
    "structure":[
    {"enity":"name","type":"context","name":"name"},
    {"enity":"surname","type":"context","name":"surname"},  
    {"enity":"id","type":"context","name":"Emploeyy_id"}, 
    {"enity":"country","type":"context","name":"country"}, 
    {"enity":"prog_id","type":"progressive","name":"id","index_start" : 9000},  
    {"enity":"rand_date","type":"rand_date","name":"Date", "range":(datetime.date(2017,1, 1),datetime.date(2017, 12, 31))}, 
    {"enity":"Date","type":"delta_date","name":"Date payment", "range":(3,8)}, 
    {"type":"choice_stat","name":"Type","range":[("Restaurant",0.3),("Hotels",0.3),("Taxi",0.3),("Honorarium",0.03),("Others",0.07)]}, 
    {"enity":"Amount_reimbourse","type":"choice_range","name":"Amount"},
    {"enity":"currency","type":"choice","name":"currency"},
    {"enity":"city","type":"choice","name":"City"},
    {"type":"fix_value","name":"Role", "value":"Sales rep"}, ]
    }


    meta_context_2 = {
    "language": "en",
    "country": [("uk",0.20),("fr",0.40),("it",0.40)],
    "number" :[(30,0.20),(176,0.10),(104,0.60)],
    "index_start":25000
    }


    df_final = synth.process_df(df,meta_context_2,structure_table_2)
    df_final.to_csv("data/"+str(project)+"/"+str(structure_table_2["name"])+".csv")

    print(df_final)

#----------------------------------------------------------------------------

if __name__ == '__main__':
    __name__ = 'Main'
    main()

#----------------------------------------------------------------------------







