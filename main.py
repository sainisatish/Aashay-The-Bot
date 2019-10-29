# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 21:32:01 2019

@author: satishsaini

"""

"""

IMPORTANT NOTE - I am continus making it better help me to make it better

"""

import requests
import jsonfiles
app_id="your id from Oxford api"
app_key="your key from Oxford api"
language="en-gb"
# Requesting for Data
def word_mean():
    word_id=input("your word : ")
    url="https://od-api.oxforddictionaries.com:443/api/v2/entries/"+language+"/"+word_id.lower()
    r=requests.get(url , headers={"app_id":"your id","app_key":"your key"} )
    # passing this to the imported file (jsonfiles) to extracting meaningfull data
    jsonfiles.json_ext(r) 

# WELCOME NOTE
if __name__=='__main__':
    name=input("Sir what is your name ?\n")
    age=input("Age ?")
    print("Hi I'm Aashay \nwelcome {}".format(name))
    need_help=input("Hey Do you need any kind of help : ")
    if need_help=="yes":
        print("choose options : \n")
        print("1 - Word Meaning ?\n")
        print("2 - Wants to Know Special Facts ?\n")
        print("3 - Have a Question ?\n")
        print("OR Want to talk with me\n")
        if 1==int(input()):
            word_mean()
        elif 2==int(input()):
            print("newton is famous scientist or feature ")
        elif 3==int(input()):
            print("what is your question ? ")
