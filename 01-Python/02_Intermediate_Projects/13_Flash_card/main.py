from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_word = {}
words_dict = {}

# ---------------------------- CREATE DICT USING PANDAS CSV ------------------------------- #
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_file_data = pandas.read_csv("data/hindi_words.csv")
    words_dict = original_file_data.to_dict(orient="records")
else:
    words_dict = data.to_dict(orient="records")


# ---------------------------- ACTIVATE BUTTON ------------------------------- #
def next_card():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(words_dict)
    canvas.itemconfig(card_title, text="Hindi", fill=BACKGROUND_COLOR)
    canvas.itemconfig(card_word, text= current_word["Hindi"], fill=BACKGROUND_COLOR)
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)


# ---------------------------- FLIP CARD FUNC------------------------------- #
def flip_card():
    canvas.itemconfig(card_background, image=card_back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_word["English"], fill="white")


# ---------------------------- USER KNOW CARD FUNC------------------------------- #
# whichever word user know will remove from words_dict and word_dict left with only unknown words
def user_known():
    words_dict.remove(current_word)
    data = pandas.DataFrame(words_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)

card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image)

card_title = canvas.create_text(400, 130, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)


# WRONG BUTTON
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

# RIGHT BUTTON
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=user_known)
right_button.grid(column=1, row=1)

next_card()


window.mainloop()