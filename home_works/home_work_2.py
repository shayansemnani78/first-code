text=input("You rather to use SI or Imperial ? Answer with exact words ")
if text=="SI" :
    weight = input("pls enter your weight!!!")
    weight = float(weight)
    height = input("pls input your height")
    height = float(height)
    BMI = weight / (height ** 2)

    if BMI < 20:
        print("Underwight")

    elif 18.5 <= BMI < 25:
        print("Normal")
    elif 25 <= BMI < 30:
        print("Overweight")
    elif BMI > 30:
        print("Obesity")
    else:
        print("Not true inputs")

elif text=="Imperial" :
    weight = input("pls enter your weight!!!")
    weight = float(weight)
    height = input("pls input your height")
    height = float(height)
    BMI = (weight / (height ** 2)) * 703

    if BMI < 20:
        print("Underwight")

    elif 18.5 <= BMI < 25:
        print("Normal")
    elif 25 <= BMI < 30:
        print("Overweight")
    elif BMI > 30:
        print("Obesity")
    else:
        print("Not true inputs")
else :
    print("pls check your answer!!!")


