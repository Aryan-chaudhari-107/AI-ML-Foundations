import turtle
import csv
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)

map_turtle = turtle.Turtle()
map_turtle.shape(image)

#Turtle for writing
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()


### to get x any y of image
# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
#turtle.mainloop() # alternative of screen.exitonclick()


with open("50_states.csv", mode="r") as file:
    data = csv.DictReader(file)
    city_data = list(data)


guessed_score = 0
guessed_state = []

while guessed_score < 50:
    user_guess = screen.textinput(title=f"Guess the State: {guessed_score}/50", prompt="What's another state? (Type exit to quit)").title()

    if user_guess == "Exit":
        break

    if user_guess not in guessed_state:
        for row in city_data:
            if row["state"] == user_guess:
                 guessed_score += 1
                 guessed_state.append(user_guess)
                 x = int(row["x"])
                 y = int(row["y"])
                 writer.goto(x, y)
                 writer.write(row["state"], align="center", font=("Arial", 8, "bold"))
                 print(f"✅ Correct: {row['state']} at ({x}, {y})")


unguessed_states = [row["state"] for row in city_data if row["state"] not in guessed_state]
data = pandas.DataFrame(unguessed_states)
data.to_csv("unguessed_stated.csv")
