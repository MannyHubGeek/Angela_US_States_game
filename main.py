import turtle
import pandas
import csv


screen = turtle.Screen()
screen.title("U.S. states Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.screensize(800, 600)

turtle.shape(image)

# The function below helps to get the coordinates of a mouse click on the screen
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()


data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()

guessed_states = []
while len(guessed_states) < 50:
    answer_state = (screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name")).title()

    if answer_state == "Exit":
        to_learn = []
        for state in states_list:
            if state not in guessed_states:
                to_learn.append(state)
        new_df = pandas.DataFrame(to_learn)
        new_df.to_csv("states_to_learn.csv")
        break
    if answer_state in states_list:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)







#screen.exitonclick()
