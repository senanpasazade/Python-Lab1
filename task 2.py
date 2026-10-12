a=int(input("enter birthdate:  "))
b=a%12
if b==0:
    c="monkey"
elif b==1:
    c="rooster"
elif b==2:
    c="dog"
elif b==3:
    c="pig"
elif b==4:
    c="rat"
elif b==5:
    c="ox"
elif b==6:
    c="tiger"
elif b==7:
    c="rabbit"
elif b==8:
    c="dragon"
elif b==9:
    c="snake"
elif b==10:
    c="horse"
else:
    c="sheep"
print("your Chinese Zodiac sign is: " , c )
