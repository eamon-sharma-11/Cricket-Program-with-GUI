#-----/IMPORT LIBRARIES/-----

from tkinter import *
from tkinter import messagebox
import os

#-----/DECLARE VARIBALES/-----

team_1_array= []
team_2_array = []
t1_amount = 0
t2_amount = 0
batsmen = []
innings = 1
runs = 0
out = 0
over = 0
partnership_runs = 0
ball = 0
out_full = False
out_players = []
facing_player_in_list = 0


master = Tk()




###WS = White space
####HELP MENU

#-----/SIZING WINDOW FUNCTION: This function centers and resizes a winodow based on the contenets in the container/-----
def sizing(window):
    window.update()
    w = window.winfo_width()
    h = window.winfo_height()
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    window.geometry('+%d+%d' % (x, y))


#-----/Hover Button Function: This function changes the colour of the button if the user is hovering over it/-----
def hover(button, colour_too, colour_og):
    def enter(e):
        button['bg'] = colour_too
    def leave(e):
        button['bg'] = colour_og
    button.bind("<Enter>", enter)
    button.bind("<Leave>", leave)



#-----/HELP MENU FUNCATION/-----
def help_menu():
    top = Toplevel(master)
    sizing(top)
    top.configure(bg = "DarkSlateGrey")
    heading = Label(top, text = "Help Menu", font = "Bold", bg = "DarkSlateGrey").grid(row = 0, column = 1)
    headin_ws = Label(top, text = " ", bg = "DarkSlateGrey").grid(row = 1, column = 1)
    help_1 = Label(top, text = "-This program is designed to keep track", bg = "DarkSlateGrey").grid(row = 2, column = 1)
    help_1 = Label(top, text=" of scores during a cricket game", bg = "DarkSlateGrey").grid(row = 3, column = 1)
    help_2 = Label(top, text = "-Any issues that you may think", bg = "DarkSlateGrey").grid(row = 4, column = 1)
    help_2 = Label(top, text=" areise from the code of the game, contact", bg = "DarkSlateGrey").grid(row = 5, column = 1)
    help_2 = Label(top, text=" the developer", bg = "DarkSlateGrey").grid(row = 6, column = 1)
    help_3 = Label(top, text= "-Please reffer to the included", bg = "DarkSlateGrey").grid(row = 7, column = 1)
    help_3 = Label(top, text=" instruction guide for more help", bg = "DarkSlateGrey").grid(row = 8, column = 1)
    help_3 = Label(top, text="Current Version: 1.0.5 Dev Build", bg = "DarkSlateGrey").grid(row=9, column=1)
    leave_button = Button(top, text = "EXIT", command = top.destroy, bg = "SpringGreen3").grid(row = 10, column = 1)


#-----/ENTRY OF TEAM 1 NAME/-----
def start_team1():
    global t1_entry
    top_1 = Toplevel(master)
    top_1.configure(bg = "DarkSlateGrey")
    main_win.withdraw()
    sizing(top_1)
    top_1.title("Hows That?")

    # -----/NESTED FUNCTION FOR ENTERING TEAM 2 NAME/-----
    def start_team2():
        global team_1
        global t2_entry
        global top_2
        team_1 = t1_entry.get()
        top_2 = Toplevel(master)
        top_2.configure(bg = "DarkSlateGrey")
        top_1.withdraw()
        sizing(top_2)
        top_2.title("Hows That?")
        team2_name = Label(top_2, text="Enter Team 2's team name: ", bg="DarkSlateGrey", font="Bold").grid(row=1, column=1)
        t2_entry = Entry(top_2, width=20, bg="DimGrey", font = 20)
        ws = Label(top_2, text=" ", bg="DarkSlateGrey").grid(row=0, column=1)
        ws3 = Label(top_2, text=" ", bg="DarkSlateGrey").grid(row=4, column=1)
        ws2 = Label(top_2, text=" ", bg="DarkSlateGrey").grid(row=6, column=1)
        ws4 = Label(top_2, text=" ", bg="DarkSlateGrey").grid(row=2, column=1)
        t2_entry.grid(row=3, column=1)
        submit_button = Button(top_2, text="SUBMIT", command=save_team2_names, bg="SpringGreen3", font="bold")
        submit_button.grid(row=5, column=1)
        hover(submit_button, "palegreen", "SpringGreen3")

    team1_name = Label(top_1, text = "Enter Team 1's team name: ", bg = "DarkSlateGrey", font = "Bold").grid(row = 1, column = 1)
    t1_entry = Entry(top_1, width = 20, bg = "DimGrey", font = 20)
    ws = Label(top_1, text=" ", bg="DarkSlateGrey").grid(row=0, column=1)
    ws3 = Label(top_1, text=" ", bg = "DarkSlateGrey").grid(row=4, column=1)
    ws2 = Label(top_1, text = " ", bg = "DarkSlateGrey").grid(row = 6, column = 1)
    ws4 = Label(top_1, text=" ", bg="DarkSlateGrey").grid(row=2, column=1)
    t1_entry.grid(row = 3, column = 1)
    submit_button = Button(top_1, text = "SUBMIT", command = start_team2, bg = "SpringGreen3", font = "bold")
    submit_button.grid(row = 5, column = 1)
    hover(submit_button, "palegreen", "SpringGreen3")


