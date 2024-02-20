# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1_lower = name1.lower()
name2_lower = name2.lower()

name = name1_lower + name2_lower

t_count = name.count("t")
r_count = name.count("r")
u_count = name.count("u")
e_count = name.count("e")

l_count = name.count("l")
o_count = name.count("o")
v_count = name.count("v")
e_count = name.count("e")

true_count = t_count + r_count + u_count + e_count
love_count = l_count + o_count + v_count + e_count

true_count_string = str(true_count)
love_count_string = str(love_count)

true_love_string = true_count_string +love_count_string
print(true_love_string)
true_love = int(true_love_string)
print(true_love)

if true_love<10 and true_love>90:
  print(f"Your scores is {true_love} , you go together like coke and mentos.")
  
elif true_love>40 and true_love<50:
  print(f"Your score is {true_love}, you are alright together, though one of you is a player !!")
  
elif true_love>50 and true_love<65:
  print(f"Your score is {true_love} , You guys are good together but with alot of dramas in the house")

elif true_love>65 and true_love<80:
  print(f"Your score is {true_love}, You guys are best together , much strong with each other")

elif true_love>80 and true_love<90:
 print(f"Your score is {true_love}, You guys are best together , consider marriage buddies !!")
else:
  print(f"Your score is {true_love} , Not good with each other !!, better if you left each other !! ")