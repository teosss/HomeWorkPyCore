import re

def valid_email(email):
    error = False
    if email.count("@") == 1:
        e_tag = email[email.find("@"):]
        e_dot = e_tag[e_tag.find("."):]
        if e_tag.find("_") > 0 or re.findall("[0-9]", e_dot) != []:
            error = True
    else:
        error = True
    return "Email is not valid" if error else "Email is valid"
    




valid_email("trafik@ukr.tel.com")          #output:   "Email is valid"

valid_email("trafik@ukr_tel.com")        #output:   "Email is not valid"

valid_email("tra@fik@ukr.com")           #output:   "Email is not valid"  

valid_email("ownsite@our.c0m")         #output:   "Email is not valid"  

valid_email("ow0nsite@our.com")         #output:   "Email is not valid"  


"""
Author code

import re

def valid_email(address_to_verify):
    regex_template = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,3})$'
    try:
        if re.match(regex_template, address_to_verify) == None:
	        raise ValueError('Email is not valid')
        return "Email is valid"
    except ValueError as e:
        return e

"""