
temperture = input("Enter Temperture like This 43F, 105C : ")

temp_degree = int(temperture[:-1])
conv = temperture[-1]

if conv.upper() == "C":
  result = int(round((9 * temp_degree) / 5 + 32))
  c = "Fahrenheit"
elif conv.upper() == "F":
  result = int(round((temp_degree - 32) * 5 / 9))
  c = "Celsius"
else:
  print("Input proper convention.")
  quit()
print("The temperature in", c, "is", result, "degrees.")