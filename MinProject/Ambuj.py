import zipfile 

def crack(zfile,passw):
    try:
        zfile.extractall(pwd=bytes(passw, 'utf-8'))
        return(passw)
    except:
        return("0")

zfile=zipfile.ZipFile('Test.zip')
pfile=open('Passwords.txt')
for i in pfile.readlines():
    passw=i.strip('\n')
    g=crack(zfile,passw)
    if g!="0":
        print("Password is: "+ g)
        print("Contents of Zipfile: \n")
        print(zfile.printdir())
        break
  
zfile.close()    
    