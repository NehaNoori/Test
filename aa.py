n=int(input("Enter n: ")) 
d={} 
for i in range(n): 
    roll_no=int(input("Enter roll no: ")) 
    name=input("Enter name: ") 
    marks=int(input("Enter marks: ")) 
    d[roll_no]=[name,marks]
print(d)
