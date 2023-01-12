import math 

#Function for menu options
def MainMenu():
  print("Press [1] to calculate circle area")
  print("Press [2] to calculate circle circumference")
  print("Press [3] to calculate square area")
  print("Press [4] to calculate square perimeter")
  print("Press [5] to calculate cuboid volume")
  print("Press [6] to calculate cuboid surface area")
  print("Press [0] to exit the program")

#Call function menu will be displayed
MainMenu()

#Define a function to calculate circle area 
def CircleArea(): 
  radius = float(input("Enter the radius of the circle: "))
  area = math.pi * (radius ** 2)
  #convert int to float because argument asks to convert int to floa
  float_area = float(area)
  #variable is outside after a comma
  print("The Circle area is ", float_area) 

#Define a function to calculate circle circumference 
def CircleCircumference():
    CircumferenceRadius = float(input(" Enter the radius of the circle: "))
    circumference = 2 * math.pi * CircumferenceRadius
    float_circumference = float(circumference)
    print ("The circle circumference is", float_circumference) 

#Calculate square area function 
def SquareArea (): 
  side = float(input("Enter the lenght of the square: "))
  area = side * side 
  float_area = float(area)
  print("The square area is ", float_area ) 

#Define a function to calculate square perimeter 
def SquarePerimeter(): 
  side = float(input("Enter the lenght of the square: "))
  perimeter = 4 * side 
  float_perimeter = float(perimeter) 
  print("The square perimeter is ", float_perimeter)

#Define a function to calculate cuboid volume 
def CuboidVolume(): 
  length = float(input("Enter the length of the cuboid: "))
  width = float(input("Enter the width of the cuboid:  "))
  height = float(input("Enter the height of the cuboid:" ))
  volume = length * width * height 
  float_volume = float(volume)
  print ("The cuboid volume is ", float_volume)

#Define a function to calculate cuboid surface area 
def CuboidSurfaceArea(): 
  length = float(input("Enter the lenght of the cuboid: "))
  height = float(input("Enter the height of the cuboid:"))
  width = float(input("Enter the width of the cuboid: "))
  surfaceArea = 2 * (length * width + width * height + length * height)
  float_surfaceArea = float(surfaceArea)
  print("The Cuboid surface area is ", float_surfaceArea)

#Awaiting for user`s input to select what option. 
options = int(input("Enter your option: "))

#validation to repeat menu and options 
while options != 0: 
  if options == 1: 
    CircleArea()
    pass
  elif options == 2: 
    CircleCircumference()
    pass 
  elif options == 3: 
    SquareArea()
    pass 
  elif options == 4: 
    SquarePerimeter()
    pass
  elif options == 5:
    CuboidVolume()
    pass 
  elif options == 6: 
    CuboidSurfaceArea()
    pass 
  else: 
    print("Oops! It is not a valid answer, try again.")

  MainMenu()
  options = int(input("Enter your option: "))


print("You pressed exit the program, thank you bye.")
