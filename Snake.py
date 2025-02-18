"""
Make Snake with a doubly linked list
Filename: Clemente_project1.py
Author: Matthew Clemente
Date: March 2023
Course: COMP 1353
Assignment: make DoublyLinkedSnake class in Python
Collaborators: None
Internet Source: None
"""

# import dudraw and doublylinkedlist
from DoublyLinkedList import DoublyLinkedList
import dudraw
from dudraw import Color
from random import randint

# make snake class
class Snake(DoublyLinkedList):

    def __init__(self):
        """
        purpose: create instance variables
        arguments: none
        output: none
        """
        DoublyLinkedList.__init__(self)
        self.color=Color(0,255,0)
        self.xpos=10
        self.ypos=10
        self.xvel=1
        self.yvel=0

    def move(self):
        """
        purpose: move snake
        arguments: none
        output: none
        """
        if dudraw.has_next_key_typed():
            key=dudraw.next_key_typed()
            # update acceleration based on which key has been typed
            if key=="w":
                if self.yvel!=-1:
                    self.yvel=1
                    self.xvel=0
            if key=="a":
                if self.xvel!=1:
                    self.yvel=0
                    self.xvel=-1
            if key=="s":
                if self.yvel!=1:
                    self.yvel=-1
                    self.xvel=0
            if key=="d":
                if self.xvel!=-1:
                    self.yvel=0
                    self.xvel=1
        # update position with velocity
        self.ypos+=self.yvel
        self.xpos+=self.xvel

        # make a new segment and remove the last one so the snake moves
        self.add_first([self.xpos,self.ypos])
        self.remove_last()
        

    
    def draw(self):
        """
        purpose: draw snake
        arguments: none
        output: none
        """
        dudraw.set_pen_color(self.color)
        dudraw.filled_square(self.header.next.value[0],self.header.next.value[1],.5)
        dudraw.set_pen_color(Color(0,0,0))
        dudraw.filled_square(self.trailer.prev.value[0],self.trailer.prev.value[1],.5)


    def crash(self):
        """
        purpose:check if snake has crashed
        arguments: none
        output: True or False
        """
        # check if snake has hit a wall
        if self.header.next.value[0]>=20:
            return True
        if self.header.next.value[1]>=20:
            return True
        if self.header.next.value[0]<=0:
            return True
        if self.header.next.value[1]<=0:
            return True
        if snake.get_size()<4:
            return False
        # check if snake has hit itself
        temp1=self.header.next
        temp2=self.header.next.next
        while temp2.next is not None:
            if temp2.value==temp1.value:
                return True
            temp2=temp2.next
        return False


class Food:

    def __init__(self):
        """
        purpose: create instance variables
        arguments: none
        output: none
        """
        self.x=randint(1,19)
        self.y=randint(1,19)
        self.color=Color(255,255,0)

    def crash(self):
        """
        purpose: check if the snake has eaten food
        arguments: none
        output: True or False
        """
        if [self.x,self.y]==snake.header.next.value:
            self.add_food()
            snake.add_last([snake.trailer.prev.value[0],snake.trailer.prev.value[1]])
            return True
        else:
            return False
        
    def add_food(self):
        """
        purpose: create a food item
        arguments: none
        output: none
        """
        dudraw.set_pen_color(snake.color)
        dudraw.filled_circle(self.x,self.y,.4)
        self.x=randint(1,19)
        self.y=randint(1,19)
        

    def draw(self):
        """
        purpose: draw a food item
        arguments: none
        output: none
        """
        dudraw.set_pen_color(self.color)
        dudraw.filled_circle(self.x,self.y,.4)

# main code block

# set up dudraw (canvas size, x and y scale, color canvas)
background_color=dudraw.BLACK
dudraw.set_x_scale(0,20)
dudraw.set_y_scale(0,20)
dudraw.clear(background_color)

# make snake class object
snake=Snake()

# add starting segments for the snake to start out with
snake.add_last([10,10])
snake.add_last([9,10])

# create an object in the food class
food=Food()

# set snake_is_dead variable
snake_is_dead=False

# starter code
limit = 20 #number of frames to allow to pass before snake moves
timer = 0  #a timer to keep track of number of frames that passed

# animation loop
while not snake_is_dead:
    timer += 1
    if timer == limit:
        # while timer counts down, call all of the animation methods for snake and food classes
        snake.move()
        snake.draw()
        food.draw()
        food.crash()
        # end loop if snake crashes
        if snake.crash():
            snake_is_dead=True
        timer = 0
    dudraw.show(10)

# sequence for if the snake dies that displays "CRASH" on the screen
dudraw.set_pen_color(dudraw.RED)
dudraw.set_font_size(50)
dudraw.text(10,10,"CRASH")
dudraw.show(float("inf"))






