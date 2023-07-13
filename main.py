#Greeting Headline
print("••••••••••••••••••••••••••")
print("••••••••••••••••••••••••••")
print()
print("Welcome to @mzamudio2211's")
print("Car Customization Form")
print()
print("••••••••••••••••••••••••••")
print("••••••••••••••••••••••••••")

#Spacing
print()

#Question #1: Multiple Choice
print("Please enter the letter of the selection you're looking for: ")
print("** Make & Model **")
print("What model of car are you ordering?")
print("  a.Electric")
print("  b.Hybrid")
print("  c.Standard")
model = input("Please enter 'a' - 'c': ")

#Spacing
print()

#Question #2: Multiple Choice
print("** Exterior **")
print("What color vehicle would you prefer? Might vary depending on available stock.")
print("  a.Black")
print("  b.White")
print("  c.Red")
print("  d.Limited Edition - BARBIE PINK")
color = input("Please enter 'a' - 'd': ")

#Spacing
print()

#Question #3: Yes or No
print("** Interior **")
print("Would you like a sunroof?")
sunroof = input("Please enter \'yes\' or \'no\': ")

#Spacing
print()

#Question #4: Yes or No
print("** E-Z Pass Preference **")
print("For an extra charge of $30, would you like us to provide an E-Z Pass device for you?")
ezpass = input("Please enter \'yes\' or \'no\': ")

#Spacing
print()

#Question #5: Short-answer
print ("** Approx. Mileage **")
print("How many miles do you plan on driving weekly?")
terrain = input("Please enter your numeric answer: ")

#Spacing
print()

#Question #6: Short-answer 
print ("** Personalized Plates **")
print("Please note personalized plates should be between 3 and 7 digits/characters")
message = input ("If you would like a personalized plate, please enter your message here: ")

#Spacing
print()

#Summary Separator
print("===================")

#Summary
print("   ~ Summary ~ ")
print(f"Model: {model}")
print(f"Color: {color}")
print(f"Sunroof: {sunroof}")
print(f"E-Z Pass: {ezpass}")
print(f"Avg. Weekly Miles: {terrain}")
print(f"Personalized Plates: {message}")

#Spacing
print()