#-----/SAVING TEAM 2 NAME + CONFIRMING NAMES/-----
def save_team2_names():
    global team_2
    global confirm_screen
    if t2_entry.get() == team_1:
        error = Label(top_2, text = "Invalid Team Name, try again", bg = "DarkSlateGrey").grid(row = 2, column = 1)
    elif t2_entry.get() != team_1:
        team_2 = t2_entry.get()
        top_2.withdraw()
        confirm_screen = Toplevel(master)
        confirm_screen.configure(bg = "DarkSlateGrey")
        sizing(confirm_screen)
        t1_name = Label(confirm_screen, text = "Team 1: " + team_1, bg = "DarkSlateGrey", font = 10).grid(row = 1, column = 1)
        t2_name = Label(confirm_screen, text="Team 2: " + team_2, bg = "DarkSlateGrey", font = 10).grid(row = 1, column = 3)
        ws = Label(confirm_screen, text = ' ', bg = "DarkSlateGrey").grid(row = 1, column = 2)
        confirm_button = Button(confirm_screen, text = "Submit", width = 10, command = team_name_1, bg = "SpringGreen3", font = 10)
        confirm_button.grid(row = 4, column = 1)
        redo = Button(confirm_screen, text="Redo", width=10, command= lambda: [start_team1(), clear()], bg = "red2", font = 10)
        redo.grid(row=4, column=3)
        hover(confirm_button, "palegreen", "SpringGreen3")
        hover(redo, "tomato", "Red2")

#-----/CLEAR FUNCTION/-----
def clear():
    confirm_screen.withdraw()

#-----/SPLASH SCREEN/-----
sizing(master)
master.title("How's That")
label_ = Label(master, text = "Hows that is").grid(row = 1, column = 1)
label_2 = Label(master, text = "now loading").grid(row = 2, column = 2)






#-----/WELCOME SCREEN/-----
def main():
    try:
        os.remove("test.txt")
    except OSError:
        pass
    global main_win
    master.withdraw()
    main_win = Toplevel(master)
    sizing(main_win)
    main_win.configure(bg = "DarkSlateGrey")
    welcome_label = Label(main_win, text = 'Welcome to "Hows That?"', font = "bold", bg = "DarkSlateGrey")
    with open('test.txt', 'w+') as f:
        pass
    ws2 = Label(main_win, text=" ", bg = "DarkSlateGrey").grid(row=1, column=1)
    version = Label(main_win, text = "Version 1.0.5 Dev Build", bg = "Red2", relief = "ridge", borderwidth = 2, font = 9).grid(column = 1, row = 2)
    new = Label(main_win, text = "Whats New:\n If the exisiting text file is found\n it will be deleted and replaced with a fresh one\n Revamped UI ", bg = "DarkSlateGrey", borderwidth = 2, relief = "solid").grid(row = 4, column = 1)
    ws = Label(main_win, text = " ",bg = "DarkSlateGrey").grid(row = 7, column = 1)
    ws2 = Label(main_win, text = " ", bg = "DarkSlateGrey").grid(row = 8, column = 1)



    help_menu_button = Button(main_win, text = "HELP", command = help_menu, font = "bold", bg = "yellow")
    start_button = Button(main_win, text = "START", command = start_team1, font = "bold", bg = "SpringGreen3")
    exit_button = Button(main_win, text = "EXIT", command = sys.exit, font = "bold", bg = "Red2")

    hover(help_menu_button, "lightyellow", "yellow")
    hover(start_button, "palegreen", "SpringGreen3")
    hover(exit_button, "tomato", "Red2")




    welcome_label.grid(row = 0, column = 1)
    help_menu_button.grid(row = 9, column = 0)
    start_button.grid(row =9, column = 1)
    exit_button.grid(row = 9, column = 2)

master.after(3000, main())


#-----/AMOUNT OF PLAYERS IN TEAM 1/-----
def team_name_1():
    global team_name_input
    global team_amount_test
    team_name_input = Toplevel(master)
    confirm_screen.withdraw()
    team_name_input.configure(bg = "DarkSlateGrey")
    sizing(team_name_input)
    enter_names = Label(team_name_input, text = "Enter amount of players in team: " + team_1, bg = "DarkSlateGrey", font = 10).grid(row = 0, column = 1)
    enter_names2 = Label(team_name_input, text="(Between 2 and 11)", bg = "DarkSlateGrey", font = 5).grid(row=1, column=1)
    ws = Label(team_name_input, text = "", bg = "DarkSlategrey").grid(row = 3, column = 1)
    team_amount_test = Entry(team_name_input, width = 20, bg = "DimGrey", font = 20)
    team_amount_test.grid(row = 2, column = 1)
    submit_amount = Button(team_name_input, text="Submit", command= amount_validation_1, bg = "SpringGreen3", font = 5)
    submit_amount.grid(row=4, column=1)
    hover(submit_amount, "palegreen", "SpringGreen3")

#-----/CHECKING USER ENTRY IS WITHIN ALLOWED VALUES/-----
def amount_validation_1():
    global t1_amount
    team_amount = int(team_amount_test.get())
    if team_amount < 2 or team_amount > 11:
        error = Label(team_name_input, text = "Invalid amount, try again", bg = "DarkSlateGrey").grid(row = 4, column = 1)
    elif team_amount > 2 or team_amount < 11:
        t1_amount = team_amount
        global team_name_input2
        global team_amount_test2
        team_name_input2 = Toplevel(master)
        team_name_input.withdraw()
        team_name_input2.configure(bg = "DarkSlateGrey")
        sizing(team_name_input2)
        enter_names = Label(team_name_input2, text="Enter amount of players in team: " + team_2, bg = "DarkSlateGrey", font = 10).grid(row=0, column=1)
        enter_names2 = Label(team_name_input2, text="(Between 2 and 11)", bg = "DarkSlateGrey", font = 5).grid(row=1, column=1)
        team_amount_test2 = Entry(team_name_input2, width=20, bg = "DimGrey", font = 20)
        team_amount_test2.grid(row=2, column=1)
        ws = Label(team_name_input2, text = " ", bg = "DarkSlateGrey").grid(row = 3, column = 1)
        submit_amount = Button(team_name_input2, text="Submit", command= final_confirm, bg = "SpringGreen3", font = "bold")
        submit_amount.grid(row=4, column=1)
        hover(submit_amount, "palegreen", "SpringGreen3")

