eng2Span = {"dog": "perro", "horse": "cabillo", "cat": "gato"}

inWord = input("Enter an English Noun and I'll give you the Spanish Word:")

if inWord.lower() in eng2Span:
    print("The spanish word for {} is {}".format(inWord, eng2Span[inWord.lower()]))
else:
    print("Sorry I don't the spanish for {}.".format(inWord))
                                    
                                                 
