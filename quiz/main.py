from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question['question']
    question_answer = question['correct_answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

oQuiz = (QuizBrain(question_bank))

while oQuiz.still_has_questions():
    oQuiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {oQuiz.score}/{oQuiz.question_number}")