#-----/CONFIRMING AMOUNT OF PLAYERS IN EACH TEAM/-----
def final_confirm():
    global final_confirm
    global t2_amount
    t2_amount = int(team_amount_test2.get())
    if t2_amount < 2 or t2_amount > 11:
        error = Label(team_name_input2, text = "Invalid amount, try again").grid(row = 4, column = 1)
    elif t2_amount > 2 or t2_amount < 11:
        final_confirm = Toplevel(master)
        team_name_input2.withdraw()
        final_confirm.configure(bg = "DarkSlateGrey")
        sizing(final_confirm)
        con_title = Label(final_confirm, text = "Please ensure that all information is correct", bg = "DarkSlateGrey", font = "bold").grid(row = 0, column = 1)
        t1_con = Label(final_confirm, text = str(team_1) + ": " + str(t1_amount) + " players", bg = "DarkSlateGrey", font = 10).grid(row = 1, column = 1)
        t2_con = Label(final_confirm, text = str(team_2) + ": " + str(t2_amount) + " players", bg = "DarkSlateGrey", font = 10).grid(row = 2, column = 1)
        button_con = Button(final_confirm, text = "Confirm", command = input_stub, bg = "SpringGreen3", font = "bold")
        button_con.grid(row = 3, column = 1)
        button_redo = Button(final_confirm, text="Redo", command = save_team2_names, bg = "Red2", font = "bold")
        button_redo.grid(row=4, column=1)
        hover(button_con, "PaleGreen", "SpringGreen3")
        hover(button_redo, "tomato", "Red2")


#-----/POPUP ERROR FUNCTION/-----
def error_popup_teams():
    global response
    response = messagebox.showerror("Error Popup", "Duplicate player found, please re-enter names")
    return response

#-----/TEAM 1 PLAYER NAME INPUT/-----
player_num = 0
display_num = 1
##TEAM 1 Input
def input_stub():
    global player_num
    global name_entry
    global display_num
    global dupe
    global t1_input
    if player_num != t1_amount:
        dupe = False
        t1_input = Toplevel(master)
        t1_input.configure(bg = "DarkSlateGrey")
        final_confirm.withdraw()
        sizing(t1_input)
        title = Label(t1_input, text = team_1 + " Input", bg = "DarkSlateGrey", font = "bold").grid(row = 0, column = 1)
        request = Label(t1_input, text = "Please enter player " + str(display_num) + " name", bg = "DarkSlateGrey", font = 10).grid(row = 1, column = 1)
        name_entry = Entry(t1_input, bg = "DimGrey", font = 20)
        name_entry.grid(row = 2, column = 1)
        display_num = display_num + 1
        ws = Label(t1_input, text = " ", bg = "DarkSlateGrey").grid(row = 4, column = 1)
        valid_button = Button(t1_input, text = "Submit", command = lambda: t1_validation(team_1_array), bg = "SpringGreen3", font = "bold")
        valid_button.grid(row = 5, column = 1)
        hover(valid_button, "palegreen", "SpringGreen3")

        # -----/VALIDATING THE PLAYERS TO ENSURE NO DUPLICATES/-----
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
                    error_popup_teams()
                    if response == "ok":
                        team_1_array.clear()
                        error = Toplevel(t1_input)
                        display_num = 1
                        player_num = 0
                        error.destroy()
                        t1_input.destroy()
                        input_stub()
                elif dupe == False:
                    t1_confirm = Toplevel(master)
                    t1_input.withdraw()
                    sizing(t1_confirm)
                    t1_confirm.configure(bg = "DarkSlateGrey")
                    player_count = 1
                    for i in range(len(team_1_array)):
                        exec('Label%d=Label(t1_confirm,text="%s", bg = "DarkSlateGrey", font = "bold")\nLabel%d.pack()' % (i, "Player " + str(player_count) + " : " + team_1_array[i], i))
                        player_count = player_count + 1
                    ws = Label(t1_confirm, text = " ", bg = "DarkSlateGrey").pack()
                    confirm_button = Button(t1_confirm, text = "Confirm Team 1", command = input_stub_2, bg = "SpringGreen3", font = "bold")
                    confirm_button.pack()
                    hover(confirm_button, "PaleGreen", "SpringGreen3")

#-----/TEAM 2 PLAYER INPUT/-----

player_num2 = 0
display_num2 = 1
def input_stub_2():
    global player_num2
    global name_entry
    global display_num2
    global dupe
    global t2_input
    if player_num2 != t2_amount:
        dupe = False
        t2_input = Toplevel(master)
        t1_confirm.withdraw()
        t2_input.configure(bg = "DarkSlateGrey")
        sizing(t2_input)
        title = Label(t2_input, text = team_2 + " Input", bg = "DarkSlateGrey", font = "bold").grid(row = 0, column = 1)
        request = Label(t2_input, text = "Please enter player " + str(display_num2) + " name", bg = "DarkSlateGrey", font = 10).grid(row = 1, column = 1)
        name_entry = Entry(t2_input, bg = "DimGrey", font = 20)
        name_entry.grid(row = 2, column = 1)
        display_num2 = display_num2 + 1
        ws = Label(t2_input, text = " ", bg = "DarkSlateGrey").grid(row = 3, column = 1)
        valid_button = Button(t2_input, text = "Submit", command = lambda: t2_validation(team_2_array), bg = "SpringGreen3", font = "bold")
        valid_button.grid(row = 4, column = 1)
        hover(valid_button, "PaleGreen", "SpringGreen3")

        # -----/VALIDATING PLAYERS TO ENSURE NO DUPLICATES/-----

