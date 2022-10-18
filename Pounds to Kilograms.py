str_kilograms=input("Please enter the number of kilograms you wish to convert: ")
float_kilograms=float(str_kilograms)
pounds=float_kilograms//(0.45359237)
pounds_remain=float_kilograms/(0.45359237)-pounds
ounces=pounds_remain*16
print(float_kilograms,"kilograms is",int(pounds),"pounds and",ounces,"ounces.")
