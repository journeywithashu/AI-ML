age = 21

if age >= 18:
     print("you can drive")
     print("you can vote")
else:
     print("you can't vote")


color = input("enter color: ")

if color == "red":
     print("Stop")
elif color == "green":
     print("go") 
elif color == "yellow":
     print("look")
else:
     print("wrong color for traffic light")


#matchcase

color = input("enter color: ")

match color:
     case "Green":
          print("Go")
     case "Yellow":
          print("Look")
     case "Red":
          print("Stop")
     case _:
          print("Wrong color!")
