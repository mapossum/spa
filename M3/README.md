#Lecture
##Meeting 3 – Sequences
####Today we will discuss a number of data types that allow for grouping of sets of information (sequences):

1. Strings – We already know what strings are, but…
  1. Strings are really just sets of characters (sequence of characters).
    1. Characters are just numbers that have been told they represent a character (ASCII, Unicode etc).
  2. Generic sequence operations:
    1. Accessing items in a sequence []
    2. len() – length operator
    3. Traversal with a for loop
    4. Slices
    5. in operator
  3. String Operators:
    1. Upper
    2. Lower
    3. Replace
    4. Find
    5. ==
    6. Split (turns into a list)
  4. Immutable vs mutable
2. Lists – Another type of sequence that is a sequence of anythings
  1. Elements are items in a list
  2. Elements can be any data type (you can even have lists of lists)
  3. Lists are mutable
  4. List operations
    1. Items above listed under generic sequence operations
    2. Pop (removes and returns at index)
    3. Append (adds to bottom of the list)
    4. Remove (removes the first occurrence of a specific value)
    5. Sort 
    6. Join
  5. Lists inside of functions (objects vs values)
3. Tuples – Similar to lists with some important differences
  1. Tuples are immutable
  2. Tuples are useful for the following situations:
    1. Tuple assignment is different
    2. Tuples can be returned from a function
    3. Gathering and scattering using *	
4. Sequence Skills:
  1. Sequence functions
    1. Counting occurrences
    2. Reduce functions
      1. Totals (accumulator)
      2. Means
      3. Standard Deviation (review what this means)
    3. Map functions
    4. Filter functions
    5. Special functions
      1. zip function
      2. range function
      3. enumerate function

    
2015 - Lecture Video: https://www.youtube.com/watch?v=5rDnqBTlt_Y&x-yt-ts=1422327029&x-yt-cl=84838260


#Lab Assignment
##Exercise #3 – Sequences

####Do the following assignments:

1. Write a simple functions that takes a list of numbers and does the following:
  1. Checks that the list is in fact a list of just numbers, and if not returns only a value of None.  If true returns each of the following as a tuple:
  2. Returns the sum.
  3. Returns the mean.
  4. Returns Standard Deviation
  * Test this function above by creating a program to generate a report of the return values.
2. The function included with this lab uses a module to find the latitude and longitude of a city or address.  Modify the last program from last week to take a list of cities (as strings e.g. “Hattiesburg, MS”) and report the distance along a path that traverses the entire list (your list should include at least 5 cities).  
3. Modify the script from above to include the function you wrote from Script 1 so that the user is also give the mean, standard deviation of all the legs.

Please turn them in by emailing the python scripts to me at ghy.gis@gmail.com  

Name the script W_X_Y_Z.py 

where :
* W is your last name, 
* X is your first name, 
* Y is the Exercise number (in this case 1) and 
* Z is the script number (the first is 1 then second is 2 and so on). 

2016 Video: https://www.youtube.com/watch?v=lcLgSmgPjkA#t=3769
2015 Video: https://www.youtube.com/watch?v=5rDnqBTlt_Y&x-yt-cl=84838260&x-yt-ts=1422327029 

Thus for the first script to turn in, I would name the file Raber_George_3_1.py

You will turn in 3 scripts for this exercise.
      
      
      

