def main ():

    probelms = []
    n = int(input("Enter number of probelms : "))
    while n>6:
        print("Too many probelms")
        n = int(input("Enter number of probelms : "))
    for i in range(0,n):
        put=str(input())
   
        probelms.append(put)

    print(probelms)

 # code for arrangement of probelms 
    for x in probelms:
        if " " not in x:
            print("There must be space on both side of operator")
        y = x.split(" ",2 )
    
        a = len(y[0])
        b = len(y[2])
        if y[1] == '+':
            c = int(y[0]) + int(y[2])
        if y[1] == '-':
            c = int(y[0]) - int(y[2])

        if (a | b)>5:
            print("probelm can't be more than four digits.")
        if (y[0].isdecimal() | y[1].isdecimal()) == False:
            print("Number should only contain digits.")
        if a==b:
            string1 =y[0].rjust(a+2)
            print(string1)
            print(y[1]+' '+y[2])
            print("-"*(a+2))
            answer =str(c).rjust(a+2)
            print(answer)
        if a>b:
            string2 =y[0].rjust(a+2)
            print(string2)
            if a==b+1:
                print(y[1]+'  '+y[2])
            if a==b+2:
                print(y[1]+'   '+y[2])
            if a==b+3:
                print(y[1]+'    '+y[2])
            print("-"*(a+2))
            answer =str(c).rjust(a+2)
            print(answer)

        if a<b:
            if a+1==b:
                string3 =y[0].rjust(a+3)
                print(string3)
                answer =str(c).rjust(a+3)
               
            if a+2==b:
                string4 =y[0].rjust(a+4)
                print(string4)
                answer =str(c).rjust(a+4)
            
            if a+3==b:
                string5 =y[0].rjust(a+5)
                print(string5)
                answer =str(c).rjust(a+5)
            
            print(y[1]+' '+y[2])
            print("-"*(b+2))
            print(answer)









        # for z in y:
        #     print(z[0])
if __name__ == "__main__":
    main()


### for find
    # https://www.w3schools.com/python/trypython.asp?filename=demo_ref_string_find2

### for spilt character
    # https://www.w3schools.com/python/trypython.asp?filename=demo_regex_split2

### to check either string is decimal or not
    # https://www.w3schools.com/python/trypython.asp?filename=demo_ref_string_isdecimal2

### to spilt a string
    # https://www.w3schools.com/python/trypython.asp?filename=demo_ref_string_split
    # https://www.w3schools.com/python/trypython.asp?filename=demo_ref_string_split4