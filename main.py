from tkinter import *
import sys
from time import sleep

team_1_array= []
team_2_array = []
double = False
t1_amount = 0
t2_amount = 0



master = Tk()

master.attributes("-topmost", True)

###WS = White space
####HELP MENU

def help_menu():
    top = Toplevel(master)
    top.title("Help Menu")
    heading = Label(top, text = "Help Menu").grid(row = 0, column = 1)
    headin_ws = Label(top, text = " ").grid(row = 1, column = 1)
    help_1 = Label(top, text = "-This program is designed to keep track").grid(row = 2, column = 1)
    help_1 = Label(top, text=" of scores during a cricket game").grid(row = 3, column = 1)
    help_2 = Label(top, text = "-Any issues that you may think").grid(row = 4, column = 1)
    help_2 = Label(top, text=" areise from the code of the game, contact").grid(row = 5, column = 1)
    help_2 = Label(top, text=" the developer").grid(row = 6, column = 1)
    help_3 = Label(top, text= "-Please reffer to the included").grid(row = 7, column = 1)
    help_3 = Label(top, text=" instruction guide for more help").grid(row = 8, column = 1)
    leave_button = Button(top, text = "EXIT", command = top.destroy).grid(row = 9, column = 1)


def start_team1():
    global t1_entry
    top_1 = Toplevel(master)
    master.withdraw()
    top_1.title("Hows That?")
    def start_team2():
        global team_1
        global t2_entry
        global top_2
        team_1 = t1_entry.get()
        top_2 = Toplevel(master)
        top_1.withdraw()
        top_2.title("Hows That?")
        team2_name = Label(top_2, text="Enter Team 2's team name: ").grid(row=0, column=1)
        previous = "Team 1: " + team_1
        previouslb = Label(top_2, text = previous).grid(row=2, column=1)
        t2_entry = Entry(top_2, width=20)
        t2_entry.grid(row=1, column=1)
        ws_2 = Label(top_2, text=" ").grid(row=3, column=1)
        submit_button = Button(top_2, text="SUBMIT", command=save_team2_names).grid(row=4, column=1)

    team1_name = Label(top_1, text = "Enter Team 1's team name: ").grid(row = 0, column = 1)
    t1_entry = Entry(top_1, width = 20)
    t1_entry.grid(row = 1, column = 1)
    #ws_1 = Label(top_1, text = " ").grid(row = 2, column = 1)
    submit_button = Button(top_1, text = "SUBMIT", command = start_team2).grid(row = 3, column = 1)



def save_team2_names():
    global team_2
    global confirm_screen
    if t2_entry.get() == team_1:
        error = Label(top_2, text = "Invalid Team Name, try again").grid(row = 2, column = 1)
    elif t2_entry.get() != team_1:
        team_2 = t2_entry.get()
        top_2.withdraw()
        confirm_screen = Toplevel(master)
        t1_name = Label(confirm_screen, text = "Team 1: " + team_1).grid(row = 1, column = 1)
        t2_name = Label(confirm_screen, text="Team 2: " + team_2).grid(row = 1, column = 2)
        confirm_button = Button(confirm_screen, text = "Submit", width = 10, command = team_name_1).grid(row = 4, column = 1)
        redo = Button(confirm_screen, text="Redo", width=10, command= lambda: [start_team1(), clear()]).grid(row=4, column=2)

def clear():
    confirm_screen.withdraw()



#SETTING UP MAIN SCREEN
welcome_label = Label(master, text = 'Welcome to "Hows That?"')
white_space_welcome = Label(master, text = " ")
white_space_welcome2 = Label(master, text = " ")
white_space_welcome3 = Label(master, text = " ")

help_menu_button = Button(master, text = "HELP", command = help_menu)
start_button = Button(master, text = "START", command = start_team1)
exit_button = Button(master, text = "EXIT", command = sys.exit)


