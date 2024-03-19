import arcpy

def saveAnimal(lop):
    array = arcpy.Array(lop)
    polyline = arcpy.Polyline(array)
    return polyline

fc = r'C:\temp\spaLab\week8\tracks.gdb\GPS_Points'
fields = ['Time', 'Animal', 'SHAPE@XY']
#Create a feature class with the right fields and
#fcPath = STUFF


#Create Insert cursor
Pathcursor = arcpy.da.InsertCursor(fcPath, ["SHAPE@", Animal])

#setup some variables
iAnimal = -1
currentPoints = []

with arcpy.da.SearchCursor(fc, fields, None, None, None, (None, "ORDER BY Animal, Time")) as cursor:
    for row in cursor:
        #print(u'{0}, {1}, {2}'.format(row[0], row[1], row[2]))
        if iAnimal == -1:
            iAnimal = row[1]
            
        if iAnimal != row[1]:
            #get current animal path as polyline
            animalpath = saveAnimal(currentPoints)

            #save it using insert cursor
            print currentPoints, iAnimal
            Pathcursor.insertRow([polyline, iAnimal])

            #Empty list
            currentPoints = []

        #Store the current point in the current polyline
        
        currentPoints.append(arcpy.Point(row[2][0], row[2][1]))
        iAnimal = row[1]

animalpath = saveAnimal(currentPoints)

#save it using insert cursor
print currentPoints, iAnimal


    
