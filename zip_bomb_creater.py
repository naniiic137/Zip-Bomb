import zipfile,os
os.system('mode 90,10')
zip_name=input("Zip Name : ")
nb=int(input('How many file do you want : '))
print("")
print("it may take a while to create your zip file if the number is to big")
print("")
print("so here is the math 1,000,000 ≈ 1MB")
print("if you want 10,000,000 ≈ 10Mb")
print("100,000,000 ≈ 100MB")
print("1,000,000,000 ≈ 1GB")
print("")
print("but be ware of system limit and disk limit so the system limit is 9223372036854775807 ")
print("")
size=int(input("Give me file size :"))
i=1
while i<nb+1:
    with open(str(i)+".txt","w+") as f:
        f.write("0"*size)
        f.close
    i=i+1
dir_files=os.listdir(os.path.dirname(__file__))
dir_files.pop()
with zipfile.ZipFile(zip_name+'.zip','w',compression=zipfile.ZIP_DEFLATED) as z:
    for c in dir_files:
        z.write(c)
for i in range(1,nb+1):
    os.remove(str(i)+'.txt')