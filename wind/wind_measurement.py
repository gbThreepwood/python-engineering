import math
import csv
import string


# To bee replaced by sensor data
with open('wind.csv') as csvfile:
  reader = csv.DictReader(csvfile)
  try:
    for row in reader:
      windspeed = string.atoi(row['speed'])
      winddir = string.atoi(row['direction'])
      print(row['speed'], row['direction'])
  except csv.Error as e:
      sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))

def deg2rad(deg):
  return deg*math.pi/180

def rad2deg(rad):
  return rad*180/math.pi

def average(wind):
  return wind

print average(reader)
print deg2rad(winddir)