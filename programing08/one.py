'''The Unix nl command prints the lines of a text file with a line number at the start
of each line. (It can be useful when printing out programs for dry runs or white-box
testing). Write an implementation of this command. It should take the name of the
files as a command-line argument.

 
'''
import sys
def main():
    if len(sys.argv)  !=2:
        print("write one file name eg: python nl.py <filename>")
        sys.exit(1)

    filename=sys.argv[1]
    try:
        with open(filename,'r') as file:
            lines=file.readlines()
        for num,line in enumerate(lines, start=1):
            print(f"{num} {line.rstirp()}")
    except FileNotFoundError:
        print(f"Error: file '{filename}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"eroor due to {e}")
        sys.exit(1)
if __name__=="__main__":
    main()



