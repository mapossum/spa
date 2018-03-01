name1 = raw_input("What is the name? ")
name2 = "George"  #"GEORGE"

if (name1 == name2):
    print "Correct!"
elif (name1.upper() == name2.upper()):
    print "You typed the same name, but didn't capitalize!"
else:
    print "Wrong"

print "done"
