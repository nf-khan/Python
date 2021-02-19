#declaring variable
f=0
# print(f)

# #declaring string
# f="abc"
# print(f)

# #ERROR: variable of diff type cant combined
# print("this is a string "+str(123))


#Global vs. Local variables
def someFunction():
    global f
    f="def"
    print(f)

someFunction()
print(f)

del f
print(f)