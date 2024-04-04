from tkinter import *

import csv
from datetime import datetime
current_date_and_time = datetime.now()
import math

root = Tk()
root.geometry('600x750')
root.title("Start To Build UR Basement")
root.iconbitmap('/x.png')

# def floor_plan(rooms):
#     num_rooms = rooms + 1
    
#     return num_rooms

# def framing_wood(length, height, ):
#     stud_length = height - 3
#     wall_studs = length / 16 + 2
#     tb_plates = length * 2
#     baseboards = length
#     nails_needed = wall_studs * 4
#     # door_frame = 


# def room_scope(walls, windows, doors):
#      wall = walls
#      window = windows
#      door = doors

# def room_electric():

# def room_drywall():
     
# def room_paint():
     
# def room_plumbing():
     
# def room_hvac():
     


# def Tk(className):
#     className: str = "STFUB"

# def item_cost(cost, quantity):
#     total_cost = cost * quantity

    
#     return total_cost 

product_name = 1
requested_quantity = 1
product_number = 0
product_price = 2

def read_dictionary(filename, key_column_index):
    lowes_dictionary ={}

    with open(filename, mode="rt") as my_lowes:
        l = csv.reader(my_lowes)
        next(l)
        for row_list in l:
            if len(row_list) !=0:
                key = row_list[key_column_index]
                lowes_dictionary[key] = row_list

    return lowes_dictionary

def main():

    try:
        products_dict = read_dictionary("lowes.csv", 0)
        print(f"Lowes Products:")
        print(products_dict)

        print(products_dict['11456'])
        tool = products_dict['11456'][1]
        print(tool)

        list_item = products_dict['11356']
        p2 = products_dict['11456'] 
        p3 = products_dict['D215']
        p4 = products_dict['P019']
        p5 = products_dict['P020']
        p6 = products_dict['P021']
        p7 = products_dict['P025']
        p8 = products_dict['11456']
        carpet_item = products_dict['W231']
        p10 = products_dict['W112']
        p11 = products_dict['C013']
        p12 = products_dict['H001']
        p13 = products_dict['H014']
        p14 = products_dict['H020']
        p15 = products_dict['H021']
        p16 = products_dict['H025']

        # with open("request.csv", mode="rt") as test_file:
        with open("lowes.csv", mode="rt") as test_file:
            my_lowes = csv.reader(test_file)
            next(my_lowes)
            # print()
            # print(f"Fast and Speedy Purchase Receipt:")
            # print()
            for line in my_lowes:
                # quantity = int(line[requested_quantity])
           
                number = line[product_number]

                product_id = line
                # [number]
            
                name = product_id[product_name]
                price = float(product_id[product_price])

                print(f"{name} : {number} @ {price}")
                # total_quantity += quantity
                
                # subtotal += price
    except KeyError as Error:
        print(f"Error: unknown product ID in the lowes.csv file'{Error}")
    except FileNotFoundError as not_found_err:
        print(not_found_err)

    num_rooms = 0
    total_perimiter = 0

    height = Entry(root, width=10, justify='center')
    height.grid( row = 3, column = 3 )
    # field_insert = field.get()

    perimiter = Entry(root, width=10, justify='center')
    perimiter.grid( row = 5, column = 3 )
    # perimiter_insert = perimiter.get()

    doors = Entry(root, width=10, justify='center')
    doors.grid( row = 7, column = 3 )

    windows = Entry(root, width=10, justify='center')
    windows.grid( row = 9, column = 3 )

    walls = Entry(root, width=10, justify='center')
    walls.grid( row = 11, column = 3 )

    # def item_cost(cost, quantity):