def t2_validation(current_team):
            global display_num2
            global t2_confirm
            global player_num2
            global display_num
            global team_2_array
            global player_num2
            global dupe
            elem = t2_amount
            current_player_trans = name_entry.get()
            current_team.append(current_player_trans)
            player_num2 = player_num2 + 1
            if player_num2 != t2_amount:
                t2_input.destroy()
                input_stub_2()
            elif player_num2 == t2_amount:
                for i in range(0, len(team_2_array)):
                    for j in range(i + 1, len(team_2_array)):
                        if (team_2_array[i] == team_2_array[j]):
                            dupe = True
                if dupe == True:
                    error_popup_teams()
                    if response == "ok":
                        team_2_array.clear()
                        error = Toplevel(t2_input)
                        display_num2 = 1
                        player_num2 = 0
                        error.destroy()
                        t2_input.destroy()
                        input_stub_2()
                elif dupe == False:
                    t2_confirm = Toplevel(master)
                    t2_input.withdraw()
                    t2_confirm.configure(bg = "DarkSlateGrey")
                    sizing(t2_confirm)
                    player_count = 1
                    for i in range(len(team_2_array)):
                        exec('Label%d=Label(t2_confirm,text="%s",bg = "DarkSlateGrey", font = "bold")\nLabel%d.pack()' % (i, "Player " + str(player_count) + " : " + team_2_array[i], i))
                        player_count = player_count + 1
                    ws = Label(t2_confirm, text = " ", bg = "DarkSlateGrey").pack()
                    confirm_button = Button(t2_confirm, text = "Confirm Team 2", command = full_confirm_func, bg = "SpringGreen3", font = "bold")
                    confirm_button.pack()
                    hover(confirm_button, "PaleGreen", "SpringGreen3")

#-----/FULL CONFIRMATION OF PLAYERS IN RESPECTIVE TEAMS/-----

def full_confirm_func():
    global full_confirm
    global team_1_array
    global team_2_array
    player_count_1 = 1
    player_count_2 = 1
    full_confirm = Toplevel(master)
    t2_confirm.withdraw()
    full_confirm.configure(bg = "DarkSlateGrey")
    sizing(full_confirm)
    t1_label = Label(full_confirm, text = "Team: " + team_1, bg = "DarkSlateGrey", font = "bold").pack()
    for i in range(len(team_1_array)):
        exec('Label%d=Label(full_confirm,text="%s", bg = "DarkSlateGrey", font = 10)\nLabel%d.pack()' % (
        i, "Player " + str(player_count_1) + " : " + team_1_array[i], i))
        player_count_1 = player_count_1 + 1
    line = Label(full_confirm, text = "------------", bg = "DarkSlateGrey").pack()
    t2_label = Label(full_confirm, text= "Team: " + team_2, bg = "DarkSlateGrey", font = "Bold").pack()
    for i in range(len(team_2_array)):
        exec('Label%d=Label(full_confirm,text="%s", bg = "DarkSlateGrey", font = 10)\nLabel%d.pack()' % (
        i, "Player " + str(player_count_2) + " : " + team_2_array[i], i))
        player_count_2 = player_count_2 + 1
    submit = Button(full_confirm, text = "Submit", command = choosing_sides_func, bg = "SpringGreen3", font = "bold")
    submit.pack()
    back = Button(full_confirm, text="Redo Name input", command= lambda: reset_player_num(player_num, display_num, player_num2, display_num2), bg = "Red2", font = "bold")
    back.pack()
    hover(submit, "PaleGreen", "SpringGreen3")
    hover(back, "tomato", "Red2")

#-----/RESETING GAME VALUES/-----

def reset_player_num(player1, display1, display2, player2):
    player1 = 0
    display1 = 1
    player2 = 0
    display2 = 1
    input_stub()

#-----/SELECTING EITHER BATTING OF BOWLING FOR EACH TEAM/-----

def choosing_sides_func():
    global choosing_sides
    choosing_sides = Toplevel(master)
    full_confirm.withdraw()
    choosing_sides.configure(bg = "DarkSlateGrey")
    sizing(choosing_sides)
    title = Label(choosing_sides, text = "Which team is batting first?", bg = "DarkSlateGrey", font = "bold").grid(row = 0, column = 1)
    ws = Label(choosing_sides, text = " ", bg = "DarkSlateBlue").grid(row = 1, column = 1)
    t1_batting_button = Button(choosing_sides, text = team_1, command = lambda: [t1_batting(team_1_array, team_2_array), team_set(1)], bg = "LimeGreen", font = "bold")
    t1_batting_button.grid(row = 2,column = 1)
    t2_batting_button = Button(choosing_sides, text=team_2, command= lambda: [t1_batting(team_2_array, team_1_array), team_set(2)], bg = "Cyan2", font = "bold")
    t2_batting_button.grid(row=3, column=1)
    hover(t1_batting_button, "LimeGreen", "GreenYellow")
    hover(t2_batting_button, "turquoise1", "Cyan2")

#-----/PLACING PLAYERS IN NEW ARRAY/-----

def t1_batting(Batting, Fielding):
    global batting_team
    global fielding_team
    global batting_team_copy

    fielding_team = [None] * len(Fielding)
    for i in range(0, len(Fielding)):
        fielding_team[i] = Fielding[i]

    ###COPY OF BATTING TEAM
    batting_team_copy = [None] * len(Batting)
    for i in range(0, len(Batting)):
        batting_team_copy[i] = Batting[i]


    # Batting Team set
    batting_team = [None] * len(Batting)
    for i in range(0, len(Batting)):
        batting_team[i] = Batting[i]

    list_teams_stub(batting_team, fielding_team)

#-----/GLOBAL VARIABLES SO THAT FUNCTIONS KNOW WHOS BATTING AND BOWLING/-----

def team_set(team):
    global first_team
    global team_facing
    global team_not
    if team == 1:
        first_team = "t1"
        team_facing = team_1
        team_not = team_2
    if team == 2:
        first_team = "t2"
        team_facing = team_2
        team_not = team_1

#-----/LISTING ALL RELEVENT INFORMATION/-----

