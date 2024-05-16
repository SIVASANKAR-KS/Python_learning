def next_method(method_name):
    print(f"\n#############    {method_name}()   ####################")

def mprint(msg, *arg):
    print(f"{msg} +  --->  {arg}")   ## Used format to print dict along with string else it will throw error as unsupported operands.

##Methods for Dictionary
birthdays = {'employee1' : "07/03/1997"}
birthdays['employee2'] = "27/03/2000"
mprint("created a dict as birthdays", birthdays)

###update
next_method("update")
birthdays.update({"employee3": "07/08/2000"})
mprint("updated birthdays ", birthdays)

###Copy
next_method("copy")
birthdays_copy = birthdays.copy()
mprint("copied birthdays ", birthdays_copy)

###fromkeys   ===> returns a new dictionary with keys from a dict or list and default value
next_method("from keys ")
mprint("from keys with 2nd arg as 00 ",dict.fromkeys(birthdays,"00"))
mprint("from keys without 2nd arg", dict.fromkeys(birthdays))

##.items()
next_method("items")
mprint("items", birthdays.items() )

##.keys() and .values()
next_method("keys")
mprint("keys", birthdays.keys() )
next_method("values")
mprint("values", birthdays.values() )

###SetDefault ===> returns value if key is present,  else inserts key and return the value
next_method("setdefault")
mprint("setdefault example : key is not there ", birthdays.setdefault('employee4',"19/04/1998"))
mprint("setdefault example : key is already there",birthdays.setdefault('employee2',"19/04/1998"))


##.pop()
next_method("pop")
mprint("pop employee1", birthdays.pop("employee1") )
mprint("birthdays after pop ", birthdays)

##.popitem () ==> pops last inserted key-pair value and returns it as list string
next_method("popitem ")
mprint("popitem employee1", birthdays.popitem() )
mprint("birthdays after popitem ", birthdays)
birthdays.clear()

mprint("after birthdays clear", birthdays, birthdays_copy)