#     total_cost = cost * quantity

    def click_clear():
        return
    def myClick():

        # def inventory_cost(item_number,quantity,entry):
    
    

        # p_cost = item_number[2] * quantity
        # print(f"this is p_cost: {p_cost}")
        # return  p_cost
            # print( item_number, quantity, entry)
            # entry.insert(0, quantity * item_number[2] )

        #height of the rooms
        myLabel = height.get()   
        room_height = int(myLabel)

        #length of circumfrence of room
        room_perimiter= perimiter.get()
        room_per = float(room_perimiter)

        #number of doors in room
        room_doors= doors.get()
        num_doors = int(room_doors)

        #number of windows in room
        room_windows= windows.get()
        num_windows = int(room_windows)

        #numbers of walls in room
        room_walls= walls.get()
        num_walls = int(room_walls)




        # Figuring out how many studs are needed
        stud_amount = room_per / 16 + ( 2 * num_walls ) + ( 2 * num_doors) + (3 * num_windows)
        # How long should your studs be
        stud_length = room_height - 3
        # Needing top and bottom plates
        tb_plate = round( room_per / 16) 

      
        Label(root, text='11356').grid(row=17, column = 0)
        Label(root, text=list_item[1]).grid(row=17, column = 1, columnspan=2, sticky=W)
        sa = StringVar()
        sa.set(stud_amount)
        Entry(root, width=5, textvariable=sa, disabledbackground='white', disabledforeground='red', state=DISABLED, justify='center').grid(row=17, column = 3)
        tc = StringVar()
        stud_cost = stud_amount * float(list_item[2])
        tc.set(f'{stud_cost:.2f}')
        Entry(root, width=5, textvariable=tc, disabledbackground='red', disabledforeground='white', state=DISABLED, justify='center').grid(row=17, column = 4)
        


        Label(root, text=(f"Stud Length:{stud_length} foot tall studs")).grid(row=18, column = 1, columnspan=2, sticky=W)

        Label(root, text="P021").grid(row=19, column = 0)
        Label(root, text=p6[1]).grid(row=19, column = 1, columnspan=2, sticky=W)
        tp = StringVar()
        tp.set(tb_plate)
        Entry(root, width=5, textvariable=tp, disabledbackground='white', disabledforeground='red', state=DISABLED, justify='center').grid(row=19, column = 3)
        lc = StringVar()
        tb_cost = tb_plate * float(p6[2])
        lc.set(f'{tb_cost:.2f}')
        Entry(root, width=5, textvariable=lc, disabledbackground='red', disabledforeground='white', state=DISABLED, justify='center').grid(row=19, column = 4)


        Label(root, text=(f"16 foot pressure treated base plates")).grid(row=20, column = 1, columnspan=2, sticky=W)




    
    l1 = Label(root, text='Start To Finish UR Basement', background='white', fg='black')
    l2 = Label(root, text="Answer the questions below to compute your list of materials needed", background='white', fg='black')
    l3 = Label(root, text="What is the height of your room?")
    l4 = Label(root, text="What is the total length of the perimiter?")
    l5 = Label(root, text="How many doors?")
    l6 = Label(root, text="How many windows?" )
    l7 = Label(root, text="How many walls?")
    Label(root, text="").grid(row = 2, column =0)
    Label(root, text="").grid(row = 13, column =0)
    # Label(root, text="").grid(row = 15, column =0)

    
    l1.grid(row = 0, column = 1, columnspan=4)
    l2.grid(row = 1, column = 1, columnspan=4)
    l3.grid(row = 3, column = 1, columnspan=2)
    l4.grid(row = 5, column = 1, columnspan=2)
    l5.grid(row = 7, column = 1, columnspan=2)
    l6.grid(row = 9, column = 1, columnspan=2)
    l7.grid(row = 11, column =1, columnspan=2)
    

    submit_button = Button(root, text="Submit", command = myClick, padx=30)
    submit_button.grid(row=14,column=1)

    clear_button = Button(root, text="Clear", command = click_clear, padx=30 )
    clear_button.grid(row=14,column=3)


    Label(root, text="________________________________________________").grid(row = 15, column =0, columnspan=4)
    Label(root, text="Item Number").grid(row = 16, column =0)
    Label(root, text="Discription").grid(row = 16, column =1, columnspan=2)
    Label(root, text="Quantity").grid(row = 16, column =3)
    Label(root, text="Total Cost", border=6 ).grid(row = 16, column =4)

    # Entry(root, width=100, disabledbackground='lightgray', state=DISABLED, justify='center').grid(row=16, column = 0, columnspan=4, )


    

    root.mainloop()

    # rooms = int(input("How many total rooms will you be finishing?"))
    
    # total_rooms = floor_plan(rooms)


    # print(f"this is the total number of rooms: {total_rooms}")





if __name__ == "__main__":
    main()