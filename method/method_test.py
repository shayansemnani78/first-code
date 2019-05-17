weight = input("pls enter your weight :")
height = input("pls enter your height :")
weight = int(weight)
height = float(height)
body_mass_index = weight/(height**2)

print(body_mass_index)
if body_mass_index <= 20:
    print("low weight")

elif 20 < body_mass_index <= 25:
    print("normal")

else:
    print("over weight")

