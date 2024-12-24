''' Write a program that manages a list of countries and their capital cities. It should
prompt the user to enter the name of a country. If the program already "knows"
the name of the capital city, it should display it. Otherwise it should ask the user to
enter it. This should carry on until the user terminates the program (how this
happens is up to you 
Note: A good solution to this task will be able to cope with the country being entered
variously as, for example,
"Wales"
"wales"
"WALES" and so on. '''
countries={}
print("welcome ")
while True:
    enter= input("enter the country to see its capital;")
    coutry=enter.title

    if enter  in countries:
        print(f"{enter} capital is {countries[enter]}")
    else:
        print("no capital known ")
        capital=input("enter the capital")
        countries[enter]=capital.strip()
        print(f"{enter} capital {countries[enter]}")
    continuee=input("do you want to contine (y/n)")
    if continuee.lower() =="n":
        break


        

        
