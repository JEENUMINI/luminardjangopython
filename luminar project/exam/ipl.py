f=open("ipl.txt","r")
dt={}
for lines in f:
    ipl_data=lines.rstrip("\n").split(",")
    id=ipl_data[0]
    name=ipl_data[1]
    matches=ipl_data[2]
    win=ipl_data[3]
    loss=ipl_data[4]
    points=ipl_data[5]
    if(id not in dt):
        dt[id]={"id":id,"name":name,"matches":matches,"win":win,"loss":loss,"points":points}
    else:
        pass
for k,v in dt.items():
    print(k,"->",v)


# def getname(ipl_id):
#     if ipl_id in dt:
#         print(dt[ipl_id]["name"])
#     else:
#         print("no team with this id")
#
#
# getname("1")
# getname("2")
#
# def getdetails(**args):
#     ipl_id = args["id"]
#     prope=args["prope"]
#     print(dt[ipl_id]["name"])
#     print(dt[ipl_id][prope])
#
#
#
#
# getdetails(id="1",prope="matches")
# getdetails(id="2",prope="win")

def getData(**args):
    id=args["id"]
    attr=args["data"]
    #print(attr)
    if(id in dt):
        print(dt[id]["name"])
        print(dt[id][attr])
    else:
        print("no team exist")
getData(id="1",data="win")
getData(id="2",data="matches")