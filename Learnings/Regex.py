import re
txt="asd The rain Portasdugal9d asd in Spain ad Portugal"
x=re.search("The.*Spain$",txt)     ##return None as search fails
print(x)
x=re.findall("Portugal|Spain", txt)      ##['Portugal', 'Portugal']
print(x)
x=re.split("Portugal", txt)        ##['asd The rain ', ' in Spain ', '']
print(x)
x=re.sub("Portugal", "9" , txt)    ##Replaces all occurences
print(x)
x=re.sub(r"Portugal$", "9", txt, 1)  ##Replaces only one occurence
print(x)


###Special Characters 
spcl_char={
    "\A"  : "Return a match at end or beginning of the string",
    r"\b" : "Returns a match at end or beginning of the word",
    r"\B" : "Returns not a match at end nor beginning of the word",             
    r"\d" : "Returns a match where string contains digits",                     ##returns string only digits
    r"\D" : "Returns a match where string does not contain digits",             ##returns string excluding digits
    r"\s" : "Returns a match where string contains white space",                ##returns string only the whitespaces
    r"\S" : "Returns a match where string does not white space",                ##returns string excluding digits
    r"\w" : "Returns a match where string contains any alphanumeric",           ##returns string only the alphanumeric
    r"\W" : "Returns a match where string does not contain any alphanumeric",   ##returns string excluding alphaneric
    r"\Z" : "Returns a match at the end of the string",
    }
print(spcl_char)


for k,v in spcl_char.items():
   print(k,v)
   x=re.findall(f"{k}", txt)
   print(x)
