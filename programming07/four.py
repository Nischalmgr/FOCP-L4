''' One approach to analysing some encrypted data where a substitution is suspected
is frequency analysis. A count of the diﬀerent symbols in the message can be used
to identify the language used, and sometimes some of the letters. In English, the
most common letter is "e"
, and so the symbol representing "e" should appear most
in the encrypted text.
Write a program that processes a string representing a message and reports the six
most common letters, along with the number of times they appear. Case should
not matter, so "E" and "e" are considered the same.
Hint: There are many ways to do this. It is obviously a dictionary, but we will want
zero counts, so some initialisation is needed. Also, sorting dictionaries is tricky, so
best to ignore that initially, and then check the usual resources for the runes.'''
 
while True:
    message=input("enter the message")
    message=message.lower()
    final="".join(message)
    counts={}
    for letter in final:
        counts[letter]=counts.get(letter,0)+1
    sorted_list=sorted(counts.items(), key=lambda x : x[1], reverse=True )
    final_list=sorted_list[:6]
    for word, count in final_list:
        print(f"{word} : {count}")
    con=input("do you want to continue?")
    con=con.lower()
    if con=='n':
        break