welcome_label.grid(row = 0, column = 1)
white_space_welcome.grid(row = 1, column = 1)
white_space_welcome2.grid(row = 2, column = 1)
white_space_welcome3.grid(row = 3, column = 1)
help_menu_button.grid(row = 4, column = 0)
start_button.grid(row = 4, column = 1)
exit_button.grid(row = 4, column = 2)


####AFTER CONFIRMING TEAMS

def team_name_1():
    global team_name_input
    global team_amount_test
    team_name_input = Toplevel(master)
    confirm_screen.withdraw()
    enter_names = Label(team_name_input, text = "Enter amount of players in " + team_1).grid(row = 0, column = 1)
    enter_names2 = Label(team_name_input, text="(Between 2 and 11)").grid(row=1, column=1)
    team_amount_test = Entry(team_name_input, width = 20)
    team_amount_test.grid(row = 2, column = 1)
    submit_amount = Button(team_name_input, text="Submit", command= amount_validation_1).grid(row=3, column=1)


def amount_validation_1():
    global t1_amount
    team_amount = int(team_amount_test.get())
    if team_amount < 2 or team_amount > 11:
        error = Label(team_name_input, text = "Invalid amount, try again").grid(row = 4, column = 1)
    elif team_amount > 2 or team_amount < 11:
        t1_amount = team_amount
        global team_name_input2
        global team_amount_test2
        team_name_input2 = Toplevel(master)
        team_name_input.withdraw()
        enter_names = Label(team_name_input2, text="Enter amount of players in " + team_2).grid(row=0, column=1)
        enter_names2 = Label(team_name_input2, text="(Between 2 and 11)").grid(row=1, column=1)
        team_amount_test2 = Entry(team_name_input2, width=20)
        team_amount_test2.grid(row=2, column=1)
        submit_amount = Button(team_name_input2, text="Submit", command= final_confirm).grid(row=3, column=1)

def final_confirm():
    global final_confirm
    global t2_amount
    t2_amount = int(team_amount_test2.get())
    if t2_amount < 2 or t2_amount > 11:
        error = Label(team_name_input2, text = "Invalid amount, try again").grid(row = 4, column = 1)
    elif t2_amount > 2 or t2_amount < 11:
        final_confirm = Toplevel(master)
        team_name_input2.withdraw()
        con_title = Label(final_confirm, text = "Please ensure that all information is correct").grid(row = 0, column = 1)
        t1_con = Label(final_confirm, text = str(team_1) + ": " + str(t1_amount) + " players").grid(row = 1, column = 1)
        t2_con = Label(final_confirm, text = str(team_2) + ": " + str(t2_amount) + " players").grid(row = 2, column = 1)
        button_con = Button(final_confirm, text = "Confirm", command = input_stub).grid(row = 3, column = 1)
        button_redo = Button(final_confirm, text="Redo", command = save_team2_names).grid(row=3, column=2)


player_num = 0
display_num = 1
dupe = False
##TEAM 1 Input
def input_stub():
    global player_num
    global name_entry
    global display_num
    if player_num != t1_amount:
        t1_input = Toplevel(master)
        final_confirm.withdraw()
        title = Label(t1_input, text = "Team 1 Input").grid(row = 0, column = 1)
        request = Label(t1_input, text = "Please enter player " + str(display_num) + " name").grid(row = 1, column = 1)
        name_entry = Entry(t1_input)
        name_entry.grid(row = 2, column = 1)
        display_num = display_num + 1
        valid_button = Button(t1_input, text = "Submit", command = lambda: t1_validation(team_1_array)).grid(row = 4, column = 1)
        def t1_validation(current_team):
            global t1_confirm
            global player_num
            global display_num
            global team_1_array
            global player_num
            global dupe
            elem = t1_amount
            current_player_trans = name_entry.get()
            current_team.append(current_player_trans)
            player_num = player_num + 1
            if player_num != t1_amount:
                t1_input.destroy()
                input_stub()
            elif player_num == t1_amount:
                for i in range(0, len(team_1_array)):
                    for j in range(i + 1, len(team_1_array)):
                        if (team_1_array[i] == team_1_array[j]):
                            dupe = True
                if dupe == True:
                    team_1_array = []
                    error = Label(t1_input, text = "Error").grid(row = 4, column = 1)
                    display_num = 1
                    player_num = 0
                    sleep(4)
                    t1_input.destroy()
                    input_stub()
                if dupe == False:
                    t1_confirm = Toplevel(master)
                    t1_input.withdraw()
                    t1_confirm.geometry("200x200")
                    player_count = 1
                    for i in range(len(team_1_array)):
                        exec('Label%d=Label(t1_confirm,text="%s")\nLabel%d.pack()' % (i, "Player " + str(player_count) + " : " + team_1_array[i], i))
                        player_count = player_count + 1
                    confirm_button = Button(t1_confirm, text = "Confirm Team 1", command = input_stub_2).pack()



