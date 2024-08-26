from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizlett")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 18, "italic"))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.ques_text = self.canvas.create_text(
            150, 125,
            text="Quiz Question",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR,
            width=280
        )
        self.ans_text = self.canvas.create_text(
            150, 200,
            text="",
            font=("Arial", 15, "italic"),
            fill=THEME_COLOR,
            width=280
        )

        self.tick_img = PhotoImage(file="images/true.png")
        self.know_butt = Button(image=self.tick_img, highlightthickness=0, command=self.true_pressed)
        self.know_butt.grid(row=2, column=0)

        self.cross_img = PhotoImage(file="images/false.png")
        self.false_butt = Button(image=self.cross_img, highlightthickness=0, command=self.false_pressed)
        self.false_butt.grid(row=2, column=1)

        self.get_next_ques()

        self.window.mainloop()

    def get_next_ques(self):
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.ans_text, text="")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.ques_text, text=q_text)
            self.know_butt.config(state="normal")
            self.false_butt.config(state="normal")
        else:
            self.canvas.itemconfig(self.ques_text, text="You've reached the end of the quiz.")
            self.canvas.itemconfig(self.ans_text,
                                   text=f"Your final score: {self.quiz.score}/{self.quiz.question_number}")
            self.know_butt.config(state="disabled")
            self.false_butt.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
            correct_answer = self.quiz.current_question.answer
            self.canvas.itemconfig(self.ans_text, text=f"Correct answer: {correct_answer}")

        self.know_butt.config(state="disabled")
        self.false_butt.config(state="disabled")
        self.window.after(2000, self.get_next_ques)