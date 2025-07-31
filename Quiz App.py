import tkinter as tk
from tkinter import messagebox
import random

# Simulated AI-generated math question bank
questions = [
    {
        "question": "What is 5 + 3 * 2?",
        "options": ["11", "16", "13", "8"],
        "correct": "11",
        "analysis": "Step-by-step: According to the order of operations (PEMDAS), multiply first: 3 * 2 = 6. Then add: 5 + 6 = 11."
    },
    {
        "question": "Solve for x: 2x + 3 = 11",
        "options": ["4", "5", "3", "6"],
        "correct": "4",
        "analysis": "Step-by-step: Subtract 3 from both sides: 2x = 11 - 3 = 8. Divide by 2: x = 8 / 2 = 4."
    },
    {
        "question": "What is the area of a triangle with base 6 and height 4?",
        "options": ["12", "24", "10", "15"],
        "correct": "12",
        "analysis": "Step-by-step: Area of a triangle = (1/2) * base * height = (1/2) * 6 * 4 = 12."
    },
    {
        "question": "What is 2^3 + 5?",
        "options": ["13", "10", "9", "11"],
        "correct": "13",
        "analysis": "Step-by-step: Calculate the exponent first: 2^3 = 8. Then add: 8 + 5 = 13."
    },
    {
        "question": "If 3x = 15, what is x?",
        "options": ["3", "5", "4", "6"],
        "correct": "5",
        "analysis": "Step-by-step: Divide both sides by 3: x = 15 / 3 = 5."
    }
]


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Math Quiz App")
        self.root.geometry("600x400")

        # Initialize variables
        self.score = 0
        self.current_question = 0
        self.selected_answer = tk.StringVar()
        self.question_bank = random.sample(questions, len(questions))  # Shuffle questions

        # GUI elements
        self.label_question = tk.Label(root, text="", wraplength=500, font=("Arial", 14))
        self.label_question.pack(pady=20)

        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(root, text="", variable=self.selected_answer, value="", font=("Arial", 12))
            rb.pack(anchor="w", padx=20)
            self.radio_buttons.append(rb)

        self.btn_submit = tk.Button(root, text="Submit", command=self.check_answer, font=("Arial", 12))
        self.btn_submit.pack(pady=10)

        self.btn_next = tk.Button(root, text="Next Question", command=self.next_question, font=("Arial", 12))
        self.btn_next.pack(pady=10)
        self.btn_next.config(state="disabled")

        self.label_analysis = tk.Label(root, text="", wraplength=500, font=("Arial", 12), fg="blue")
        self.label_analysis.pack(pady=20)

        self.label_score = tk.Label(root, text=f"Score: {self.score}/{len(questions)}", font=("Arial", 12))
        self.label_score.pack(pady=10)

        # Load first question
        self.load_question()

    def load_question(self):
        if self.current_question < len(self.question_bank):
            q = self.question_bank[self.current_question]
            self.label_question.config(text=q["question"])
            self.selected_answer.set("")  # Reset selection
            for i, option in enumerate(q["options"]):
                self.radio_buttons[i].config(text=option, value=option)
            self.label_analysis.config(text="")
            self.btn_submit.config(state="normal")
            self.btn_next.config(state="disabled")
        else:
            # Quiz finished
            messagebox.showinfo("Quiz Finished", f"Quiz complete! Your final score is {self.score}/{len(questions)}.")
            self.btn_submit.config(state="disabled")
            self.btn_next.config(state="disabled")

    def check_answer(self):
        if not self.selected_answer.get():
            messagebox.showwarning("No Selection", "Please select an answer!")
            return

        q = self.question_bank[self.current_question]
        if self.selected_answer.get() == q["correct"]:
            self.score += 1
            self.label_analysis.config(text=f"Correct! {q['analysis']}", fg="green")
        else:
            self.label_analysis.config(text=f"Incorrect. {q['analysis']}", fg="red")

        self.label_score.config(text=f"Score: {self.score}/{len(questions)}")
        self.btn_submit.config(state="disabled")
        self.btn_next.config(state="normal")

    def next_question(self):
        self.current_question += 1
        self.load_question()


# Create and run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()