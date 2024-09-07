from turtle import *


#we want to build house

#step 1: Draw a square

begin_fill()
width(8)
color("brown")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#End of square

#Drawing a door



forward(67)

left(90)

color("yellow")      #we gave color to our door
begin_fill()
forward(100)

right(90)

forward(67)

right(90)
forward(100)
end_fill()         #now we are doing roof 
penup()

goto(200, 200)

pendown()

color("red")
begin_fill()

left(230)

forward(130)

right(280)

forward(130)
end_fill()              #here we fill roof

penup()
color("black")
goto(180, 180)

pendown()
begin_fill()
left(320)

forward(50)

right(270)        #first window

forward(50)

left(90)

forward(50)

right(270)

forward(50)
end_fill()
penup()

goto(20, 180)

pendown()


right(90)        #second window
begin_fill()
forward(50)

left(270)

forward(50)

right(90)

forward(50)

left(270)

forward(50)
end_fill()
exitonclick()               #finish      
