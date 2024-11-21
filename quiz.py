import mysql.connector


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yuvraj@123",
    database="quiz_game"
)

cursor = conn.cursor()

add_question_choice = input("Do you want to add a new question before starting the game? (yes/no): ").lower()

if add_question_choice == "yes":
    ques_n0 = int(input("How many question u want to insert : "))
    for i in range(ques_n0):
        print("\n--- Add a New Question ---")
        question = input("Enter the question: ")
        option_a = input("Enter option A: ")
        option_b = input("Enter option B: ")
        option_c = input("Enter option C: ")
        option_d = input("Enter option D: ")
        correct_answer = input("Enter the correct answer (A, B, C, or D): ").lower()

        query = """
        INSERT INTO quiz_questions (question, option_a, option_b, option_c, option_d, correct_answer)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
    cursor.execute(query,(question, option_a, option_b, option_c, option_d, correct_answer))
    conn.commit()
    print("\nNew question added successfully!")

cursor.execute("SELECT * FROM quiz_questions")
questions = cursor.fetchall()

player_name = input("\nEnter your name: ")
# quiz strt
score = 0


for q in questions:
    print(f"\n{q[1]}")  # Question
    print(f"a) {q[2]}")
    print(f"b) {q[3]}")
    print(f"c) {q[4]}")
    print(f"d) {q[5]}")

    answer = input("\nYour answer (a, b, c, d): ").lower()

    if answer == q[6].lower():
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer was {q[6]}.")

print(f"\nGame Over! {player_name} final score is {score}/{len(questions)}")

query = "INSERT INTO quiz_scores (player_name, score) VALUES (%s, %s)"
cursor.execute(query, (player_name, score))
conn.commit()

# Retrieve the top scorer
cursor.execute("""
    SELECT player_name, score 
    FROM quiz_scores 
    ORDER BY score DESC 
    LIMIT 5
""")
leaderboard = cursor.fetchall()

print("\nTop 5 Leaderboard:")
for rank, (name, score) in enumerate(leaderboard, start=1):
    print(f"{rank}. {name} - {score}")





conn.close()
