#This is my health evaluation application


# 1. Hello name function

def hello(name):
  print("Hello", name)

# 1 step - Greet a user
print("Dear user")
print("This is a heath evaluator app")
print("According to your health parameters I will give your a overview and some recomendations to be sure you are on the right way to the healthy life style")

your_name = input("Put your name, please: ")
hello(your_name)

# 2. Adult or not function
#Second function asks an age of a user to be sure we are checking an adult, if the age is less than 20, the execution of the code start again

def adult_or_not(age):
    if age >= 20:
      print("Your age is: ", age)
    else:
      print("Sorry", your_name, "but I can't make evaluations for kids, please ask your doctor")
      user_age = int(input("Enter your age, please: "))

user_age = int(input("Enter your age, please: "))
adult_or_not(user_age)


# 3 step - Asking a permission to use the data.

# print("Let's check your health parameter?")
# check = input ("Put yes to proceed: ")
# if check == "yes":
#   print("Great, let's move on")
# elif check == "no":
#   print("I see you need more time, let's try later")
#   exit ()
# else:
#   print("Yes or No required")

'''
At this point is our user ready for check up the health rate, so lets move on
These parameter we need to ask: gender, weight,height,waist_size, hip_size, activity rate
If we combine the evaluation of BMI, waist-to-hip ratio, age and gender we can make a more comprehensive decision about a person's health.
The BMI can overestimate body fat in athletes and other individuals with a muscular physique.
It can underestimate body fat of older individuals, particularly those who have lost muscle mass.
So we try to exclude athletic persons and older people from bmi calculations
'''

# 3. Gender function
def gender(gen):
  while True:
    gender_input = input(gen)
    if gender_input == "m":
      print("You are male")
      return gender_input
    elif gender_input == "f":
      print("You are female")
      return gender_input
    else:
      print("If you are not related to these both categories I can't make evaluation for you")

print("To make the evaluation of your health paramerters more clear please define your gender")
user_gender_input = input("Please use following letters: m or f - ")
gender (user_gender_input)



# 4. Activity rate function
intensity_levels = {None:1, "moderate":2, "vigorous":3}   

def aktivity_rate(times_per_week, duration, intensity):
    a_rate = times_per_week * duration
    if a_rate <= 1 and intensity == intensity_levels[None] or a_rate  <= 1 and intensity == intensity_levels["moderate"] or a_rate  <= 1 and intensity == intensity_levels["vigorous"]:
        print("You are activ:", a_rate, "houres per week")
        print("Your athletic level leaves much to be desired.", your_name, "what's about any alternative kind of activities: walking, cycling, wheeling, yoga, pilates, zumba?")
    elif a_rate <= 2 and intensity == intensity_levels["moderate"]:
        print("Your calculated activity time:", a_rate, "houres per week")
        print("Looks like you're at the beginning. Don't give up, let it rip!")
        print("Just at least 2.5-3.0 houres of moderate-intensity physical activity throughout the week")
        print("reduce the risk of hypertension, coronary heart disease, diabetes, various types of cancer and depression")
    elif a_rate <= 7 and intensity == intensity_levels["moderate"]:
        print("Your calculated activity time is:", a_rate, "houres per week")
        print("Your activity level is pretty good. Keep going.")
    elif a_rate <= 7 and intensity == intensity_levels["vigorous"] :
        print("Your calculated activity is:", a_rate, "houres per week")
        print("Looks like you make it professionaly. Keep going")
    return a_rate

try:
    times_per_week = int(input("How many times per week are you active or go in for sport?: "))
    duration = float(input("How many houres, on average, is each of your activities?"))
    intensity = float(input("How intense is your activity? Expected answer: 1 for None, 2 for moderate, 3 for vigorous: "))

    user_activity_rate = aktivity_rate(times_per_week, duration, intensity)


except ValueError:
    print("Invalid input. Please enter numeric values for times per week and duration.")


# 5. BMI function
import math

bmi_description = ["are underweight", "in a healthy_range", "are overweight", "have obesity"]

