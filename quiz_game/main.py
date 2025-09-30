print("Welcome to the quiz!")

playing = input("Do you want to play? (yes/no): ")
if playing.lower() != "yes":
    print("Maybe next time!")
    quit()

print("Great! Let's start the quiz.")
score = 0

answer = input("What is the capital of Sri lanka? ")
if answer.lower() == "sri jayawardenepura kotte":
    print("Correct!")
    score += 1 
else:
    print("Incorrect! The correct answer is Sri Jayawardenepura Kotte.") 

answer = input("What is the longest rever in the world? ")
if answer.lower() == "nile":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is Nile") 


answer = input("What is the highest place in the world? ")
if answer.lower() == "everest":
    print("Correct!")
    score += 1 
else:
    print("Incorrect! The correct answer is Everest.") 


answer = input("Which year begun the world war 2? ")
if answer.lower() == "1939":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 1944") 

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + "%.")