# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 13:52:09 2016

@author: Maxime
"""
import requests
import time

def account_selection(Account,Account_list):
    """
    Select the account you want to work on
    """
    test1 = '1' in str(Account)
    if test1 == False :
        Account_list.remove('robert.vanloo@wur.nl')
    test2 = '2' in str(Account)
    if test2 == False:
        Account_list.remove('flowerpower.pbr1@gmail.com')
    test3 = '3' in str(Account)
    if test3 == False:
        Account_list.remove('flowerpower.pbr2@gmail.com')
    test4 = '4' in str(Account)    
    if test4 == False:
        Account_list.remove('flowerpowertest1@gmail.com')
    test5 = '5' in str(Account)
    if test5 == False:
        Account_list.remove('Jd.ligthart@bejo.nl')

    return(Account_list)


def loggin(username):
    #==================================================================================
    #               Log in
    #
    #  Log in to your flowerpower account and to your 'Parrot For Developers' account
    #==================================================================================
    
        # First we set our credentials
    username = username
    password ='smart2diverse'
    if username == 'Jd.ligthart@bejo.nl':
        password = 'BejoZaden1972'
    
        # Get your client credentials here: https://apiflowerpower.parrot.com/api_access/signup

    client_id = 'wurfp1@gmail.com'
    client_secret = 'a02OOSurToc9OpPRIZevcePl6dd2UX5KoHORl8gdfukRa5Q6'

    
    #==============================================================================
    #               Requesting data from the API (1/2)
    #  " application programming interface "
    #  Get authorization to access to the data and prepare the downloading
    #==============================================================================
    
    ###
    # few parameters
    ###
    
    Internet_connection = False
        # we assume that we are not connected to internet.
    attempt = 1
    
    
        # we could try 10 times to make a connection with the website.
        # Now we need to send a request to the website (API)
        # But we need to be sure that we have a corrrect internet connection to avoid any crashes.
    
    # While loop 1 - 
    while Internet_connection == False:
        
        if attempt <= 11: # try to request the data 10 times, and after that, just quit if it is still not working.
            try:
#                req = requests.get('https://apiflowerpower.parrot.com/user/v1/authenticate',
#                               data={'grant_type': 'password','username': username,
#                                     'password': password,'client_id': client_id,
#                                     'client_secret': client_secret,})
                req = requests.get('https://api-flower-power-pot.parrot.com/user/v1/authenticate',
                               data={'grant_type': 'password','username': username,
                                     'password': password,'client_id': client_id,
                                     'client_secret': client_secret,})
                
                # 'Requests' comes with a builtin JSON decode,this is the reason why we must
                # the json function.
                response = req.json()
    
                # Get authorization token from response
                access_token = response['access_token']
                # -> string
                
                auth_header = {'Authorization': 'Bearer {token}'.format(token = access_token)}
                # -> dict
    
                # From now on, we won't need initial credentials: access_token and auth_header
                # will be enough.
    
                # Get sync data
                req = requests.get('https://api-flower-power-pot.parrot.com/garden/v2/configuration',
                                   headers=auth_header)
                
                response = req.json()
                # -> dict
    
                locations = response['locations']

                # -> list of dict, one dict for one sensor.
                
                # Build a dict to link location_identifiers to the sensors' identifier
                # Build a dict to link location_identifiers to the sensors' nickname
                
                loc2name = {l['plant_nickname'].upper().replace(" ","_"): l['location_identifier'] for l in locations}
                serial2name = {l['plant_nickname'].upper().replace(" ","_") : l['sensor']['system_id'] for l in locations}    
                    # capitalize the nickname and replace any whitespace
                Internet_connection = True
                    
            except:
                    
                print(attempt,'attempt(s):','Failed to establish a connection with the website. waiting time of two minutes before the next attempt')
                attempt+=1
                # wait 2 minutes before to try once again.
                time.sleep(120)
        else:
            print('After 10 attempts, it is still impossible to establish a connection with the cloud /n'
                'Check your wifi connection before launch the script a new time')
            quit()
            
    return(loc2name,auth_header,serial2name)