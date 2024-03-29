from tkinter import *

import csv
from datetime import datetime
current_date_and_time = datetime.now()
import math

wall_studs = 0
tb_plates = 0
baseboards = 0
wall = 0
window = 0
door = 0
nails_needed = 0
door_frame = 0
# num_rooms = 0


def floor_plan(rooms):
    num_rooms = rooms + 1
    
    return num_rooms

def framing_wood(length, height, ):
    stud_length = height - 3
    wall_studs = length / 16 + 2
    tb_plates = length * 2
    baseboards = length
    nails_needed = wall_studs * 4
    # door_frame = 


def room_scope(walls, windows, doors):
     wall = walls
     window = windows
     door = doors

# def room_electric():

# def room_drywall():
     
# def room_paint():
     
# def room_plumbing():
     
# def room_hvac():
     


# def Tk(className):
#     className: str = "STFUB"

# root = Tk()
# root.geometry('300x300')
# l = Label(root, text='Start To Finish UR Basement', background="blue")



# l.pack()

# root.mainloop()
def main():
    rooms = int(input("How many total rooms will you be finishing?"))
    
    total_rooms = floor_plan(rooms)


    print(f"this is the total number of rooms: {total_rooms}")





if __name__ == "__main__":
    main()