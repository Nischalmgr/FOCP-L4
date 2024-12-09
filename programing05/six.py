import shutil
import os
import sys
def check_file(file):
    if not os.path.isfile(file):
        print("file doesnot exist")
        return
    new_file=file + "backup"
    try:
        shutil.copy(file,new_file)
        print("coopied succesfully")
    except Exception as e:
        print(f"the file could not be run due to {e}")

file=sys.argv
if len (file)!=2:
    print("enter a file for backup")
else :
    check_file(file[1])