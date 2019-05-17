weight=85
height=1.85
body_mass_index=weight/(height**2)

print(body_mass_index)
if body_mass_index < 20:
    print("low weight")

if 20 < body_mass_index < 25:
    print("normal")

if body_mass_index > 25:
    print("over weight")

