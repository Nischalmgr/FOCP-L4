'''The Unix spell command is a simple spell-checker. It prints out all the words in a
text file that are not found in a dictionary. Write and test an implementation of this,
that takes a file name as a command-line argument.
Note: You may want to simplify the program at first by testing with a text file that
does not contain any punctuation. A complete version should obviously be able to
handle normal files, with punctuation.
Another Note: You will need a list of valid words. Linux users will already have one
(probably in /usr/share/dict/words). It is more complicated, as usual, for
Windows users. Happily, there are several available on GitHu'''
import sys
import string
def load_dict(file):
    try:
        with open (file,'r') as file:
            return set(word.strip().lower() for word in file.readlines())
    except FileNotFoundError:
        print(f" error: file{file} not found")
        sys.exit(1)
    except Exception as e:
        print(f"unexcepted error ocuured wile loadiig as", e)
        sys.exit(1)
def check_spelling(filename,dictionary):
    try: 
        with open(filename, 'r') as file:
            content=file.read()
            trans=str.maketrans('','',string.punctuation)
            words=content.translate(trans).split()
            misspelled_words=[word for word in words if word.lower()not in dictionary]
            if misspelled_words:
                print("misspelled words")
                for word in misspelled_words:
                    print(word)
            else:
                print("no misspelled woerds")
    except FileNotFoundError:
        print(f"{file} not found")
    except Exception as e:
        print("error due to ",e)
if __name__=="__main__":
    if len(sys.argv)!=3:
        print("usage: five.py <file1> <file2>")
    else:
        dict=load_dict(sys.argv[2])
        check_spelling(sys.argv[1],dict)


