from Tkinter import *
import time

#This is a program that replicates Langtons Ant using TKinter
class LangtonsAnt:

    def __init__(self, n, scale):
        self.master = Tk()
        self.ant_array = [[0 for x in range(n)] for x in range(n)] #Creates array representation of board NxN
        self.n = n
        self.scale = scale
        self.antX = int(n/2)
        self.antY = self.antX
        self.ant_array[self.antY][self.antX] = 1
        self.ant_direction = 0 #0-N, 1-E, 2-S, 3-W
        self.should_stop = False

        self.zero_colr = '#95EEE6'
        self.out_colr = '#C1FEC0'
        self.one_colr = '#8947BE'
 
        self.my_canvas = Canvas(self.master, width=n*scale, height=n*scale)
        self.my_canvas.pack()
        self.draw_initial()
        self.draw()
        self.master.mainloop()


    def draw_initial(self):
        for y, column in enumerate(self.ant_array):
            for x, cell in enumerate(column):
                self.my_canvas.create_rectangle(x*self.scale, y*self.scale, (x+1)*self.scale, (y+1)*self.scale, fill=self.zero_colr, outline=self.out_colr)
        self.my_canvas.update()


    #This doesn't use recursion as reaches max depth.
    def draw(self):
        while not self.should_stop: #Escape, although it is redundant
            if (self.antX >= self.n or self.antX < 0 or self.antY >= self.n or self.antY < 0) : #out of bounds
                self.should_stop = True #Redundant, need to fix
                return
            colour = self.zero_colr    #White
            if self.ant_array[self.antY][self.antX] == 1: #Black
                colour = self.one_colr
            self.my_canvas.create_rectangle(self.antX*self.scale, self.antY*self.scale, (self.antX+1)*self.scale, (self.antY+1)*self.scale, fill=colour, outline=self.out_colr)
            self.my_canvas.update()
            self.master.after(0, self.move_ant()) #Change this value to add a delay, However its already slow enough
        

    #onWhite: turn right, swap colour, move forward
    #onBlack: turn left, swap colour, move forward
    def move_ant(self):    
        if self.ant_array[self.antY][self.antX] == 0: #if white
            self.ant_direction = (self.ant_direction+1) % 4 #turn right
        else:
            self.ant_direction = (self.ant_direction-1) % 4 #turn left
        self.ant_array[self.antY][self.antX] = 1 - self.ant_array[self.antY][self.antX] #swap colour
        if self.ant_direction == 0: #North
            self.antX = self.antX+1
        elif self.ant_direction == 1: #East
            self.antY = self.antY+1
        elif self.ant_direction == 2: #South
            self.antX = self.antX-1
        elif self.ant_direction == 3: #West
            self.antY = self.antY-1
            
        




#Main

LangtonsAnt(150, 4)

