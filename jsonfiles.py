# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 20:45:28 2019

@author: satishsaini
"""
import json
def json_ext(r):
    json_data=r.json()
    print("Meaning Of The Word : {} ".format(json_data['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]["definitions"][0]))
    print("Examples : {} \n or {}".format(json_data['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]["examples"][0]['text'],json_data['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]["examples"][1]['text']))
    print("Short Examples : {} \n or {}".format(json_data['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['subsenses'][0]["examples"][0]['text'],json_data['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['subsenses'][0]["examples"][1]['text']))
