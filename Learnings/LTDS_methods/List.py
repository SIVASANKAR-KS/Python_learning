def next_method(method_name):
    print(f"\n#############    {method_name}()   ####################")

def mprint(msg, *arg):
    print(f"{msg} +  --->  {arg}")   ## Used format to print dict along with string else it will throw error as unsupported operands.

##Methods for Lists
list1 = ["abc", 34, True,34, 40, "male", '']

###append
next_method("append")
list1.append("new_element")
mprint("append new_element to list  ", list1)

###insert
next_method("insert")
list1.insert(2, "new_element")
mprint("insert new_element to list at index 2  ", list1)

###copy
next_method("copy")
list2 = list1.copy()
mprint("copy of list1  ", list2)

###index
next_method("index")
try:                                                        ##===> throws error if searched element is not in list
    mprint("index of cba in list1  ", list1.index("cba"))
except:
    print("cba not in list")
mprint("index of 34 in list1  ", list1.index(34))

###count   ===> counts the number of occurences of an element 
next_method("count")
mprint("copy of list1  ", list1.count(34))

###remove
next_method("remove")
mprint("list1 before remove",list1)  
mprint("remove the new_element in list1 ", list1.remove("new_element"))   ##==> removes first element 'new_element in list1'
mprint("list1 after remove",list1)

###pop
next_method("pop")
mprint("list1 before pop",list1)
mprint("popped the list1 ", list1.pop())    
mprint("list1 after pop",list1)

###reverse
next_method("reverse")
mprint("list1 before reverse",list1)
mprint("reverse the list1 ", list1.reverse())  ##returns None
mprint("list1 after reverse",list1)

###sort
next_method("sort")
def myFunc(e):
  return len(e) if isinstance(e, str) else e

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

#cars.sort(key=myFunc)
mprint("list1 before sort",list1)
mprint("sort the list1 ", list1.sort(key=myFunc))  ##returns Error not supported for int,string
mprint("list1 after sort",list1)

###clear
next_method("clear")
list1.clear()
mprint("cleared the list1 ", list1)
mprint("printing list2",list2)

###extends
next_method("extend")
list1.extend(list2)
mprint("printing list1 after extend", list1)