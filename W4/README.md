#Lecture
##Meeting 4 – Sequences
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
5. Dictionaries – Are a data type that is like a list, but the index can be almost any other non sequence type (although it is typically a string)
  1. Sometimes called hashtables or associative arrays.
  2. Consist of a key and a value.
    1. Keys must be unique
    2. Values can be any of any type
6. Arrays (Numpy)
  1. Numpy
  2. Vanillia Arrays (how are they different from arrays)
  3. Structured Arrays (how are they different from dictionaries)
7. Classes and Objects
  1. We've already been using these
  2. What is a class and what is an object
  3. How do you create a class? (Not going to really cover in this class).
  4. How do you use a class (How do you create an object).
  5. Again, in this class we will mostly be consumers of classes and objects other's have written, but if it helps you to orgainze things go ahead and create your own.
  8. Files – are the primary way to persist information that you want to keep around.
  9. Types of files – we will be using just text files for this class so skip the parts of the chapter that deal with "databases" and "pickeling".
	1. Writing files
	2. Format operator
  10. Directories – the os module
    1. Exists, isdir, listdir
    2. Walk function from the book is helpful.
8. Other Topics 
  1. Try statement
  2. Raise statement
  3. Random numbers


Other Videos to Watch:
1. https://youtu.be/WKs-vN2cjk0 (Strings)
1. https://youtu.be/R-HLU9Fl5ug (Sequences)
2. https://youtu.be/cKlnR-CB3tk (Lambda, Map, Filter, Reduce)
3. https://youtu.be/8Mpc9ukltVA (Numpy)
 

#Lab Assignment
##Exercise #4 – Sequences

####Do the following assignment:

1. Complete the exercises on the Notebooks from the lecture.

2. Use the included points2 file.  Read in the data into an array or list. Compile the following statistics for each column (must work even if there are more columns) as a tuple and then report them to the screen using the tuple:
  1. Min.
  2. Mean.
  3. Standard Deviation.

3. Use the included points2 file.  Read in all the points into an array or list.  Then write a function that calculates the standard distance.  Your function should take two paramaters and return a tuple:
  1. Checks that the list is in fact a list of just numbers, and if not returns only a value of None.  If true returns each of the following as a tuple:
  2. Returns the sum.
  3. Returns the mean.
  4. Returns Standard Deviation
  * Test this function above by creating a program to generate a report of the return values.

Please turn them in by using Canvas.

You will turn in 2 scripts for this exercise.
      
      
      

