class MyClass:
    
    def funcName(self):

        self.variableName = "VARIABLE STRING"


# Usage
myClass = MyClass()

# I want to print the string defined in variableName, using below way of calling it
# Its currently erroring out 
# IS THIS POSSIBLE
print(myClass.funcName.variableName)  # Current Output : ERROR : AttributeError: 'function' object has no attribute 'variableName'
# Needed Output: VARIABLE STRING