def body_mass_index(weight, height):
    try: 
        height_in_meters = height / 100 # Here we convert height to meters, so the users just have to put it easy in cm
        bmi = round(weight / (height_in_meters ** 2), 2) #here we round the bmi result to two decimal numbers after comma

        if bmi <= 18.5:
          print("Your BMI is:", bmi, "which means you", bmi_description[0])
          print("You can only stay healthy in the long term with the right nutrition and the right amount of exercise.")
    
        elif bmi < 25:
          print("Your BMI is:", bmi, "which means you", bmi_description[1])
          print("Great! Your weight is in a healthy range. With balanced nutrition and regular exercise, your weight will stay constant in the future.")
    
        elif bmi < 30:
          print("Your BMI is:", bmi, "which means you", bmi_description[2])
          print("Your BMI is slightly elevated. Pay attention to your diet and exercise regularly. This will help you minimize the risk of possible comorbidities.")
    
        elif bmi > 30:
          print("Your BMI is:", bmi, "which means you", bmi_description[3])
          print("Your BMI indicates that you are overweight. This carries the risk of diseases such as diabetes. Please apply for a check-up with your doctor.")
        else:
            print("An error is occured. Please ty again")
    
    except ValueError:
        print("An error occurred. Please enter valid numeric values for weight and height.")

    except ZeroDivisionError:
        print("An error occurred. Height cannot be zero.")
    return bmi

# 6. WHR function

def waist_to_hip_ratio(waist, hip): #Example: 68cm/94cm
    whr = waist / hip
    if whr < 0.80 and user_gender_input == "f":
      print("Congratulations,", your_name , "your waist to hip ration is: ", whr, " - this is pear bodyshape, it means the risks for your health are low")
      print("Just continue to pay attention to a healthy nutrition and regular physical activity.")
    elif whr <= 0.85 and user_gender_input == "f":
      print(your_name, " - your waist to hip ration is: ", whr, "You belongs to body shape avocado")
      print("It's time to start with regular sport activity and heath nutrition, else the health risks to diabetes, heart or metabolic disease are goint to grow" )
    elif whr > 0.85 and user_gender_input == "f":
      print("Dear", your_name, " - your waist to hip ration is: ", whr, "You belongs to body shape apple")
      print("Your health risks are high, it's very important to become a consultancy of nutrition spesialist")
      print("Typical for this bodyshape desease are diabetes and blood preasure")
      print("Here are some tips for you:‌ ")
      print("Be more active. Start it easier - 150 minutes of moderate-intensity activity every week")
      print("Change your diet:")
      print("- Eat at least 5 portions of fruits and vegetables every day")
      print("- 6 to 8 glasses of fluids. Less sugary drinks and more water")
      print("- Fewer foods high in fat, salt, and sugar")
    elif whr < 0.95 and user_gender_input == "m":
      print("Congratulations,", your_name , "your waist to hip ration is: ", whr, " this is pear bodyshape, it means the health risks are low")
      print("Just continue to pay attention to a healthy nutrition and regular physical activity to stay fit.")
    elif whr <= 1 and user_gender_input == "m":
      print(your_name, " - your waist to hip ration is: ", whr, "You belongs to body shape avocado")
      print("It's time to start with regular sport activity and heath nutrition, else the health risks to diabetes or  heart disease are goint to grow" )
    elif whr > 1 and user_gender_input == "m":
      print("Dear", your_name, " - your waist to hip ration is: ", whr, "You belongs to body shape apple")
      print("Your health risks are high, it's very important to become a consultancy of nutrition spesialist")
      print("Typical for this bodyshape desease are diabetes and blood preasure")
      print("Just try these tips to lower your weight:‌ ‌")
      print("Be more active. Aim for a total of 150 minutes of moderate-intensity activity every week")
      print("Change your diet:")
      print("- At least 5 portions of fruits and vegetables every day")
      print("- 6 to 8 glasses of fluids. Less sugary drinks and more water")
      print("- Fewer foods high in fat, salt, and sugar")
    return whr


# 6 step - Activity rate evaluation for further calculations

if user_activity_rate >= 3 and intensity == intensity_levels["vigorous"] or user_age > 50:
  print("Let's calculate your waise_to_hip_ratio" )
  user_waist = float(input("Enter your waist circumference in cm: "))
  user_hip = float(input("Enter your hip circumference in cm: "))
  waist_to_hip_ratio(user_waist, user_hip)
else:
  print("Let's calculate your body mass index")
  user_weight = float(input("Enter your weight in kg: "))
  user_height = float(input("Enter your height in cm: "))
  body_mass_index(user_weight, user_height)

# 7 Conclution
print("*Please note: All recommendations are based on the fairness and accuracy of provided data.")
print("If your a already feel hampered because of desease, contact your doctor")