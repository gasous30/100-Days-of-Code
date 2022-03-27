import turtle
import pandas as pd

data = pd.read_csv('50_states.csv')
guessed_states = []

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

while len(guessed_states) <=50:
    answer_input = screen.textinput(title=f'{len(guessed_states)}/50 correct states', prompt="What's another states name?")
    if answer_input == None:
        break
    answer = data[data['state'] == answer_input.title()]
    if answer_input.title() == 'Exit':
        break
    if not answer.empty:
        st = turtle.Turtle()
        st.ht()
        st.penup()
        st.goto(int(answer['x']),int(answer['y']))
        st.write(answer['state'].item())
        guessed_states.append(answer_input.title())

unguessed_state = data['state'].to_list()

for state in unguessed_state:
    if state in guessed_states:
        unguessed_state.remove(state)

df_unguessed = pd.DataFrame(unguessed_state, columns=['states'])
df_unguessed.to_csv('states_to_learn.csv')