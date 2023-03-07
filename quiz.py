print("Welcome to Ana's quiz! ")
answer_user = input("Let's start (Y/N) ")

if answer_user != "Y":
    quit()
score = 0

print("Starting...")
print("Who devolped the Grand Theft Auto (GTA) game? \n (A) Rockstar Games \n (B) Ubisoft \n (C) Activision \n (D) EA \n ")
answer_1 = input("Resposta: ")

if answer_1 == "A":
    print("Correct!")
    score = score + 1

else:
    print("Incorrect!")

print("Who is the best Hornets player? \n (A) LaMelo Ball \n (B) Derrick Rose \n (C) Lonzo Ball \n (D) Jordan Poole \n ")
answer_2 = input("Resposta: ")

if answer_2 == "A":
    print("Correct!")
    score = score + 1

else:
    print("Incorrect!")


print("What is the biggest planet in the solar system? \n (A) Earth \n (B) Jupiter \n (C) Venus \n (D) Wakanda \n ")
answer_3 = input("Resposta: ")

if answer_3 == "B":
    print("Correct!")
    score = score + 1

else:
    print("Incorrect!")

print(f"The quiz is over! thanks for playing <3... Points: {score}/3")