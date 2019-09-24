#Lecture
##Meeting 6 � Python in ArcGIS (arcpy) - Building Toolboxes
####Today we will continue to discuss arcpy, specifically, how to connect the scripts we make to Toolboxes:

Making a toolbox:
One of the most useful things you can do with a script it to create a toolbox and tools that gather the input parameters and execute your script from within ArcGIS.  Doing this allows you to share your tools with others and truly customize the arcGIS experience.

A toolbox is basically just a file with a .tbx extension.  A toolbox that a user creates is called a custom toolbox.  These exist on your computer in a location that you specify.  Toolboxes contain tools.  Tools can be connected to scripts so that executing one will run the script in the process.  We will walk through the process of creating a script tool and hooking a script up to it.

1. Use of arcpy.GetParameterAsText and arcpy.GetParameter
2. arcpy.GetArgumentCount()
3. Creating a toolbox in ArcGIS
  1. Script Tools
  2. Building to Script Tool
    1. Input and Output Types
	2. Everything is passed around as strings
4. Use of SetParameterAsText and SetParameter

The lab assignement for this week is simply to take the assignement from last week and turn it into a script tool within a toolbox.

Youtube Lecture Video: https://youtu.be/6EZg9ABz0B0
Youtube Lab Video: https://youtu.be/mdyYhzUWb_U

Old Youtube Video:  https://www.youtube.com/watch?v=2W6di6SwNYg




      
      

