question1=input# Simple Agriculture Quiz for Farmers in Kenya

print("Welcome to the Agriculture Quiz!\n")

score = 0

question1 = input("1. Which crop is most commonly affected by Fall Armyworm in Kenya? (A) Maize (B) Beans (C) Coffee (D) Rice: ").strip().upper()
if question1 == "A":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is A) Maize.")

question2 = input("\n2. What is the best way to improve soil fertility naturally? (A) Adding chemical fertilizers (B) Using biochar and compost (C) Burning crop residues (D) Flooding the field: ").strip().upper()
if question2 == "B":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is B) Using biochar and compost.")

question3 = input("\n3. Which of these pests affects avocado trees? (A) Whiteflies (B) Fall Armyworm (C) Thrips (D) Locusts: ").strip().upper()
if question3 == "C":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is C) Thrips.")

question4 = input("\n4. Which storage method helps prevent post-harvest losses in maize? (A) Using hermetic bags (B) Storing in plastic bags (C) Leaving maize in the field (D) Mixing grains with sand: ").strip().upper()
if question4 == "A":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is A) Using hermetic bags.")

question5 = input("\n5. Which farming practice helps conserve water in dry areas? (A) Irrigation (B) Zai pits (C) Flooding the farm (D) Using pesticides: ").strip().upper()
if question5 == "B":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is B) Zai pits.")

print("\n Quiz Over!")
print(f"Your final score: {score}/5")

play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
if play_again == "yes":
    print("\nRestart the program to play again! ")
else:
    print("Asante kwa kucheza! Happy farming!")
