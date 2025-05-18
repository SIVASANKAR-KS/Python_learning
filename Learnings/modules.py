import List as k    ####prints some lines as print is used in List i.e on import List will be exeuted
print (k.list1)    ###prints list from List module

import platform
x=platform.processor()
print(x)

from LTDS_methods.List import next_method
next_method("asd")


###Be aware that import loads the whole module, hence it might take time to load whole bigger modules