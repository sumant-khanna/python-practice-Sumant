n = int(input("enter time in hours"))
n1 = int(input("enter time in minutes"))

if n>=5 and n<=23:
    if n1>=30 and n1<=59:
        GMTh = n-5              #GMTh means Greenwich mean time in hours
        GMTm = n1-30            #GMTm means Greenwich mean time in minutes
        print("GMT=", GMTh,":",GMTm)
    elif n1<=30 and n1>=0:
        GMTh = n-6
        GMTm = n1+30
        print("GMT=",GMTh,":",GMTm)
    else:
        print("time not valid")
elif n<=5 and n>=0:
    if n1>=30 and n1<=59:
        GMTh = 24-5+n
        GMTm = 30+n1
        print("GMT=",GMTh,":",GMTm)
    elif n1<=30:
            GMTh=24-6+n
            GMTm=30+n1
            print("GMT=",GMTh,":",GMTm)
    elif n1<=0 and n1>=59:
            print("time not valid")
    else:
            print("time not valid")

else:
    print("time not valid")



ontarioh = GMTh - 5              #ontarioh means time in ontrio in hours
ontariom = GMTm - 0              #ontarioh means time in ontrio in minutes

print("Time in Toronto,Ontario = ",ontarioh,":",ontariom)
