import turtle
import pandas

screen = turtle.Screen()
screen.title(f"US States game ")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

adat = pandas.read_csv("50_states.csv")
osszes = adat.state.to_list()
lehetseges = adat["state"]
megfejtések = []
missed = []

while len(megfejtések) < 50:
    valasz = screen.textinput("Válaszolj a kérdésre:", f"Adj meg egy államot!{len(megfejtések)}/50").title()
    if valasz not in megfejtések:
      for i in lehetseges:
         if i == valasz:
            koord = adat[adat.state == i]
            kiir = turtle.Turtle()
            kiir.penup()
            kiir.hideturtle()
            kiir.goto(int(koord.x), int(koord.y))
            kiir.write(valasz, move=False, align="left", font=("Arial", 8, "normal"))
            megfejtések.append(i)
    if valasz == "Exit":
        missed = [i for i in osszes if i not in megfejtések]

        data = pandas.DataFrame(missed)
        data.to_csv("missed.csv")

        break


