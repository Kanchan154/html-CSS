import csv
fh=open("student.csv","w",newline="")
stu=csv.writer(fh)
stu.writerow(["rollNO","marks","name"])
list=[]
for i in range(4):
    rollNo=int(input("enter the rollNo: "))
    marks=int(input("Enter the marks:"))
    name=input("Enter the name:")
    list.append([rollNo,marks,name])
stu.writerows(list)
fh.close()