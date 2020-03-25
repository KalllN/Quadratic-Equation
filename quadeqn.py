print("Enter roots of quadratic equation: ", end = "")
a, b, c = map(int, input().split())
d = (b**2) - (4*a*c)
if d > 0:
  x1 = (-b + (d**0.5)) / (2*a)
  x2 = (-b - (d**0.5)) / (2*a)
  print("The roots of the equation are: ", "{0:.2f}".format(x1), "and", "{0:.2f}".format(x2))
elif d < 0:
  x1 = (-b + (abs(d)**0.5)) / (2*a)
  x2 = (-b - (abs(d)**0.5)) / (2*a)
  print("The roots are imaginary:", "{0:.2f}".format(x1), end = "i and ")
  print("{0:.2f}".format(x2), end="i\n")
else:
  print("Only one root:", "{0:.2f}".format(x1))
