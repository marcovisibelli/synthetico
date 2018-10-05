
#!/bin/env python
#----------------------------------------------------------------------------
# Name:         utils.py
# Purpose:      utils module for Synthetico 
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
from modules.data import *


def letters(input):
    valids = []
    for character in input:
        if character.isalpha():
            valids.append(character)
    valid=  ''.join(valids)
    valid = valid.replace("ó","o").replace("á","a").replace("é","e").replace("ô","o").replace("ç","c")


    return valid

def merge_two_dicts(x, y):
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z

def email(df,context):
    return letters(str(df["name"]).lower()) + "." + letters(str(df["surname"]).lower()) +"@"+ letters(str(context["company"]).lower())+".com"

#this contain the variables
email_entity = email




def statistical_select(elements):
    results = []
    resoltion = 1000
    for ele in elements:
        for conte in range(0,int(resoltion*ele[1])):
            results.append(ele[0])
    return random.choice(results)
        

def random_date(start, end):
    """Generate a random datetime between `start` and `end`"""
    return start + datetime.timedelta(
        # Get a random amount of seconds between `start` and `end`
        seconds=random.randint(0, int((end - start).total_seconds())),
    )

def apply_context(selectors,element,context,current_row):
    
    #print(element," vs ",current_row)
    # applica i selettore generico
    if selectors != []:
        lista_selectors = [ a for a in selectors if a in context.keys()]

        # per tutte le combinazioni usando il context
        ritorno = []
        # se rispetta tutti i check

        for ele_sele in lista_selectors:
            if element[ele_sele] == context[ele_sele]:
                ritorno.append(element["values"])

        lista_selectors_2 = [ a for a in selectors if a in current_row.keys()]
        # per tutte le combinazioni usando l'ultima riga 
        
        # se rispetta tutti i check
        for ele_sele in lista_selectors_2:
            if element[ele_sele] == current_row[ele_sele]:
                ritorno.append(element["values"])

        return ritorno
    else:
        return element["values"]


def process_context(meta_context):
    context = {}
    for element in meta_context.keys():
        if isinstance(meta_context[element], (list,)):
            context[element] = statistical_select(meta_context[element])
        else:
            context[element] = meta_context[element]
    return context
