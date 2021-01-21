from tkinter import *
import sys

team_1 = ""
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
    if t2_entry.get() == team_1:
        error = Label(top_2, text = "Invalid Team Name, try again").grid(row = 2, column = 1)
    elif t2_entry.get() != team_1:
        team_2 = t2_entry.get()
        top_2.withdraw()
        confirm_screen = confirm_win = Toplevel(master)
        ws_2 = Label(confirm_screen, text=" ").grid(row=1, column=0)
        ws_2 = Label(confirm_screen, text=" ").grid(row=2, column=0)
        t1_name = Label(confirm_screen, text = "Team 1: " + team_1).grid(row = 1, column = 2)
        t2_name = Label(confirm_screen, text="Team 2: " + team_2).grid(row = 2, column = 2)





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








mainloop()


