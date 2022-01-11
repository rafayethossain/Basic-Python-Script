fileLocation = "D:\PythonFullStack\Python-Hard-Way\AutomateTheBoringStuff\hello.txt"

helloFile = open(fileLocation)

readText = helloFile.read() 
print(readText + "\n")

helloFile = open(fileLocation)
readLines = helloFile.readlines()
print(readLines)
helloFile.close()


textFile = open("D:\PythonFullStack\Python-Hard-Way\AutomateTheBoringStuff\wrtingTest.txt", 'w')

myText = 'Hello ! this text for testing writing something in text file '

textFile.write(myText + "\n")
textFile.write("Test succeed!")