player_num_2 = 0
display_num_2 = 1

##TEAM 2 INPUT

player_num2 = 0
display_num2 = 1
dupe = False
##TEAM 1 Input
def input_stub_2():
    global player_num2
    global name_entry
    global display_num2
    if player_num != t2_amount:
        t2_input = Toplevel(master)
        t1_input.withdraw()
        title = Label(t2_input, text = "Team 2 Input").grid(row = 0, column = 1)
        request = Label(t2_input, text = "Please enter player " + str(display_num2) + " name").grid(row = 1, column = 1)
        name_entry = Entry(t2_input)
        name_entry.grid(row = 2, column = 1)
        display_num2 = display_num2 + 1
        valid_button = Button(t2_input, text = "Submit", command = lambda: t2_validation(team_2_array)).grid(row = 4, column = 1)
        def t1_validation(current_team):
            global t2_confirm
            global player_num2
            global display_num2
            global team_2_array
            global dupe
            elem = t2_amount
            current_player_trans = name_entry.get()
            current_team.append(current_player_trans)
            player_num2 = player_num2 + 1
            if player_num != t2_amount:
                t2_input.destroy()
                input_stub_2()
            elif player_num == t2_amount:
                for i in range(0, len(team_2_array)):
                    for j in range(i + 1, len(team_2_array)):
                        if (team_2_array[i] == team_2_array[j]):
                            dupe = True
                if dupe == True:
                    team_2_array = []
                    error = Label(t2_input, text = "Error").grid(row = 5, column = 1)
                    display_num2 = 1
                    player_num2 = 0
                    sleep(4)
                    t2_input.destroy()
                    input_stub_2()
                if dupe == False:
                    t2_confirm = Toplevel(master)
                    t2_input.withdraw()
                    t2_confirm.geometry("200x200")
                    player_count2 = 1
                    for i in range(len(team_1_array)):
                        exec('Label%d=Label(t2_confirm,text="%s")\nLabel%d.pack()' % (i, "Player " + str(player_count2) + " : " + team_2_array[i], i))
                        player_count2 = player_count2 + 1
                    confirm_button = Button(t2_confirm, text = "Confirm Team 2", command = full_confirm).pack()




def full_confirm():
    player_count_1 = 1
    player_count_2 = 1
    full_confirm = Toplevel(master)
    t2_confirm.withdraw()
    t1_label = Label(full_confirm, text = "Team: " + team_1).pack()
    for i in range(len(team_1_array)):
        exec('Label%d=Label(full_confirm,text="%s")\nLabel%d.pack()' % (
        i, "Player " + str(player_count_1) + " : " + team_1_array[i], i))
        player_count_1 = player_count_1 + 1
    line = Label(full_confirm, text = "------------").pack()
    t2_label = Label(full_confirm, text= "Team: " + team_2).pack()
    for i in range(len(team_2_array)):
        exec('Label%d=Label(full_confirm,text="%s")\nLabel%d.pack()' % (
        i, "Player " + str(player_count_2) + " : " + team_2_array[i], i))
        player_count_2 = player_count_2 + 1





#ADD A FEATURE AFTER THE USER HAS FINSIHED INPUTTING ARRAY TO COMPRE THE ARRY FOR REPEEATS












#TEST COMMIT











mainloop()