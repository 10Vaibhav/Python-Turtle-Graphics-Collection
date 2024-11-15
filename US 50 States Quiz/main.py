import turtle
import pandas
from writer import Writer

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
write = Writer()
data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()

guess_list = []
step = 0
while len(guess_list) < 50:
    user = screen.textinput(title=f"{len(guess_list)}/50 States Correct", prompt="What's another state?")
    answer = user.title()

    if answer == "Exit":
        missing_states = [state for state in all_states if state not in guess_list]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer in all_states:
        axis_x = int(data[data["state"] == answer].x.iloc[0])
        axis_y = int(data[data["state"] == answer].y.iloc[0])
        write.update(answer, axis_x, axis_y)
        guess_list.append(answer)
        step += 1


