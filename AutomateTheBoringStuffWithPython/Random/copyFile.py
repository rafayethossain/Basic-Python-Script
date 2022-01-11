import shutil


src = 'D:\PythonFullStack\Python-Hard-Way\copyTest.txt'
dst = 'D:\PythonFullStack\Python-Hard-Way\AutomateTheBoringStuff'

shutil.copy(src, dst)

# .copytree()  # to copy folder
# .move() # moving a folder
# shutil.copy(src,dst) 
print("\n")

print("Disk Usage:", shutil.disk_usage(dst))