def convert_temperature(value, scale):
    if scale.lower() == "c":
        f = (value*9/5) + 32
        k = value + 273.15
        print(f"{value}C = {f:.2f}F = {k:.2f}K")
    elif scale.lower() == "f":
        c = (value-32)*5/9
        k = c + 273.15
        print(f"{value}F = {c:.2f}C = {k:.2f}K")
    elif scale.lower() =="k":
        c = value - 273.15
        f = (c*9/5) + 32
        print(f"{value}K = {c:.2f}C = {f:.2f}F")
        print("Invalid scale! use C,F, or K.")
    temp = float(input("Enter temperature value:"))  
    scale = input("Enter scale (C/F/K):")
    convert_temperature(temp,scale)     
