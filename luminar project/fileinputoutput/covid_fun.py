f=open("complete.csv","r")
covid={}

for lines in f:
    line=lines.lower()
    data=line.rstrip("\n").split(",")
    state=data[1]
    confirmed=float(data[4])

    death=data[5]
    cured=float(data[6])

    if state not in covid:
        covid[state]={"state":state,"confirmed":confirmed,"cured":cured,"death":death}
    else:
        pass

for k,v in covid.items():
    print(k,"->",v)

# def getdetails(covstate):
#     if covstate in covid:
#         print(covid[covstate]["confirmed"])
#     else:
#         print("does not exist")
#
# getdetails("telangana")
# getdetails("punjab")

def getdetails(**args):
    st_nm=args["state"]
    prop=args["prop"]
    print(covid[st_nm]["state"])
    print(covid[st_nm][prop])

getdetails(state="kerala",prop="cured")



