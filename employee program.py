import pickle
f= open("employee.dat", "rb")
f.seek(0)
rec= pickle.load(f)

f.close()

print("The records are: ")
print(rec)

def modify():
    count =0
    f=open("employee.dat", "wb")
    no= int(input("Enter employee number to change : "))
    for i in range (len(rec)):
        if rec[i][0] == no:
            print("Found employee")
            print(rec[i])
            sal= int(input("Enter new salary: "))
            rec[i][2]= sal
            
            count = count+1
    

    if count ==0:
        print("Employee record not found")
    pickle.dump(rec,f)

    f.close()


def delete():
    count=0
    f=open("employee.dat", "wb")
    no= int(input("Enter employee no you want to delete: "))
    for i in range(len(rec)-1):
        if rec[i][0]== no:
            rec.pop(i)
            count= count+1

    if count == 0:
        print("No record found")

    pickle.dump(rec,f)
    f.close()

print("1- Modify salary")
print("2- Delete record")
n=int(input("ENter choice: "))
if n==1:
    modify()
elif n==2:
    delete()

else:
    print("Wrong choice entered")
    
    
