from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    question_text = item["question"]
    question_answer = item["correct_answer"]
    question = Question(question_text, question_answer)
    question_bank.append(question)

# print(question_bank)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was {quiz.current_score}/{quiz.question_number}")