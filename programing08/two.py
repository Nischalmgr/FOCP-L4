'''The Unix diff command compares two files and reports the diﬀerences, if any.
Write a simple implementation of this that takes two file names as command-line
arguments and reports whether or not the two files are the same. (Define "same" as
having the same contents.)   
---'''
import sys
def compare_files(file1,file2):
    try:
        with open(file1,'r') as f1 , open (file2,'r') as f2:
            content1=f1.readlines()
            content2=f2.readlines()
            if content1==content2:
                print(f"file{file1} and file {file2}are same")
            else:
                for i ,(line1,line2) in enumerate(zip(content1,content2), start=1):
                    if line1!=line2:
                        print(f" line {i} differs:\n  File1:{line1.strip()}\n Filename:{line2.strip()}")

                if len(content1)>len(content2):
                    print(f"{file1 } has extra lines starting at line {len(content2)}")
                elif len(content2) > len(content1):
                    print(f"{file2} has extra lines starting at line {len(content1) + 1}.")
    except FileNotFoundError:
        print("error")
    except Exception as e:
        print("error due to",e)
if  __name__=="__main__":
    if len(sys.argv) !=3:
        print("usage: use python3.12 two.py <file1> <file2>")
    else:
        compare_files(sys.argv[1],sys.argv[2])