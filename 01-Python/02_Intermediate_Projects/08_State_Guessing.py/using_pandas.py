import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game.")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#turtle for writing
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:
    user_guess = screen.textinput(title = f"{len(guessed_states)}/50 States Correct.", prompt="What's another state's name? (Type exit for quite.)").title()

    if user_guess == "Exit":
        break
    if user_guess in all_states and user_guess not in guessed_states:
        guessed_states.append(user_guess)
        state_data = data[data.state == user_guess]
        writer.goto(state_data.x.item(), state_data.y.item())
        writer.write(state_data.state.item())


unguessed_state = [state for state in all_states if state not in guessed_states]
data = pandas.DataFrame(unguessed_state)
data.to_csv("Unguessed_states.csv")


