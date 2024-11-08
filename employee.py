import pickle
f= open("employee.dat", "wb")
emp=[]
while True:
    no= int(input("Enter employee no: "))
    name= input("Enter name: ")
    sal= int(input("ENter salary of employee: "))
    ans= input("Do you want to enter more records ?(y/n)")
    emp.append([no,name,sal])
    if ans=="n":
        break
pickle.dump(emp,f)

f.close()