def list_teams_stub(bt, ft):
    global list_teams
    player_count_3 = 1
    player_count_4 = 1
    list_teams = Toplevel(master)
    choosing_sides.withdraw()
    list_teams.configure(bg = "DarkSlateGrey")
    sizing(list_teams)
    batting = Label(list_teams, text = "Batting Team:", bg = "DarkSlateGrey", font = "Bold").pack()
    for i in range(len(bt)):
        exec('Label%d=Label(list_teams,text="%s",bg = "DarkSlateGrey", font = 10)\nLabel%d.pack()' % (i, "Player " + str(player_count_3) + " : " + bt[i], i))
        player_count_3 = player_count_3 + 1
    line = Label(list_teams, text="----------", bg = "DarkSlateGrey", font = "Bold").pack()
    fielding = Label(list_teams, text="Fielding Team:", bg = "DarkSlateGrey").pack()
    for i in range(len(ft)):
        exec('Label%d=Label(list_teams,text="%s",bg = "DarkSlateGrey")\nLabel%d.pack()' % (i, "Player " + str(player_count_4) + " : " + ft[i], i))
        player_count_4 = player_count_4 + 1
    next = Button(list_teams, text = "Confirm", command = match_type_stub(), bg = "SpringGreen3")
    next.pack()
    hover(next, "PaleGreen", "SpringGreen3")

#-----/CHOOSING LENGTH OF GAME/-----

def match_type_stub():
    global match_type
    match_type = Toplevel(master)
    match_type.configure(bg = "DarkSlateGrey")
    list_teams.withdraw()
    sizing(match_type)
    title_1 = Label(match_type, text = "What type of game", bg = "DarkSlateGrey").grid(row = 0, column = 1)
    title_2 = Label(match_type, text = "do you want to play?", bg = "DarkSlateGrey").grid(row = 1, column =1)
    T20 = Button(match_type, text = "T20", command = lambda: match_type_set(20), bg = "RoyalBlue1")
    T20.grid(row = 2, column = 1)
    One_day = Button(match_type, text="One Day", command = lambda: match_type_set(50), bg = "SpringGreen2")
    One_day.grid(row=3, column=1)
    Custom = Button(match_type, text="Custom", command= custom_over, bg = "Red2")
    Custom.grid(row=4, column=1)
    hover(T20, "dodgerBlue", "RoyalBlue1")
    hover(One_day, "PaleGreen", "SpringGreen2")
    hover(Custom, "tomato", "Red2")

#-----/DECLARING RUN AMOUNTS/-----

def match_type_set(type):
    global over_amount
    if type == 20:
        over_amount = 20
    elif type == 50:
        over_amount = 50
    batsmen_1(0, 0, None, None, 0, None, 0, 0)

#-----/CUSTOM OVER AMOUNT/-----

co_flag = False
def custom_over():
    global cust_over
    global amount
    global co_flag
    co_flag = True
    cust_over = Toplevel(master)
    cust_over.configure(bg = "DarkSlateGrey")
    match_type.withdraw()
    sizing(cust_over)
    title = Label(cust_over, text = "Input custom over amount", bg = "DarkSlateGrey").grid(row = 0, column = 1)
    title = Label(cust_over, text="(Between 10-50)", bg = "DarkSlateGrey").grid(row=1, column=1)
    amount = Entry(cust_over, bg = "DimGrey")
    amount.grid(row = 2, column = 1)
    submit = Button(cust_over, text = "Submit", command = lambda: [batsmen_1(0, 0, None, None, 0, None, 0, 0), clear_win_1()], bg = "SpringGreen3")
    submit.grid(row = 3, column = 1)
    hover(submit, "PaleGreen", "SpringGreen3")

#-----/CLEAR WINODW FUNCTION/-----

def clear_win_1():
    cust_over.withdraw()

#-----/CHOOSING FIRST BATSMEN/-----

def batsmen_1(balls, run, facing, other, over, current_bowler, patnership, out):
    global batsmen_win
    global batsmen
    global innings
    global over_amount4
    if co_flag == True:
        over_amount = amount.get()
        over_amount = int(over_amount)
        if over_amount < 10 or over_amount > 50:
            error = Label(cust_over, text = "Error, out of range", bg = "DarkSlateGrey").grid(row = 4, column = 1)
        elif co_flag == False:
            cust_over.withdraw()
    batsmen_win = Toplevel(master)
    match_type.withdraw()
    batsmen_win.configure(bg = "DarkSlateGrey")
    sizing(batsmen_win)
    itle = Label(batsmen_win, text="Choose the first batsmen", bg = "DarkSlateGrey").grid(row=0, column=1)
    variable = StringVar(batsmen_win)
    variable.set(batting_team[0])  # default value

    w = OptionMenu(batsmen_win, variable, *batting_team)
    w.grid(row = 1, column = 1)

    def ok(balls, run, facing, other, over, current_bowler, patnership, out):
        global batsmen
        batsmen.append(variable.get())
        for players in batting_team:
            if players == batsmen[0]:
                batting_team.remove(batsmen[0])
        batsmen_2(balls, run, facing, other, over, current_bowler, patnership, out)

    button = Button(batsmen_win, text="OK", command=lambda: ok(balls, run, facing, other, over, current_bowler, patnership, out), bg = "SpringGreen3")
    button.grid(row = 2, column = 1)
    hover(button, "PaleGreen", "SpringGreen3")

#-----/CHOOSING SECOND BATSMEN/-----

def batsmen_2(balls, run, facing, other, over, current_bowler, patnership, out):
    global batsmen_win_2
    global batsmen
    global other_batsmen
    batsmen_win_2 = Toplevel(master)
    batsmen_win_2.configure(bg = "DarkSlateGrey")
    batsmen_win.withdraw()
    sizing(batsmen_win_2)
    variable = StringVar(batsmen_win_2)
    variable.set(batting_team[0])  # default value
    title = Label(batsmen_win_2, text = "Choose the second batsmen", bg = "DarkSlateGrey").grid(row =0, column = 1)


    w = OptionMenu(batsmen_win_2, variable, *batting_team)
    w.grid(row = 1, column = 1)

    def ok1(balls, run, facing, other, over, current_bowler, patnership, out):
        global batsmen
        batsmen.append(variable.get())
        for players in batting_team:
            if players == batsmen[1]:
                batting_team.remove(batsmen[1])
        bowler(balls, run, facing, other, over, current_bowler, patnership, out)

    button = Button(batsmen_win_2, text="OK", command= lambda: ok1(balls, run, facing, other, over, current_bowler, patnership, out), bg = "SpringGreen3")
    button.grid(row = 2, column = 1)
    hover(button, "PaleGreen", "SpringGreen3")

