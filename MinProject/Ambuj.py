import zipfile
import os 
def crack(zfile,passw,infol):
    try:
        zfile.extractall(infol,pwd=bytes(passw, 'utf-8'))
        return(passw)
    except:
        return("0")

ch='y'
while ch=='y':
    os.system('cls')
    print("-------------------Hello!!!!Welcome to ZipFile Cracker--------------------------\nPlease Enter the zipfile file name.")
    filename=input()    
    if filename.endswith('.zip')==False: 
        print("Please Enter a valid file type!!!") 
    else:
        zfile=zipfile.ZipFile(filename) 
        print("Enter the folder where you want to extract the file")
        infol=input()
        pfile=open('Passwords.txt')
        for i in pfile.readlines():
            passw=i.strip('\n')
            g=crack(zfile,passw,infol)
            if g!="0":
                print("Password is: "+ g)
                print("Contents of Zipfile: \n")
                print(zfile.printdir())
                break
    print("Do you want to continue(y/n): ") 
    ch=input()
zfile.close()   
pfile.close()
