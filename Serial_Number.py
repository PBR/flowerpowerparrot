# -*- coding: utf-8 -*-
"""
Created on  Mon Sep 12 11:15:14 2016

@author: Maxime Mobailly - Robert Van Loo (supervisor and reviewer) - Wageningen University
"""

import pandas as pan


def serial_number(loc2name):
    """
    This scipt was done to get the serial number of the sensors
    and it returns result like this: 
    Sensors name(or nickname), serial number (the four last numbers) and the complete serial number  
    """
     # create a new dataframe
    nickname_serialnumber = pan.DataFrame.from_dict(loc2name,orient = 'index')

    nickname_serialnumber.rename(index = {'0':"sensors'nickname"}, columns = {0:'serial_number'},inplace = True)
    nickname_serialnumber['serial_number_2'] =  nickname_serialnumber['serial_number'].str[12:]
    
    nickname_serialnumber.sort_index(axis=0, ascending=True, inplace=True)
    
    return(nickname_serialnumber)
    