#-----/SELECTING BOWLER/-----

def bowler(balls, run, facing, other, over, current_bowler, patnership, out):
    global bowler_win
    bowler_win = Toplevel(master)
    bowler_win.configure(bg = "DarkSlateGrey")
    batsmen_win_2.withdraw()
    sizing(bowler_win)
    variable = StringVar(bowler_win)
    variable.set(fielding_team[0])
    title = Label(bowler_win, text = "Please choose the bowler", bg = "DarkSlateGrey").grid(row = 0, column = 1)

    w = OptionMenu(bowler_win, variable, *fielding_team)
    w.grid(row = 1, column = 1)

    def ok2(balls, run, facing, other, over, current_bowler, patnership, out):
        global fielding_team
        current_bowler = variable.get()
        for players in fielding_team:
            if players == current_bowler:
                fielding_team.remove(current_bowler)
        setting_batsmen(balls, run, facing, other, over, current_bowler, patnership, out)

    button = Button(bowler_win, text="OK", command= lambda: ok2(balls, run, facing, other, over, current_bowler, patnership, out), bg = "SpringGreen3")
    button.grid(row = 2, column = 1)
    hover(button, "Palegreen", "SpringGreen3")

#-----/PLACING BATSMEN INTO NEW ARRAY/-----

def setting_batsmen(balls, run, facing, other, over, current_bowler, patnership, out):
    global facing_player_in_list
    facing = batsmen[0]
    other = batsmen[1]
    facing_player_in_list = 1
    main_play(0, facing, other, 0, 0, current_bowler, patnership, out)

#-----/PLAY WINODW/-----

def main_play(run, facing, other, over, ball, current_bowler, patnership, out):
    global main_win
    global ctr_right
    global ctr_left
    global top_frame
    global center
    global ctr_mid
    global btm_frame
    global btm_frame2
    with open('test.txt', 'a') as f:
        f.write(f"Ball: {ball}\n")
        f.write(f"Over: {over}\n")
        f.write(f'Current Runs: {run}\n')
        f.write(f'Current Partnership: {patnership}\n')
        f.write(f"Current Bowler: {current_bowler}\n")
    print(batsmen)
    main_win = Toplevel(master)
    sizing(main_win)
    bowler_win.withdraw()
    #Defining Frame
    top_frame = Frame(main_win, bg='DarkSlateGrey', width=450, height=50, pady=3)
    center = Frame(main_win, bg='gray2', width=50, height=40, padx=3, pady=3, relief = "solid")
    btm_frame = Frame(main_win, bg='white', width=450, height=45, pady=3)
    btm_frame2 = Frame(main_win, bg='lavender', width=450, height=60, pady=3)

    # layout all of the main containers
    main_win.grid_rowconfigure(1, weight=1)
    main_win.grid_columnconfigure(0, weight=1)

    top_frame.grid(row=0, sticky="ew")
    center.grid(row=1, sticky="nsew")
    btm_frame.grid(row=3, sticky="ew")
    btm_frame2.grid(row=4, sticky="ew")

    # create the widgets for the top frame
    model_label = Label(top_frame, text='Model Dimensions')
    model_label.grid(row = 1, column = 1, padx = 282)

    # layout the widgets in the top frame
    model_label.grid(row=0, column=3)

    # create the center widgets
    center.grid_rowconfigure(0, weight=1)
    center.grid_columnconfigure(1, weight=1)

    ctr_left = Frame(center, bg='lavender', width=100, height=145, relief = "solid", borderwidth = 2)
    ctr_mid = Frame(center, bg='light green', width=250, height=145, padx=3, pady=3, relief = "solid", borderwidth = 2)
    ctr_right = Frame(center, bg='lavender', width=100, height=145, padx=3, pady=3, relief = "solid", borderwidth = 2)

    ctr_left.grid(row=0, column=0, sticky="ns")
    ctr_mid.grid(row=0, column=1, sticky="nsew")
    ctr_right.grid(row=0, column=2, sticky="ns")

    ##CENTER FRAME INFO
    facing_label = Label(ctr_mid, text="Facing: " + str(facing), font=25, bg="light green")
    facing_label.grid(row=1, column=5, pady=5, padx=110)
    ws = Label(ctr_mid, text="    ", bg="light green")
    ws.grid(row=2, column=1, pady=70)
    other_title = Label(ctr_mid, text="Other Batsmen: " + other, font=10, bg="light green")
    other_title.grid(row=30, column=5, padx=110, pady=60)
    bowler_title = Label(ctr_mid, text="Bowler: " + current_bowler, font=10, bg="light green")
    bowler_title.grid(row=40, column=5, padx=110, )

    score_title = Label(ctr_left, text="Score:", font=10, relief = "ridge")
    score_title.grid(row=0, column=1, pady=60, padx=20)
    score = Label(ctr_left, text="Runs: " + str(run), font=10, relief = "ridge")
    score.grid(row=1, column=1, padx=20)
    out_label = Label(ctr_left, text="Outs: " + str(out), font=10, relief = "ridge")
    out_label.grid(row=2, column=1, pady=60)

    info_title = Label(ctr_right, text="Info:", font=10, relief = "ridge")
    info_title.grid(row=0, column=1, pady=60, padx=20)
    ball_amount = Label(ctr_right, text="Balls: " + str(ball), font=10, relief = "ridge")
    ball_amount.grid(row=1, column=1, padx=20)
    over_label = Label(ctr_right, text="Over: " + str(over), font=10, relief = "ridge")
    over_label.grid(row=2, column=1, pady=60)

    # Bottom frame button

    move_on = Button(btm_frame, text="Play!", command= lambda: play_func(ball, run, facing, other, over, current_bowler, patnership, out), height=5, width= int(main_win.winfo_width() / 6.6), font=10, bg = "SpringGreen3")
    move_on.grid(column=1, row=1)
    exit = Button(btm_frame, text="Exit!", command=sys.exit, height=5, width= int(main_win.winfo_width() / 6.6), font=10, bg = "Red2")
    exit.grid(column=2, row=1)
    hover(move_on, "PaleGreen", "SpringGreen3")
    hover(exit, "tomato", "Red2")

    current_facing = Label(btm_frame2, text="Batting: " + team_facing, font=20, relief = "ridge")
    other_facing = Label(btm_frame2, text="Bowling: " + team_not, font=20, relief = "ridge")
    current_facing.grid(row=0, column=1, padx=130, pady=18)
    other_facing.grid(row=0, column=2)

