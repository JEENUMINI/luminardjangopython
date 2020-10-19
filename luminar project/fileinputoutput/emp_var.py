f=open("employee","r")
employee={}




for lines in f:
    data=lines.rstrip("\n").split(",")
    #print(data)
    id=data[0]
    name=data[1]
    salary=data[2]
    exp=data[3]
    desig=data[4]

    if id not in employee:
        employee[id]={"id":id,"name":name,"salary":salary,"exp":exp,"desig":desig}

    else:
        pass
# for k,v in employee.items():
#     print(k,"->",v)
#
# def getdetails(eid):
#     if eid in employee:
#         print(employee[eid]["name"])
#     else:
#         print("employee does not exist with this field")
#
# getdetails("1001")
#
# getdetails("1002")

def getemployeedetails(**args):
    eid=args["id"]
    prope=args["prop"]
    print(employee[eid]["name"])
    print(employee[eid][prope])

getemployeedetails(id="1001",prop="salary")
getemployeedetails(id="1001",prop="exp")
getemployeedetails(id="1003",prop="desig")
#getemployeedetails(id="1002",prop="desig""salary")