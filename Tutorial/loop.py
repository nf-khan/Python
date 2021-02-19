# x=0
# # while loop
# while(x<5):
#     print(x)
#     x=x+1

# # basic for loop
# for x in range(5, 10):
#     print(x)

# # use for loop for correction
# days =["mon","tue","wed","thu","fri","sat","sun"]
# for d in days:
#     print(d)

# # break 
# for x in range(5, 10):
#     if (x==7):break
#     print(x)

# continue
for x in range(5, 10):
    if (x%2==0):continue
    print(x)

# to get index use enumerate() function
days =["mon","tue","wed","thu","fri","sat","sun"]
for i,d in enumerate(days):
    print(i, d)