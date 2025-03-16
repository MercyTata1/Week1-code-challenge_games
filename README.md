Let’s break down the code step by step so you understand how it works. 🚜😊
________________________________________
1️⃣ Introduction & Displaying a Welcome Message
print("🌾 Welcome to the Agriculture Quiz! 🌱\n")
📌 This prints a welcome message on the screen.
📌 \n is used to add a blank line for better readability.
________________________________________
2️⃣ Initializing the Score
score = 0
📌 The score variable stores the user's points.
📌 We start at 0 and increase it whenever the user gets a correct answer.
________________________________________
3️⃣ Asking the First Question
question1 = input("1. Which crop is most commonly affected by Fall Armyworm in Kenya? (A) Maize (B) Beans (C) Coffee (D) Rice: ").strip().upper()
📌 input() asks the user to enter an answer.
📌 .strip() removes extra spaces from the input.
📌 .upper() converts the answer to uppercase, so both a and A will work.
________________________________________
4️⃣ Checking the Answer
if question1 == "A":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! The correct answer is A) Maize.")
📌 if checks if the user entered "A".
📌 If correct, it adds 1 to score using score += 1.
📌 If wrong, it displays the correct answer.
________________________________________
5️⃣ Repeating the Same Steps for Other Questions
Each question follows the same structure:
1.	Ask the user for an answer (input())
2.	Convert the answer to uppercase (.strip().upper())
3.	Check if it’s correct (if-else)
4.	Update the score if correct (score += 1)
Example:
question2 = input("\n2. What is the best way to improve soil fertility naturally? (A) Adding chemical fertilizers (B) Using biochar and compost (C) Burning crop residues (D) Flooding the field: ").strip().upper()
if question2 == "B":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! The correct answer is B) Using biochar and compost.")
📌 Same process as the first question! ✅
________________________________________
6️⃣ Displaying the Final Score
print("\n🏆 Quiz Over! 🏆")
print(f"Your final score: {score}/5")
📌 \n adds a blank line for better formatting.
📌 f"Your final score: {score}/5" uses f-strings to insert the score dynamically.
________________________________________
7️⃣ Asking If the User Wants to Play Again
play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
if play_again == "yes":
    print("\nRestart the program to play again! 🚜")
else:
    print("Asante kwa kucheza! Happy farming! 🌾")
📌 .strip().lower() makes sure that inputs like "YES" or " yes " are treated as "yes".
📌 If they say "yes", they are asked to restart the program.
📌 If they say "no", the game ends with a thank-you message.
________________________________________
🔹 Full Summary
1.	The quiz starts with a welcome message.
2.	The user answers five multiple-choice questions.
3.	Their score is updated for correct answers.
4.	At the end, their total score is displayed.
5.	The user can choose to play again or exit.
________________________________________
🔹 Why is this Beginner-Friendly?
✅ Uses simple if-else statements
✅ Uses basic input & print functions
✅ No complex loops or functions
✅ Very easy to modify or expand
