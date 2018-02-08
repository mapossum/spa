#Lecture
##Meeting 4 – Dictionaries and External Modules
####Today we will finish sequences (Dictionaries) and introduce a number of powerful external modules:

1. Dictionaries – Are a data type that is like a list, but the index can be almost any other non sequence type (although it is typically a string)
  1. Sometimes called hashtables or associative arrays.
  2. Consist of a key and a value.
    1. Keys must be unique
    2. Values can be any of any type
  3. Tuples are often used to store tabular information
    1. Can be used to build bar charts and histograms
  4. JSON (Javascript Object Notation)
2. Files – are the primary way to persist information that you want to keep around.
  1. Types of files – we will be using just text files for this class so skip the parts of the chapter that deal with "databases" and "pickeling".
  2. Reading files (section 9.1)
    1. Readline, readlines, read
    2. Strip function
	3. Split and Join Function
  3. Writing files
  4. Format operator
  5. Directories – the os module
    1. Exists, isdir, listdir
    2. Walk function from the book is helpful.
  6. Format operator
5. Other Topics 
  1. Try statement
  2. Raise statement
  3. Random numbers


link to Lecture and Lab:

2016 Lecture Video: https://www.youtube.com/watch?v=Tfgfp0X6AQE
2016 Lab Video: https://www.youtube.com/watch?v=kBlAEVH7S1E
2015 Video: https://www.youtube.com/watch?v=0v_D4A7WjUQ#t=3176
  
#Lab Assignment
##Exercise #4 – Using Objects, Dictionaries and Files

First we will write a point class simmilar to the one in the book on page 144 (we will do this in class so no need to turn in).

####Do the following assignment:

In this assignement you will turn in a single script, but the script will have several functions.
1. Write a function that takes the path to a text file as the only input parameter and then reads the lines of that textfile into a list or tuple (one line is one item in the list) and then returns the list or tuple.
2. Write a function that takes a list of cities and returns a dictionary where the keys are the city names and the values are the locations as a dictionary with x and y as keys and the point values as the values.  For this step you will re-use the function from last week that finds the location of a city.
3. Write a function that takes a dictionary of points (The output of #2 above), and a file location and writes the values to a text file that has the data in rows with the name of the city followed by the coordinate value.  

You can use the given list of cities for testing.  Feel free to make it smaller (just use the citiesSmall.txt until you want to test on larger set).

Please turn them in by emailing the python scripts to me at ghy.gis@gmail.com  

Name the script W_X_Y_Z.py 

where :
* W is your last name, 
* X is your first name, 
* Y is the Exercise number (in this case 1) and 
* Z is the script number (the first is 1 then second is 2 and so on). 


Thus for the first script to turn in, I would name the file Raber_George_4_1.py

You will turn in 3 scripts for this exercise.
      
      
      

