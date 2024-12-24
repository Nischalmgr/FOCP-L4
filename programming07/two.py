''' Write and test three functions that each take two words (strings) as parameters and
return sorted lists (as defined above) representing respectively:
Letters that appear in at least one of the two words.
Letters that appear in both words.
Letters that appear in either word, but not in bot '''
def appear_at_least_once(word1,word2):
    return(sorted(set(word1 | word2))) 
def appear_both(word1,word2):
    return(sorted(set(word1 & word2))) 
def either_but_not_both(word1,word2):
    return(sorted(set(word1 ^ word2))) 

word1="apple"
word2="planet"
print("letters in at least one word: ",appear_at_least_once(word1,word2))
print("letters iin both words: ", appear_both(word1,word2))
print("letters in either but not both: ", either_but_not_both(word1,word2))


