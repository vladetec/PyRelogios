
import turtle
import time

#Window

wn = turtle.Screen()
wn.bgcolor("green")
wn.bgpic('RelogioPalmeiras2.gif')
wn.setup(width=600, height=600)
wn.title("Relogio Analogico Com Python")

wn.tracer(0)

#Pen

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)

def draw_clock(h, m, s, pen):

	#Clock face

	pen.up()
	pen.goto(0, 210)
	pen.setheading(180)
	pen.color("green")
	pen.pendown()
	pen.circle(210)

	#Hour lines

	pen.penup()
	pen.goto(0, 0)
	pen.setheading(90)

	for _ in range(12):
		pen.fd(190)
		pen.pendown()
		pen.fd(20)
		pen.penup()
		pen.goto(0, 0)
		pen.rt(30)

	#Hour Hand

	pen.penup()
	pen.goto(0, 0)
	pen.color("gold")
	pen.setheading(90)
	angle = (h / 12) * 360
	pen.rt(angle)
	pen.pendown()
	pen.fd(60)
	pen.dot(10, "gold")

	#Minute Hand

	pen.penup()
	pen.goto(0, 0)
	pen.color("orange")
	pen.setheading(90)
	angle = (m / 60) * 360
	pen.rt(angle)
	pen.pendown()
	pen.fd(80)
	pen.dot(5, "orange")

	#Second Hand

	pen.penup()
	pen.goto(0, 0)
	pen.color("red")
	pen.setheading(90)
	angle = (s / 60) * 360
	pen.rt(angle)
	pen.pendown()
	pen.fd(100)
	pen.dot(5, "red")

#Update the time

while True:

	h = int(time.strftime("%I"))
	m = int(time.strftime("%M"))
	s = int(time.strftime("%S"))

	draw_clock(h, m, s, pen)
	wn.update()

	time.sleep(1)

	pen.clear()

wn.mainloop()