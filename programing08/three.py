''' The Unix grep command searches a file and outputs the lines in the file that
contain a certain pattern. Write an implementation of this. It will take two
command-line arguments: the first is the string to look for, and the second is the
file name. The output should be the lines in the file that contain the string.'''
import sys

def grep(pattern, filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        found = False
        for line_num, line in enumerate(lines, start=1):
            if pattern in line:
                print(f"Line {line_num}: {line.strip()}")
                found = True
        
        if not found:
            print(f"No lines containing the pattern '{pattern}' were found in the file.")
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python grep.py <pattern> <filename>")
    else:
        grep(sys.argv[1], sys.argv[2])
