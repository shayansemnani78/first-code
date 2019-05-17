weight = 85
height = 1
body_mass_index = weight/(height**2)

print(body_mass_index)
if body_mass_index < 20:
    print("low weight")

elif 20 < body_mass_index < 25:
    print("normal")

else:
    print("over weight")

