
#!/bin/env python
#----------------------------------------------------------------------------
# Name:         synthetico.py
# Purpose:      main module for Synthetico 
#
# Author:       Marco Visibelli
# Contact:      https://github.com/marcovisibelli
#
# Created:      02/04/2017
# Copyright:    (c) 2018 by Marco Visibelli
# Licence:      MIT license
#----------------------------------------------------------------------------

import sys, os
import pandas as pd 
import numpy as np
import random
import datetime
from tqdm import tqdm
from modules.utils import *

class synthetico:

    def __init__(self):
        pass

    def save(self):
        pass
        #df_final.to_csv("data/"+str(structure_table_4["name"])+".csv")

    def _builder(self,table_element,meta_context):
        # this rappresent one row

        data_rows = []

        context = process_context(meta_context)
        
        for ele in range(0,context["number"]):

            # this transform the meta context into a context

            context = process_context(meta_context)

            data_row ={}

            for entity in  table_element["structure"]:


                # this let you to rename entities
                if "rename"  in entity.keys():
                    
                    values_to_rename = entity["rename"]

                    # for all the elements to rename
                    for element_to_rename in values_to_rename:

                        if element_to_rename[0] in context.keys():
                            context[element_to_rename[1]]= context[element_to_rename[0]]

                        if element_to_rename[0] in data_row.keys():
                            data_row[element_to_rename[1]]= data_row[element_to_rename[0]]

                #print(entity)
                
                value = 0
                
                lista_selected = []

                if entity["type"] == "choice":
                    
                    entity_values = globals()[entity["enity"] +"_entity"]
                    
                    list_of_values = entity_values["values_all"]

                    lista_selected = []
                    
                    for ele in list_of_values:
                        # search in the context or IN THE CURRENT row
                        rit = apply_context(entity_values["selectors"],ele,context,data_row) 
                        if rit:
                            lista_selected +=rit
                    
                    x_list = sum(lista_selected, [])
                                    
                    value = random.choice(x_list)

                    # this add the feature to the row
                #
                if entity["type"] == "choice_range":
                    
                    entity_values = globals()[entity["enity"] +"_entity"]
                    
                    list_of_values = entity_values["values_all"]

                    lista_selected = []
                    
                    for ele in list_of_values:
                        # search in the context or IN THE CURRENT row
                        rit = apply_context(entity_values["selectors"],ele,context,data_row) 
                        if rit:
                            lista_selected +=rit
                                                                    
                    value = round(random.uniform(lista_selected[0][0],lista_selected[0][1]),2)

                    # this add the feature to the row                
                    
                elif entity["type"] == "progressive":
                    
                    if  entity["enity"] not in prog_id_entity.keys():
                        prog_id_entity[entity["enity"]] = entity["index_start"]

                    last_value = prog_id_entity[entity["enity"]]

                    value = last_value + 1

                    prog_id_entity[entity["enity"]] = value

                elif entity["type"] == "choice_fix":

                    value = random.choice(entity["range"])            
                
                elif entity["type"] == "choice_stat":

                    value = statistical_select(entity["range"])        

                elif entity["type"] == "phone_number":

                    value = phone_generator(entity["pattern"])    

                elif entity["type"] == "random_amount":

                    value = random.uniform(entity["range"][0],entity["range"][1]) 

                elif entity["type"] == "random_range":

                    value = random.randint(entity["range"][0], entity["range"][1])

                elif entity["type"] == "fix_value":   

                    value = entity["value"]
                    
                elif entity["type"] == "rand_date":   
                    
                    value = random_date(entity["range"][0], entity["range"][1])

                elif entity["type"] == "delta_date":   
                    
                    # take the relative data
                    start = data_row[entity["enity"]]

                    # add a delta
                    value =  start + datetime.timedelta(seconds= 90000 * random.randint(entity["range"][0], entity["range"][1]))
                    
                elif entity["type"] == "context":   
                    
                    # data could be i the context or in the current directory
                    if entity["enity"] in context.keys():
                        value = context[entity["enity"]]

                    elif entity["enity"] in data_row.keys():
                        value = data_row[entity["enity"]]

                elif entity["type"] == "function":   
                    
                    entity_function = globals()[entity["enity"] +"_entity"]

                    value = entity_function(data_row,context)
                
                data_row[entity["name"]] = value    
            # append row to dataframe
            data_rows.append(data_row)

        df = pd.DataFrame(data_rows)
        
        prog_id_entity["values"] = 0
        
        df.reset_index(drop=True)

        return df

    def process_df(self,df,meta_context,structure_table_2):
        df_final_return = None 

        counter = 0

        for index, row in tqdm(df.iterrows(), total=df.shape[0]):

            context_instance = merge_two_dicts(meta_context,row.to_dict())

            if counter == 0:
                df_final_return = self._builder(structure_table_2,context_instance)
                
            else:
                df2 = self._builder(structure_table_2,context_instance)

                df_final_return = df_final_return.append(df2)

            #TO REMOVE
            prog_id_entity["id_sales_month_x"] = 0 
            prog_id_entity["id_sales_month_y"] = 0 

            counter +=1

        df_final_return.reset_index(drop=True)

        return df_final_return
            
    def process_numb(self,number,meta_context,structure_table):
        df_final = None 

        for index in tqdm(range(0,number)):

            if index == 0:
               #print(data_row)
                df_final = self._builder(structure_table,meta_context)
                
            else:
                df2 = self._builder(structure_table,meta_context)
                df_final = df_final.append(df2)
            
        return df_final