#-----/PLAY FUNCATION FOR EITHER OUT OR RUNS/-----

def play_func(balls, run, facing, other, over, current_bowler, patnership, out):
    global play_win
    play_win = Toplevel(master)
    play_win.configure(bg = "DarkSlateGrey")
    sizing(play_win)
    ball = balls + 1
    with open('test.txt', "a") as f:
        f.write(f'{current_bowler} has bowled to {facing}\n')
    title = Label(play_win, text = "Select Outcome of play", bg = "DarkSlateGrey").grid(row = 0, column = 1)
    run_button = Button(play_win, text = "Runs", command = lambda: run_function(ball, run, facing, other, over, current_bowler, patnership, out), bg = "SpringGreen3")
    run_button.grid(row = 1, column = 1)
    out_button = Button(play_win, text="Out", command= lambda: out_function(ball, run, facing, other, over, current_bowler, patnership, out), bg = "Red2")
    out_button.grid(row=2, column=1)
    hover(run_button, "palegreen", "SpringGreen3")
    hover(out_button, "tomato", "Red2")
    return ball

#-----/OUT FUNCTION/-----

##ADD FUNCTION FOR METHOD OF GETTING OUT
def out_function(ball, run, facing, other, over, current_bowler, patnership, out):
    global out_win
    global innings
    partnership = 0
    out = out + 1
    with open('test.txt', 'a') as f:
        f.write("Out\n")
    print("Out function")
    if len(batting_team) == 0:
        innings = innings + 1
        change_sides(ball, run, facing, other, over, current_bowler, patnership, out)
    else:
        out_win = Toplevel(master)
        out_win.configure(bg = "DarkSlateGrey")
        play_win.withdraw()
        sizing(out_win)
        out_players.append(facing)
        facing = other
        variable = StringVar(out_win)
        variable.set(batting_team[0])  # default value
        title = Label(out_win, text="Choose the new batsmen", bg = "DarkSlateGrey").grid(row=0, column=1)

        w = OptionMenu(out_win, variable, *batting_team)
        w.grid(row=1, column=1)

        def ok5(ball, run, facing, other, over, current_bowler, patnership, out):
            other = variable.get()
            for players in batting_team:
                if players == other:
                    batting_team.remove(other)
            out_win.destroy()
            over_or_fin_check(ball, run, facing, other, over, current_bowler, patnership, out)

        button = Button(out_win, text="OK", command=lambda: ok5(ball, run, facing, other, over, current_bowler, patnership, out), bg = "SpringGreen3")
        button.grid(row=2, column=1)
        hover(button, "palegreen", "SpringGreen3")

#-----/RUN FUNCATION/-----

def run_function(balls, run, facing, other, over, current_bowler, patnership, out):
    global run_win
    run_win = Toplevel(master)
    run_win.configure(bg = "DarkSlateGrey")
    play_win.withdraw()
    sizing(run_win)
    title = Label(run_win, text = "Enter amount of runs scored", bg = "DarkSlateGrey").grid(row = 0, column = 1)
    run_entry = Entry(run_win, bg = "DimGrey")
    run_entry.grid(row = 1, column = 1)

    def run_submit(balls, run, facing, other, over, current_bowler, patnership, out):
        new_run = int(run_entry.get())
        with open("test.txt", "a") as f:
            f.write(f"{facing} and {other} scored a total of {new_run} runs\n")
        run = new_run + run
        patnership = patnership + new_run
        print(run)
        print(new_run)
        if new_run % 2 != 0:
            other, facing = facing, other
        else:
            print("Same")
        over_or_fin_check(balls, run, facing, other, over, current_bowler, patnership, out)

    submit_runs = Button(run_win, text = "Submit", command = lambda:[run_submit(balls, run, facing, other, over, current_bowler, patnership, out), clear_win()], bg = "SpringGreen3")
    submit_runs.grid(row = 2, column = 1)
    hover(submit_runs, "PaleGreen", "SpringGreen3")

#-----/CLEAR FUNCATION/-----

def clear_win():
    run_win.destroy()

#-----/OVER CALCULATION/-----

def over_or_fin_check(ball, run, facing, other, over, current_bowler, patnership, out):
    print("Out change function")
    if ball % 6 == 0:
        updated_over = over + 1
        change_bowler(current_bowler, ball, run, facing, other, updated_over, patnership, out)
    else:
        innings_over_check(ball, run, facing, other, over, current_bowler, patnership, out)

#-----/CHANGING BOWLER FUNCTION/-----

