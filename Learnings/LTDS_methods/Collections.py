"""
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""
print("press 'yes' or 'no' to answer\n")
is_ordered = 0 if input("is ordered\n") == "yes" else 1
is_mutable = 0 if input("is mutable\n") == "yes" else 1
duplicates_allowed = 0 if input("allows duplicated?\n")  == "yes" else 1

#unordered , immutable , duplicate
#000-list
#001-dict
#011-tuple
#101-dict
#110-set
collections = [[["List","Dictionary"], ["","Tuple"]],[["","dic"],["set",""]]]
print(collections[is_ordered][is_mutable][duplicates_allowed])
