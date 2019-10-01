
import arcpy

#What inputs are we going to allow the user to specify
watersheds = r"C:\temp\LabData.gdb\watersheds"
census = r"C:\temp\LabData.gdb\ctracts"
int1 = r"in_memory\int"
output = r"C:\temp\LabData.gdb\watersheds_w_pop2"

#Set Up Arcpy.GetParamaters
watersheds = arcpy.GetParameterAsText(0)
census = arcpy.GetParameterAsText(1)
output = arcpy.GetParameterAsText(2)
dissolvefield = "HUC_8"

arcpy.AddMessage("{0} will be overlayed with {1} and then dissolved and the population will be summariezed in the output file: {2}.".format(watersheds,census,output))


#Write Code Logic

#overlay watersheds and census data
arcpy.Identity_analysis(watersheds, census, int1)

#dissolve output data into new data using watershed field
arcpy.Dissolve_management(int1, output, [dissolvefield], [["P0010001", "SUM"]])

#Results! No Need to set because it is not derived





