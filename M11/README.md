#Lecture
##Meeting 11 – Review and Final Exam Discussion 
##### Today we will cover a few more items related to external modules and cover the final exam.

1. You will be presented with a written test next time we meet (December 3rd).  It will be same format at the last exam.  To prevent some of the issues we had the last time, I will give you 3 hours to complete the exam (until 2:30pm). 
  1. Most of it will be looking at code snippets and interpreting what is happening.  
  2. The test will be open notes / open computers like the last one.
  3. The written portion of the exam will account for 50% of your final exam score (On the mid-term it was 70%). 
  4. The take home portion this time will be two scripts.  Each will account for 25% of your score.  We will start both as part of this class and go over strategy for completing each.  One will be turned in as a toolbox, the other as a Juypter notebook.
  

#Final Exam Scripting Part

You will write 2 scripts for your final exam.  The first should be turned in as a script tied to a toolbox, the other as a notebook.

**SCRIPT 1:**
You will write a python script that is attached to a tool a the toolbox. You must turn in both the script and the toolbox.  The tool will calculate lapse rate (described below) and return the modeled temperature as a new raster.  The tool will have as input a feature class (or feature layer) and allow the user to specify an output location for the output raster.  The scatterplot of the relationship should be saved in a directory specified by the user.
While air temperatures generally drop with increasing elevation, the amount of temperature change depends on how much water vapor the air mass is carrying. When water vapor condenses from a gas to a liquid, it releases all the heat that was originally necessary to evaporate it from a liquid to a gas. The release of this latent heat (“latent” means hidden) energy warms the air around it. This means a parcel of dry air (very low humidity) will cool off faster when it rises in elevation than a rising parcel of wet air (very high humidity).  The lapse rate is the degree of change in temperature per 1000 units of change in elevation.  The lapse rate can be derived empirically through linear regression.  In class I will demonstrate using python to find the linear relationship between two numpy arrays using regression.  You will combine this knowledge with what you already know to complete the assignment. 
The script that you will write will allow users to calculate the lapse rate for a given area (feature class).  You will calculate the lapse rate based on the provided raster data (elevation and temperature).  Do not include in your tool the ability to select the elevation and temperature raster datasets.  They should be “hard coded” into the script (i.e. there should be only two user defined parameters, one input and one output.  The output raster will be the predicted temperature given the lapse rate you provide.  
i.e. modeled temperature outputraster = slope(m)*Elevation + intercept(b)

Grading:
If your tool works (functions and returns the expected result) you will get an 85 out of 100.  You have the opportunity to earn extra points for completing the following:
1)	4 points for writing the scatterplot out to a file.
2)	2 points for writing the correlation coefficient and the actual lapse rate (slope * 1000) to the processing window as a message.
3)	4 points for styling your code to include a function that takes the path to the feature class and a path to the output raster.  It returns the message to be placed in the processing window).  Most of the logic for your script will then be contained within the function, but your script will need to call your function.  You will not get these points if all your logic is in the main body of the script.
4)	1 point if your solution is turned in before midnight on Dec 5th and 1 point before midnight on Dec 6th.
5)	3 Points for correctly inferring which of the three sample areas I included has the highest humidity.  Please include a one sentence description of why this is the case with your answer and what the lapse rate is for each area.
6)	NOTE that you cannot get credit for turning the assignment in early unless it is correct or only has minor errors (see below).  

You also will lose points for the following:
1)	1 point for each day past Dec 6th that you turn in the solution.  (must be turned in by the 13th which would be 7 points off).
2)	10 points off if your script is not built into a tool (executes only form IDLE).  This includes even if the script is built into a tool, but it does not execute as described (user must be able to specify input area and output location).
3)	Up to 30 points for an incorrect solution 
a.	5 points will be reduced for a solution that executes but has minor logic errors (one where you could still get the right answer, but you are still technically doing something wrong).
b.	15 points for a solution that executes but is missing a major component of logic and therefore produces an inaccurate solution(e.g. leaves off a step in the processing). 
c.	30 points for a partial solution that does not work entirely or leaves off most of the logic necessary to complete the assignment.

**SCRIPT 2:**
You will write a python script as a juypter notebook that creates a histogram of the values in a field of a feature class.  We will create a script together in class that creates a histogram using a simple list and and matplotlib. You will need to write the code that will read from a feature class.  You can use a search cursor to loop through all the values or create a pandas data frame from a feature class.  

Grading:
The grading will be same with the following exceptions.  
1)	Rather than the correlation coefficient and the lapse rate, display the mean and standard deviation of the values in the list. (Still 2 plus points)
2)	Include in your code a histogram function that takes a list and creates a histogram (still 4 plus points).
3)	Rather than correctly inferring an answer you can earn 3 extra points by including error checking logic that makes sure the field that was specified by the user is numeric and exits the script gracefully and reports the error to the user.  











  




      
      

