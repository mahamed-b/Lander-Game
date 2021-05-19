import turtle
import math
import random
class Lander(turtle.Turtle):
    '''
    Purpose: The ship(or lander)
    Instance variables: self.vx: x velocity; self.vy: y velocity; self.x_pos: x position;
    self.y_pos: y position; self.fuel_remaining: the amount of fuel remaining; self.left: sets ship left by 90 degrees;
    self.penup: takes the pen up; self.setpos: sets the position of the ship;
    self.speed: speeds up the process
    Methods: move: moves the ship; thrust: when you press the up botton it thrusts you foward;
    left_1: turns the ship 10 degrees left; right_1: turns the ship 10 degrees right
    '''
    def __init__(self,x_pos, y_pos, x_vel, y_vel):
        turtle.Turtle.__init__(self)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.vx = x_vel
        self.vy = y_vel
        self.fuel_remaining = 50
        self.left(90)
        self.color('white')
        self.penup()
        self.setpos(x_pos, y_pos)
        self.speed(0)
    def move(self):
        new_x_pos = self.xcor()+self.vx
        new_y_vel = self.vy - 0.0486
        new_y_pos = self.ycor() + new_y_vel
        self.setpos(new_x_pos, new_y_pos)
    def thrust(self):
        print('Up button pressed')
        if self.fuel_remaining > 0:
            angle = math.radians(self.heading())
            self.vx = math.cos(angle) + self.vx
            self.vy = math.sin(angle) + self.vy
            self.fuel_remaining-=1
            print("The number of fuel remaining is: ", self.fuel_remaining)
        else:
            print("Out of fuel")
    def left_1(self):
        print('Left button pressed')
        if self.fuel_remaining > 0:
            self.left(10)
            self.fuel_remaining-=1
            print("The number of fuel remaining is: ", self.fuel_remaining)
        else:
            print("Out of fuel")
    def right_1(self):
        print('Right button pressed')
        if self.fuel_remaining > 0:
            self.right(10)
            self.fuel_remaining-=1
            print("The number of fuel remaining is: ", self.fuel_remaining)
        else:
            print("Out of fuel")

class Game:
    '''
    Purpose: Plays the game
    Instance variables: self.player: lets the player maniuplate the lander object(ship);
    self.meteor: spawns the meteors
    Methods: gameloop: calls the game every 30 seconds; add_rock: adds meteors to the game from the top of the screen;
    collosion: checks if the ship collides with a meteor;
    '''
    def __init__(self):
        turtle.bgcolor('black')
        turtle.setworldcoordinates(0, 0, 1000, 1000)
        turtle.delay(0)
        self.player = Lander(random.uniform(100,900),random.uniform(500,900),random.uniform(-2,2),random.uniform(-2,0))
        self.meteor = []
        self.player.turtlesize(1.75)
        self.gameloop()
        turtle.onkeypress(self.player.thrust, 'Up')
        turtle.onkeypress(self.player.left_1, 'Left')
        turtle.onkeypress(self.player.right_1, 'Right')
        turtle.listen()
        turtle.mainloop()
    def add_rock(self):
        f = random.randint(1,20)
        if f < 2:
            self.meteor.append(Meteors(random.uniform(100,900),1000,random.uniform(-5,5),-10))
    def collosion(self):
        for rock in self.meteor:
            x_distance = (abs(rock.xcor() - self.player.xcor()))
            y_distance = (abs(rock.ycor() - self.player.ycor()))
            if (x_distance <= 10) and (y_distance <= 10):
                print("You Crashed!")
                return True
        return False
    def gameloop(self):
        game = True
        if (self.collosion() == True):
            return
        if self.player.ycor() < 10:
            if (self.player.vx > 3) or (self.player.vy > 3):
                print('You crashed!')
                game = False
        if game == True:
            self.add_rock()
            self.player.move()
            for rock in self.meteor:
                rock.move_1()
            turtle.Screen().ontimer(self.gameloop, 30)

class Meteors(turtle.Turtle):
    '''
    Purpose: To make Meteors
    Instance variables: self.vx = x velocity; self.vy = y velocity; self.xpos: x position;
    self.ypos: y postion self.penup: takes the pen up; self.setpos: sets the position of the ship;
    self.speed: speeds up the process; self.shapesize: sets the meteor width and length to 1;
    Methods: move_1: moves the meteors
    '''
    def __init__(self, xpos, ypos, xvel, yvel):
        turtle.Turtle.__init__(self)
        self.xpos = xpos
        self.ypos = ypos
        self.vx = xvel
        self.vy = yvel
        self.shape('circle')
        self.color('red')
        self.penup()
        self.shapesize(stretch_wid = 1, stretch_len = 1)
        self.setpos(xpos, ypos)
        self.speed(0)
    def move_1(self):
        new_x_pos = self.xcor()+self.vx
        new_y_vel = self.vy - 0.0486
        new_y_pos = self.ycor() + new_y_vel
        self.setpos(new_x_pos, new_y_pos)

Game()
