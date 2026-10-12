a=int(input("enter weight (kq)  "))
b=input("enter height (m)   ")
c=float(b)
BMI=a/(c*c)
if BMI < 18.5 or BMI==18/5:
    print("underweight")
elif BMI <24.5 :
    print("normal weight")
elif BMI < 29.9:
    print("over weight")
else:
    print("obese")
