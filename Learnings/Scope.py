print("########### 1 #########")
x=100
def myFunc():
    #print(x)           #print will fail as x is not in scope hence not defined
    x=300               #==> thinks as a separate variable
myFunc()
print(x)

print("\n\n ########### 2 #########")
x=100
def myFunc():
    x=300
    def insideFunc():
        x=500            #x will be considered as a different variable
    insideFunc()
    print(x)             #==> prints 300 as x scope lies in myFunc and so x is 300
myFunc()
print(x)

print("\n\n ########### Global Scope #########")
x=100
def myFunc():
    global x 
    print(x)                 ##will print 100 and won't throw error as x is globalized
    x=300
    def insideFunc():
        #global x           #use global to update x as 500 else x will be considered as different varaible
        x=500 
    insideFunc()
myFunc()
print(x)                    ##prints 300 since x is defined as global in first function

print("\n\n ########### non local Scope #########")
x=100
def myFunc():
    #nonlocal x               ## will throw error as there is no binding for x 
    #print(x)                 ##will print 100 and won't throw error as x is globalized
    x=300
    def insideFunc():
        nonlocal x           #use global to update x as 500 else x will be considered as different varaible
        def anotherinside():
            nonlocal x        #value of x is transferred from myFunc-> insideFunc->anotherinside
            print(x)
            x=700
        anotherinside() 
    insideFunc()
    print(x)
myFunc()
print(x)                    ##prints 300 since x is defined as global in first function

