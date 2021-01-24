from tkinter import *
import sys

team_1_array= []
double = False


master = Tk()

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
        ws_2 = Label(confirm_screen, text=" ").grid(row=1, column=0)
        ws_2 = Label(confirm_screen, text=" ").grid(row=2, column=0)
        t1_name = Label(confirm_screen, text = "Team 1: " + team_1).grid(row = 1, column = 1)
        t2_name = Label(confirm_screen, text="Team 2: " + team_2).grid(row = 1, column = 2)
        confirm_button = Button(confirm_screen, text = "Submit", width = 10, command = lambda: team_names(team_1)).grid(row = 4, column = 1)
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

def team_names(team):
    global team_amount
    global team_name_input
    global team_amount_test
    team_name_input = Toplevel(master)
    confirm_screen.withdraw()
    enter_names = Label(team_name_input, text = "Enter amount of players in " + team).grid(row = 0, column = 1)
    enter_names2 = Label(team_name_input, text="(Between 2 and 11)").grid(row=1, column=1)
    team_amount_test = Entry(team_name_input, width = 20)
    team_amount_test.grid(row = 2, column = 1)
    submit_amount = Button(team_name_input, text="Submit", command= lambda:amount_validation(team_1_array)).grid(row=3, column=1)
    #print(isinstance(team_amount, int))

def amount_validation(team_array):
    team_num = 1
    team_amount = int(team_amount_test.get())
    if team_num == 1:
        current_team = team_1
    elif team_num == 2:
        current_team = team_2



    if team_amount < 2 or team_amount > 11:
        error = Label(team_name_input, text = "Invalid amount, try again").grid(row = 4, column = 1)
    elif team_amount > 2 or team_amount < 11:
        player_num = 1
        name_input_win = Toplevel(master)
        #name_input_win.geometry("200x150")
        team_name_input.withdraw()
        first = Label(name_input_win, text = "Enter player " + str(player_num) + " for " + str(current_team)).grid(row = 0, column = 1)
        name_input = Entry(name_input_win)
        name_input.grid(row = 1, column = 1)
        name = str(name_input.get())
        for i in range(0, player_num):
            p = None
        while not p or p in team_array:
            #first = Label(name_input, text="Enter player " + str(player_num) + " for " + str(current_team)).grid(row=0,column=1)
            if p in team_array:
                error = Label(name_input, text = "Player already entered").grid(row = 2, column = 1)
        team_array.append(p)
        player_num = player_num + 1






mainloop()


