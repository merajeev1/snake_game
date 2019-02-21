import turtle #python graphics library
import time # to delay the snake, because its too fast to see
import random #to generate random numbers

delay = 0.1

#Score
score = 0
file=open("high_score.txt","r")
high_score = int(file.read())
file.close()



#set up the screen
wn = turtle.Screen()
wn.title("Snake game by Rajeev")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0) #Turns off the screen updates

wn.register_shape("apple.gif")
wn.register_shape("head.gif")


# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape('head.gif')
head.color("black")
head.penup()  # its 'pen up' so it doesn't draw anything
head.goto(0,0)
head.direction = 'stop' #by default we set the head direction to up


#Snake food
#the food will remain still
food = turtle.Turtle()
food.speed(0)
food.shape("apple.gif")
food.color("red")
food.penup()  # its 'pen up' so it doesn't draw anything
food.goto(0,100)

segments=[]

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,200)
pen.write("Score: 0 Hight Score: {} ".format(high_score),align="center", font=("Courier", 24, "normal"))

# Functions
def go_up():
	if head.direction != "down": # can't go in reverse direction
		head.direction = "up"
def go_down():
	if head.direction != "up":
		head.direction = "down"

def go_left():
	if head.direction != "right":
		head.direction = "left"

def go_right():
	if head.direction != "left":
		head.direction = "right"
	
def move():
	if head.direction == "up": 
		y=head.ycor()
		head.sety(y+20)
		
	if head.direction == "down": 
		y=head.ycor()
		head.sety(y-20)
		
	if head.direction == "left": 
		x=head.xcor()
		head.setx(x-20)
	
	if head.direction == "right": 
		x=head.xcor()
		head.setx(x+20)

# Keyboard bindings
wn.listen() #window is listening to clicks now
wn.onkeypress(go_up,"w") #go_up function is called, when w is pressed, its forever
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")


# Main game loop
while True:
	wn.update()
	
	#check for a collison with the border
	if head.xcor() > 290 or head.xcor()< -290 or head.ycor()>290 or head.ycor()<-290:
		time.sleep(1)
		head.goto(0,0)
		head.direction = "stop"
		
		#hide the segments
		for segment in segments:
			segment.goto(1000,1000) #because couldn't find a way to delete turtles

			
		#clear the segments list
		segments.clear()
		
		#Reset the score
		score=0
		
		pen.clear()
		pen.write("Score: {} High Score: {}".format(score,high_score),align="center",font=("Courier", 24, "normal"))
		
		#Reset the delay
		delay = 0.1
		
	#check for a collison with the food
	if head.distance(food)<20:
		#move the food to a random spot
		x=random.randint(-290,290) #because the screen is 600*600, 0 t0 300 each side
		y=random.randint(-290,290) #we have used 290 so that it doesn't get to the bourndry
		food.goto(x,y)
		#Adding a segment
		new_segment = turtle.Turtle()
		new_segment.speed(0)
		new_segment.shape("circle")
		new_segment.color("red")
		new_segment.penup()
		segments.append(new_segment)
		
		#Increase the score
		score +=10
		
		if score > high_score:
			high_score=score
			file = open("high_score.txt","w")
			file.write(str(high_score))
			file.close()
			
		pen.clear()
		pen.write("Score: {} High Score: {}".format(score,high_score),align="center",font=("Courier", 24, "normal"))
		
		#shorten the delay
		delay -= 0.001
		
	
	#Move the end segments first in reverse order
	for index in range(len(segments)-1, 0 , -1): #it will move from 9 to 1, if length is 10
		x=segments[index-1].xcor() #find the coordinates of the turtle just in front of it
		y=segments[index-1].ycor()
		segments[index].goto(x,y) #move to the place where front turtle was
	
	if len(segments)>0:
		x=head.xcor()
		y=head.ycor()
		segments[0].goto(x,y)
		
	move()
	
	#check for head collision with the body segments
	
	for segment in segments:
		if segment.distance(head) < 20:
			time.sleep(1)
			head.goto(0,0)
			head.direction = "stop"
			
			#hide the segments
			for segment in segments:
				segment.goto(1000,1000) #because couldn't find a way to delete turtles

			
			#clear the segments list
			segments.clear()
			
			score=0
		
			pen.clear()
			pen.write("Score: {} High Score: {}".format(score,high_score),align="center",font=("Courier", 24, "normal"))
			
			#Reset the delay
			delay = 0.1
			
	
	time.sleep(delay)
	
	
#To keep the main window running
wn.mainloop()
