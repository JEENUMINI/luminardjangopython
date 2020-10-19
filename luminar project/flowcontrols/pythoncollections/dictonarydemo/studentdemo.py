student={"rollno":1,"name":"geenu","total":90}
print(student)
print(student["name"])
print(student["rollno"])
print("college"in student)
print("total" in student)
student["college name"]="luminar"
student["gender"]="female"
print(student)
student["total"]=200
print(student)
student["total"]+=50
print(student)


for k in student:
#   print(k)
    print(student[k])