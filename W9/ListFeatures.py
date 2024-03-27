import arcpy

# Set the workspace for ListFeatureClasses
arcpy.env.workspace = arcpy.GetParameterAsText(0)

# Use the ListFeatureClasses function to return a list of
#  shapefiles.
featureclasses = arcpy.ListFeatureClasses()

# Copy shapefiles to a file geodatabase
for fc in featureclasses:
    arcpy.AddMessage(fc)

arcpy.SetParameterAsText(1, featureclasses)
