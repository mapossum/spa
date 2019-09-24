#Lecture
##Meeting 11 - More External Modules - Matpotlib for plotting data, and scipy for scientific anaylsis 
##### Today we will discuss how to use Matplotlib for plotting vector and raster data.

1. You will be presented with a take home written test next week (It will be posted on canvas).
  1. Most of it will be looking at code snippets and interpreting what is happening.  
  2. The test will be open notes / open computers like the last one.
  3. The written portion of the exam will account for 40% of your final exam score.
1. There are many external modules for python that can be useful in GIS.
  1. Flask - A web server (Demo a few these next week on a video)
  2. psycop2 - interface with database (cover SQL in Vector Course next semester)
  3. numpy - arrays (ndimage, etc), structured arrays - demo FeatureClassToNumPyArray and NumPyArrayToFeatureClass http://desktop.arcgis.com/en/arcmap/10.3/analyze/arcpy-data-access/featureclasstonumpyarray.htm
  4. scipy - do scientific operations
  5. and many more.  https://www.lfd.uci.edu/~gohlke/pythonlibs/
  6. matplotlib is a powerful library for plotting data (http://matplotlib.org/)
	1. Plots arrays (or array like objects such as python lists)
	2. Sometimes arrays have to be manipulated to be the correct dimensions.
	3. Often best start with an example and modify to what you want to do.
		1. Histograms
		2. Scatter Plot
  
Videos:

https://youtu.be/XxBVSAXTcSw
https://youtu.be/VQHCIy5ye6o


#Final Exam Programming Part

You will write 2 scripts for your final exam.  Both scripts should be submitted as tools in a single toolbox file.

**SCRIPT 1:**
You will write a python script that is attached to a tool in the toolbox.  The tool will calculate lapse rate (described below) and return the modelled temperature as a new raster.  The tool will have as input a feature class (or feature set) and allow the user to specify an output location for the output raster.  The scatterplot of the relationship should be saved in the same directory.
While air temperatures generally drop with increasing elevation, the amount of temperature change depends on how much water vapor the air mass is carrying. When water vapor condenses from a gas to a liquid, it releases all the heat that was originally necessary to evaporate it from a liquid to a gas. The release of this latent heat (“latent” means hidden) energy warms the air around it. This means a parcel of dry air (very low humidity) will cool off faster when it rises in elevation than a rising parcel of wet air (very high humidity).  The lapse rate is the degree of change in temperature per 1000 units of change in elevation.  The lapse rate can be derived imperially through linear regression.  In class I will demonstrate using python to find the linear relationship between two numpy arrays using regression.  You will combine this knowledge with what you already know to complete the assignment. 
The script that you will write will allow users to calculate the lapse rate for a given area (feature class).  You will calculate the lapse rate based on the provided raster data (elevation and temperature).  Do not include in your tool the ability to select the elevation and temperature raster datasets.  They should be “hard coded” into the script (i.e. there should be only two user defined parameters, one input and one output.  The output raster will be the predicted temperature given the lapse rate you provide.  
i.e. modeled temperature outputraster = slope(m)*x + intercept(b)

Grading:
If your tool works (functions and returns the expected result) you will get an 85 out of 100.  You have the opportunity to earn extra points for completing the following:
1)	4 points for allowing the user to define a custom area (feature set) rather than just a feature class.
2)	2 points for writing the correlation coefficient and the actual lapse rate (slope * 1000) to the processing window as a message.
3)	4 points for styling your code to include a function that takes the path to the feature class and a path to the output raster.  Most of the logic for your script will then be contained within the function, but your script will need to call your function.  You will not get these points if all your logic is in the main body of the script.
4)	1 point if your solution is turned in before midnight on May 2nd and 1 point before midnight on May 1st.
5)	3 Points for correctly inferring which of the three sample areas I included has the highest humidity.  Please include a one sentence description of why this is the case with your answer and what the lapse rate is for each area.
6)	NOTE that you cannot get credit for turning the assignment in early unless it is correct or only has minor errors (see below).  

You also will lose points for the following:
1)	1 point for each day past May 3rd that you turn in the solution.  (must be turned in by the 10th which would be 7 points off).
2)	5 points off if your script is not built into a tool (executes only form IDLE).  This includes even if the script is built into a tool, but it does not execute as described (user must be able to specify input area and output location).
3)	Up to 30 points for an incorrect solution 
a.	5 points will be reduced for a solution that executes but has minor logic errors (one where you could still get the right answer but you are still technically doing something wrong).
b.	15 points for a solution that works but is missing a major component of logic (e.g. leaves off a step in the processing). 
c.	30 points for a partial solution that does not work entirely or leaves off most of the logic necessary to complete the assignment.

**SCRIPT 2:**
You will write a python script that you will build into a tool in your toolbox that has as input a single feature class and lets the user also choose a field.  Then using the histogram code that was demonstrated in class you must create a histogram of the values in that field.  You will need to use a search cursor to loop through all the values, find the value from the specified field and then store that value in a list.  Finally, after the loop the script will create and display the histogram.

Grading:
The grading will be same with the following exceptions.  
1)	Rather than the correlation coefficient and the lapse rate, display the mean and standard deviation of the values in the list. (Still 2 plus points)
2)	Include in your code a histogram function that takes a list and creates a histogram (still 4 plus points).
3)	Rather than correctly inferring an answer you can earn 3 extra points by including error checking logic that makes sure the field that was specified by the user is numeric and exits the script gracefully and reports the error to the user.  











  




      
      

