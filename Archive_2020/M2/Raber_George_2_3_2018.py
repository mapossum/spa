import math

def recalculate_coordinate(val,_as=None):
  """
    Accepts a coordinate as a tuple (degree, minutes, seconds)
    You can give only one of them (e.g. only minutes as a floating point number) and it will be duly
    recalculated into degrees, minutes and seconds.
    Return value can be specified as 'deg', 'min' or 'sec'; default return value is a proper coordinate tuple.
  """
  deg,  min,  sec = val
  # pass outstanding values from right to left
  min = (min or 0) + int(sec) / 60
  sec = sec % 60
  deg = (deg or 0) + int(min) / 60
  min = min % 60
  # pass decimal part from left to right
  dfrac,  dint = math.modf(deg)
  min = min + dfrac * 60
  deg = dint
  mfrac,  mint = math.modf(min)
  sec = sec + mfrac * 60
  min = mint
  if _as:
    sec = sec + min * 60 + deg * 3600
    if _as == 'sec': return sec
    if _as == 'min': return sec / 60
    if _as == 'deg': return sec / 3600
  return deg,  min,  sec
      

def points2distance(slong, slat, elong, elat):
  """
    Calculate distance (in kilometers) between two points given as (long, latt) pairs
    based on Haversine formula (http://en.wikipedia.org/wiki/Haversine_formula).
    slong = Starting Longitude
    slat = Starting Latitude
    elong = ending Longitude
    elat = Ending Latitude
  """
  start = ((slong,0,0),(slat,0,0))
  end = ((elong,0,0),(elat,0,0))
  start_long = math.radians(recalculate_coordinate(start[0],  'deg'))
  start_latt = math.radians(recalculate_coordinate(start[1],  'deg'))
  end_long = math.radians(recalculate_coordinate(end[0],  'deg'))
  end_latt = math.radians(recalculate_coordinate(end[1],  'deg'))
  d_latt = end_latt - start_latt
  d_long = end_long - start_long
  a = math.sin(d_latt/2)**2 + math.cos(start_latt) * math.cos(end_latt) * math.sin(d_long/2)**2
  c = 2 * math.asin(math.sqrt(a))
  return 6371 * c


#This is an Example of how it could be used
print points2distance(-89.342 , 32.3, -90.233, 24.4)


firsttime = True
totaldistance = 0
keepgoing = True

while(keepgoing):

    #Have the user give us a point as two numebers (X and Y)

    x = float(raw_input("X value for point along line:"))
    y = float(raw_input("Y value for point along line:"))

    #Test if there is a previous x and y and if not assign one
    if firsttime:
        prex = x
        prey = y
    
    firsttime = False
    
    #Figure out the distance from current point to the previous point

    cdist = points2distance(prex,prey,x,y)
    print cdist, prex, prey, x, y
    
    #Add that distance to the running total

    totaldistance = cdist + totaldistance

    #Find out if they want to continue

    cont = raw_input("Do you want to continue? (Enter Y to keep going)")

    #If they want to continue ask for another point

    if (cont == "Y"):
        prex = x
        prey = y
    else:
        #If not report the total distance
        print totaldistance
        keepgoing = False
    
