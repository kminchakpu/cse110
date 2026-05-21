# Example 3
import math
def main():
  radius = float(input("Enter the radius of a circle: "))
  area = circle_area(radius)
  print(f"area: {area:.1f}")
def circle_area(radius):
  area = math.pi * radius * radius
  return area
main()

# Example 4
import math
def main():
  radius = float(input("Enter the radius of a circle: "))
  area = circle_area(radius)
  print(f"area: {area:.1f}")
def circle_area(radius):
  area = math.pi * radius * radius
  return area
main()

# Example 5
import math
def main():
  # Call the arc_length function with only one argument
  # even though the arc_length function has two parameters.
  len1 = arc_length(4.7)
  print(f"len1: {len1:.1f}")
  # Call the arc_length function again but
  # this time with two arguments.
  len2 = arc_length(4.7, 270)
  print(f"len2: {len2:.1f}")
# Define a function with two parameters. The
# second parameter has a default value of 360.
def arc_length(radius, degrees=360):
  """Compute and return the length of an arc of a circle"""
  circumference = 2 * math.pi * radius
  length = circumference * degrees / 360
  return length
main()

"""Compute and print the volume of a right circular cone."""
# Import the standard math module so that
# math.pi can be used in this program.
import math
def main():
  # Call the cone_volume function to compute
  # the volume of an example cone.
  ex_radius = 2.8
  ex_height = 3.2
  ex_vol = cone_volume(ex_radius, ex_height)
  # Print several lines that describe this program.
  print("This program computes the volume of a right")
  print("circular cone. For example, if the radius of a")
  print(f"cone is {ex_radius} and the height is {ex_height}")
  print(f"then the volume is {ex_vol:.1f}")
  print()
  # Get the radius and height of the cone from the user.
  radius = float(input("Please enter the radius of the cone: "))
  height = float(input("Please enter the height of the cone: "))
  # Call the cone_volume function to compute the volume
  # for the radius and height that came from the user.
  vol = cone_volume(radius, height)
  # Print the radius, height, and
  # volume for the user to see.
  print(f"Radius: {radius}")
  print(f"Height: {height}")
  print(f"Volume: {vol:.1f}")
def cone_volume(radius, height):
  """Compute and return the volume of a right circular cone."""
  volume = math.pi * radius**2 * height / 3
  return volume
# Start this program by
# calling the main function.
main()