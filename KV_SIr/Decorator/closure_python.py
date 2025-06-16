# def outer_func(x):
#     y =10
#     def innner_func(z):
#         return x+y+z
#     return innner_func

# # closure = outer_func(5)
# # result = closure(3)
# # print(result)


# def functionA():
#     count = 0
#     def functionB():
#         nonlocal count
#         count+=1
#         return count
#     return functionB

# # myfunction = functionA()
# # retVal = myfunction()
# # print("Counter : ",retVal)

# # retVal = myfunction()
# # print("Counter : ",retVal)

# # retVal = myfunction()
# # print("Counter : ",retVal)

# # retVal = myfunction()
# # print("Counter : ",retVal)


# def  outerfunc(x): # Outer Function
# 	print("I am From Outer Function")
# 	def innerfunc(y): # inner Function--Called Closure
# 		print("I am from Inner Function")
# 		z=x+y
# 		return z
# 	return innerfunc

# #Main Program
# ifc=outerfunc(10) # Outer Function Call
# print("Outer Function Call Completed Its Execution")
# print("-------------------------------------------------")
# res=ifc(5) # Inner Function Call
# print("First time=",res)
# print("-------------------------------------------------")
# res=ifc(15) # Inner Function Call
# print("Second time=",res)



#ClosureEx2.py
def icicibankloanprocess(processingfee): #Outer Function OR Enclosing Function
	def  iciciemical(emiamt): # Inner Function OR Enclosed Function
		finalemi=processingfee+emiamt
		return finalemi
	return iciciemical

#Main Program
iciciem=icicibankloanprocess(100) # Outer Function call
emipay=iciciem(10000) # Inner Function Call
print("Pay=",emipay)
emipay=iciciem(15000) # Inner Function Call
print("Pay=",emipay)
