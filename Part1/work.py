import random
import time
import math
lettre="aaabcdeeeeefghiiijklmmnnoooppqrsssttuuuvwxyyz"
keyWords = ["Building ", "Compressing", "Exctracting", "Processing", "Debug", "Compiling", "Starting", "Analyzing", "Package", "Spring", "NuGet"]
n = 0
while(n<500):
    n+=1
    mot = ""
    l = ""
    phrase = ""
    j = random.randint(0,len(keyWords)-1)
    phrase = keyWords[j]
    for k in range(0,random.randint(3,7)) :
        i = random.randint(0,len(lettre)-1)
        mot = mot + lettre[i]

    phrase = phrase + " " + mot + ".cpp..."
    print(">", phrase)
    time.sleep(math.log1p(random.randint(0,500)/1000))
    if n%54 == 0:
        print ("1>------ Build started: Project: PIODBC, Configuration: Debug x64 ------")
        print ("1>  Restoring NuGet packages...")
        print ("1>  To prevent NuGet from downloading packages during build, open the Visual Studio Options dialog, click on the Package Manager node and uncheck 'Allow NuGet to download missing packages'.")
        print ("1>  All packages listed in packages.config are already installed.")
        print ("1>     Creating library C:\\Users\\Dummy\\Desktop\\PIODBC3\\PI ODBC\\3.2.16300.1\\ODBC\\PIODBC\\\\bin\\Debug\\\\x64\\PIODBC.lib and object C:\\Users\\Dummy\\Desktop\\PIODBC3\\PI ODBC\\3.2.16300.1\\ODBC\\PIODBC\\\\bin\\Debug\\\\x64\\PIODBC.exp")

print ("> ")
print ("> ")
print (">EXEC : **** warning : Publisher OSIsoft-SQL-ODBC resources could not be found or are not accessible")
print ("> ")
print ("> ")
print ("> ")
print ("========== Build: ", random.randint(5,22), " succeeded, ", random.randint(0,1), " failed, 0 skipped ==========")
