#Lecture
##Meeting 12 – Python in ArcGIS (arcpy) - Building Toolboxes
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

The lab assignement for this week is to take assignement from watersheds and census assigment (week 6) and turn it into a script tool within a toolbox.

Your toolbox and must allow the user to specify the following paramaters (has to have 5 paramaters):
1) The feature class representing the aggregation polygons (in our case watersheds)
2) the field from this feature class representing a label or unique ID for those features on which to aggregate or dissolve.
3) The feature class representing the data to be aggregated (in our case cencus tracts).
4) The field from this feature class represening the values to be aggregated (in this case the population).
5) The location of the output feature class. (This is an output paramater, but is not derived.)





      
      

