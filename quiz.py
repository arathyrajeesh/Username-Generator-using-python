quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Rome", "D. Berlin"],
        "answer": "A"
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["A. Python", "B. JavaScript", "C. C++", "D. Java"],
        "answer": "B"
    },
    {
        "question": "2 + 2 * 2 = ?",
        "options": ["A. 6", "B. 8", "C. 4", "D. 2"],
        "answer": "A"
    },
]
def quizApp():
    score = 0
    print("Welcome to the Quiz Application!\n")    
    for i in range(len(quiz_questions)):
        q = quiz_questions[i]
        print(f"Q{i+1}.{q['question']}")
        for option in q['options']:
            print(option)
        user_ans = input("Your answer (A/B/C/D): ").upper()
        if user_ans == q["answer"]:
            print("Correct! Well Done*")
            score += 1
        else:
            print(f"Wrong answer! Correct answer is {q['answer']}")
            print(f"Incorrect answer deducts -1 point")
            score -= 1    
            print(f"Your final score: {score} out of {len(quiz_questions)}")
    if score == len(quiz_questions):
        print("Congradulations!!!You have passed.")
quizApp()