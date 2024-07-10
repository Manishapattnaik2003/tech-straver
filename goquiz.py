import tkinter as tk
from tkinter import messagebox

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.current_question_index = 0
        self.score = 0

    def get_current_question(self):
        if self.current_question_index < len(self.questions):
            return self.questions[self.current_question_index]['question']
        else:
            return None

    def check_answer(self, answer):
        correct_answer = self.questions[self.current_question_index]['answer']
        if answer.lower() == correct_answer.lower():
            self.score += 1
        self.current_question_index += 1

    def is_quiz_over(self):
        return self.current_question_index >= len(self.questions)

class QuizApp:
    def __init__(self, root, quiz):
        self.quiz = quiz
        self.root = root
        self.root.title("Interactive Quiz")
        
        self.question_label = tk.Label(root, text="", wraplength=300, font=("Arial", 14))
        self.question_label.pack(pady=20)
        
        self.answer_var = tk.StringVar()
        self.answer_entry = tk.Entry(root, textvariable=self.answer_var, font=("Arial", 14))
        self.answer_entry.pack(pady=10)
        
        self.submit_button = tk.Button(root, text="Submit", command=self.submit_answer, font=("Arial", 14))
        self.submit_button.pack(pady=10)
        
        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=20)
        
        self.next_button = tk.Button(root, text="Next Question", command=self.next_question, font=("Arial", 14))
        self.next_button.pack(pady=10)
        self.next_button.config(state=tk.DISABLED)
        
        self.display_question()

    def display_question(self):
        question = self.quiz.get_current_question()
        if question:
            self.question_label.config(text=question)
            self.answer_var.set("")
            self.result_label.config(text="")
        else:
            self.question_label.config(text="Quiz over!")
            self.result_label.config(text=f"Your score: {self.quiz.score}/{len(self.quiz.questions)}")
            self.answer_entry.config(state=tk.DISABLED)
            self.submit_button.config(state=tk.DISABLED)
            self.next_button.config(state=tk.DISABLED)

    def submit_answer(self):
        answer = self.answer_var.get()
        self.quiz.check_answer(answer)
        if self.quiz.is_quiz_over():
            self.display_question()
        else:
            self.result_label.config(text=f"Correct answer: {self.quiz.questions[self.quiz.current_question_index - 1]['answer']}")
            self.submit_button.config(state=tk.DISABLED)
            self.next_button.config(state=tk.NORMAL)

    def next_question(self):
        self.display_question()
        self.submit_button.config(state=tk.NORMAL)
        self.next_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    questions = [
        {'question': 'What is the capital of France?', 'answer': 'Paris'},
        {'question': 'What is 2 + 2?', 'answer': '4'},
        {'question': 'Who wrote "To Kill a Mockingbird"?', 'answer': 'Harper Lee'},
        {'question': 'What is the largest planet in our solar system?', 'answer': 'Jupiter'},
        {'question': 'What year did the Titanic sink?', 'answer': '1912'},
    ]
    
    root = tk.Tk()
    quiz = Quiz(questions)
    app = QuizApp(root, quiz)
    root.mainloop()