def change_bowler(old_bowler, balls, run, facing, other, over, patnership, out):
    nb_win = Toplevel(master)
    run_win.withdraw()
    nb_win.configure(bg = "DarkSlateGrey")
    sizing(nb_win)
    variable = StringVar(nb_win)
    variable.set(fielding_team[0])
    title = Label(nb_win, text="Please choose the new bowler", bg = "DarkSlateGrey").grid(row=0, column=1)

    w = OptionMenu(nb_win, variable, *fielding_team)
    w.grid(row=1, column=1)

    def submit_func(old_bowler, balls, run, facing, other, over, patnership, out):
        new_bowler = variable.get()
        bowler_moving_in = new_bowler
        bowler_moving_out = old_bowler
        current_bowler = new_bowler
        fielding_team.append(bowler_moving_out)
        for players in fielding_team:
            if players == current_bowler:
                fielding_team.remove(current_bowler)
        nb_win.destroy()
        with open("test.txt", "a") as f:
            f.write(f"Bowler has been changed to {current_bowler}\n")
        innings_over_check(balls, run, facing, other, over, current_bowler, patnership, out)


    button = Button(nb_win, text="Submit", command= lambda: submit_func(old_bowler, balls, run, facing, other, over, patnership, out), bg = "SpringGreen3")
    button.grid(row=2, column=1)
    hover(button, "palegreen", "SpringGreen3")

#-----/CHECK FOR CHANGE IN INNINGS OR END OF GAME/-----

def innings_over_check(ball, run, facing, other, over, current_bowler, patnership, out):
    global innings
    if over == over_amount or innings == 3:
        innings = innings + 1
        main_win.destroy()
        change_sides(ball, run, facing, other, over, current_bowler, patnership, out)
    else:
        main_win.destroy()
        with open("test.txt", "a") as f:
            f.write(f"End of Play\n")
            f.write(f"------------------------\n")
        main_play(run, facing, other, over, ball, current_bowler, patnership, out)

#-----/CHANGING SIDES/-----

def change_sides(balls, run, facing, other, over, current_bowler, patnership, out):
    global batting_team_copy
    global first_team
    global team_not
    global team_facing
    global innings
    global fielding_team
    global batting_team
    global batsmen
    global team_1_runs_final
    global team_1_out_final
    global team_1_overs_final
    global team_2_runs_final
    global team_2_out_final
    global team_2_overs_final



    fielding_team.append(current_bowler)


    ###FIRST TEAM SAVE SCORE
    if first_team == "t1":
        print("Sides Change")
        team_1_runs_final = run
        team_1_out_final = out
        team_1_overs_final = over
        first_team = "t2"
        team_facing = team_2
        team_not = team_1
    elif first_team == "t2":
        print("Sides Change")
        team_2_runs_final = run
        team_2_out_final = out
        team_2_overs_final = over
        first_team = "t1"
        team_facing = team_1
        team_not = team_2

    ###MOVING CURRENT BATTING TEAM INTO TEMP LIST BEFORE MOVING TO MAIN LIST OF FIELDING TEAM
    new_fielding_team = [None] * len(batting_team_copy)
    for i in range(0, len(batting_team_copy)):
        new_fielding_team[i] = batting_team_copy[i]

    ###MOVING CURRENT FIELDING TEAM INTO TEMP LIST BEFORE MOVING TO MAIN LIST OF BATTING TEAM
    new_batting_team = [None] * len(fielding_team)
    for i in range(0, len(fielding_team)):
        new_batting_team[i] = fielding_team[i]

    ###MOVING NEW FIELDING TEAM FROM LIST "NEW FIELDING TEAM"
    fielding_team = [None] * len(new_fielding_team)
    for i in range(0, len(new_fielding_team)):
        fielding_team[i] = new_fielding_team[i]

    ###MOVING NEW BATTING TEAM FROM LIST "NEW BATTING TEAM"
    batting_team = [None] * len(new_batting_team)
    for i in range(0, len(new_batting_team)):
        batting_team[i] = new_batting_team[i]


    ###RESTING VALUES



    if innings == 2:
        print("New Innings")
        over = 0
        runs = 0
        out = 0
        ball = 0
        patnership = 0
        batsmen = []
        with open("test.txt", "a") as f:
            f.write(f" \n")
            f.write("Innings Change\n")
            f.write(f" \n")
        batsmen_1(balls, run, facing, other, over, current_bowler, patnership, out)
        main_win.destroy()
        ctr_right.destroy()
        ctr_left.destroy()
        top_frame.destroy()
        center.destroy()
        ctr_mid.destroy()
        btm_frame.destroy()
        btm_frame2.destroy()
        out_win.destroy()
        play_win.destroy()
    elif innings == 3:
        end_game()

#-----/DISPLAYING RESULTS/-----

def end_game():
    end_win = Toplevel(master)
    play_win.withdraw()
    main_win.withdraw()
    sizing(end_win)


    #DEFINING SPECIFIC WINDOWS
    top_frame_end = Frame(end_win, bg='DarkSlateGrey', width=450, height=50, pady=3)
    center_end = Frame(end_win, bg='gray2', width=50, height=40, padx=3, pady=3)
    btm_frame_end = Frame(end_win, bg='white', width=50, height=40, pady=3)

    end_win.grid_rowconfigure(1, weight=1)
    end_win.grid_columnconfigure(0, weight=1)

    top_frame_end.grid(row=0, sticky="ew")
    center_end.grid(row=1, sticky="nsew")
    btm_frame_end.grid(row=3, sticky="ew")

    ws = Label(top_frame_end, text = " ").grid(row = 0, column = 1)
    T1 = Label(top_frame_end, text = "Team: " + team_1).grid(row = 1, column = 1)
    T1_score = Label(top_frame_end, text = f"Score: {team_1_out_final}/{team_1_runs_final}").grid(row = 1, column = 2)
    T1_over = Label(top_frame_end, text = f"Overs: {team_1_overs_final}").grid(row = 1, column = 3)
    ws2 = Label(top_frame_end, text = " ").grid(row = 2, column = 1)

    ws3 = Label(center_end, text=" ").grid(row=0, column=1)
    T2 = Label(center_end, text="Team: " + team_2).grid(row=1, column=1)
    T2_score = Label(center_end, text=f"Score: {team_2_out_final}/{team_2_runs_final}").grid(row=1, column=2)
    T2_over = Label(center_end, text=f"Overs: {team_2_overs_final}").grid(row=1, column=3)
    ws4 = Label(center_end, text=" ").grid(row=2, column=1)


mainloop()