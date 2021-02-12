from tkinter import *
from tkinter import messagebox


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



def error_popup_teams():
    global response
    response = messagebox.showerror("Error Popup", "Duplicate player found, please re-enter names")
    return response







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
                    t1_confirm.geometry("200x200")
                    player_count = 1
                    for i in range(len(team_1_array)):
                        exec('Label%d=Label(t1_confirm,text="%s")\nLabel%d.pack()' % (i, "Player " + str(player_count) + " : " + team_1_array[i], i))
                        player_count = player_count + 1
                    confirm_button = Button(t1_confirm, text = "Confirm Team 1", command = input_stub_2).pack()




##TEAM 2 INPUT

player_num2 = 0
display_num2 = 1
##TEAM 1 Input
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
        title = Label(t2_input, text = "Team 2 Input").grid(row = 0, column = 1)
        request = Label(t2_input, text = "Please enter player " + str(display_num2) + " name").grid(row = 1, column = 1)
        name_entry = Entry(t2_input)
        name_entry.grid(row = 2, column = 1)
        display_num2 = display_num2 + 1
        valid_button = Button(t2_input, text = "Submit", command = lambda: t2_validation(team_2_array)).grid(row = 4, column = 1)
def t2_validation(current_team):
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
                    t2_confirm.geometry("200x200")
                    player_count = 1
                    for i in range(len(team_2_array)):
                        exec('Label%d=Label(t2_confirm,text="%s")\nLabel%d.pack()' % (i, "Player " + str(player_count) + " : " + team_2_array[i], i))
                        player_count = player_count + 1
                    confirm_button = Button(t2_confirm, text = "Confirm Team 2", command = full_confirm_func).pack()




def full_confirm_func():
    global full_confirm
    global team_1_array
    global team_2_array
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
    submit = Button(full_confirm, text = "Submit", command = choosing_sides_func).pack()
    back = Button(full_confirm, text="Redo Name input", command= lambda: [input_stub(), reset_player_num(player_num, display_num, player_num2, display_num2)]).pack()

def reset_player_num(player1, display1, display2, player2):
    player1 = 0
    display1 = 1
    player2 = 0
    display2 = 1


def choosing_sides_func():
    global choosing_sides
    choosing_sides = Toplevel(master)
    full_confirm.withdraw()
    title = Label(choosing_sides, text = "Which team is batting first?").grid(row = 0, column = 1)
    t1_batting_button = Button(choosing_sides, text = team_1, command = lambda: t1_batting(team_1_array, team_2_array)).grid(row = 1,column = 1)
    t2_batting_button = Button(choosing_sides, text=team_2, command= lambda: t1_batting(team_2_array, team_1_array)).grid(row=2, column=1)

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



def list_teams_stub(bt, ft):
    global list_teams
    player_count_3 = 1
    player_count_4 = 1
    list_teams = Toplevel(master)
    choosing_sides.withdraw()
    batting = Label(list_teams, text = "Batting Team:").pack()
    for i in range(len(bt)):
        exec('Label%d=Label(list_teams,text="%s")\nLabel%d.pack()' % (i, "Player " + str(player_count_3) + " : " + bt[i], i))
        player_count_3 = player_count_3 + 1
    line = Label(list_teams, text="------------").pack()
    fielding = Label(list_teams, text="Fielding Team:").pack()
    for i in range(len(ft)):
        exec('Label%d=Label(list_teams,text="%s")\nLabel%d.pack()' % (i, "Player " + str(player_count_4) + " : " + ft[i], i))
        player_count_4 = player_count_4 + 1
    next = Button(list_teams, text = "Confirm", command = match_type_stub()).pack()




def match_type_stub():
    global match_type
    match_type = Toplevel(master)
    list_teams.withdraw()
    title_1 = Label(match_type, text = "What type of game").grid(row = 0, column = 1)
    title_2 = Label(match_type, text = "do you want to play?").grid(row = 1, column =1)
    T20 = Button(match_type, text = "T20", command = lambda: match_type_set(20)).grid(row = 2, column = 1)
    One_day = Button(match_type, text="One Day", command = lambda: match_type_set(50)).grid(row=3, column=1)
    Custom = Button(match_type, text="Custom", command= custom_over).grid(row=4, column=1)


def match_type_set(type):
    global over_amount
    if type == 20:
        over_amount = 20
    elif type == 50:
        over_amount = 50
    batsmen_1()
    return over_amount


co_flag = False
def custom_over():
    global cust_over
    global amount
    global co_flag
    co_flag = True
    cust_over = Toplevel(master)
    match_type.withdraw()
    title = Label(cust_over, text = "Input custom over amount").grid(row = 0, column = 1)
    title = Label(cust_over, text="(Between 10-50)").grid(row=1, column=1)
    amount = Entry(cust_over)
    amount.grid(row = 2, column = 1)
    submit = Button(cust_over, text = "Submit", command = lambda: [batsmen_1(), clear_win()]).grid(row = 3, column = 1)


def clear_win():
    cust_over.withdraw()

def batsmen_1():
    global batsmen_win
    global batsmen
    global over_amount
    if co_flag == True:
        over_amount = amount.get()
        over_amount = int(over_amount)
        if over_amount < 10 or over_amount > 50:
            error = Label(cust_over, text = "Error, out of range").grid(row = 4, column = 1)
        elif co_flag == False:
            cust_over.withdraw()
    batsmen_win = Toplevel(master)
    match_type.withdraw()
    itle = Label(batsmen_win, text="Choose the first batsmen").grid(row=0, column=1)
    variable = StringVar(batsmen_win)
    variable.set(batting_team[0])  # default value

    w = OptionMenu(batsmen_win, variable, *batting_team)
    w.grid(row = 1, column = 1)

    def ok():
        global batsmen
        batsmen.append(variable.get())
        for players in batting_team:
            if players == batsmen[0]:
                batting_team.remove(batsmen[0])
        batsmen_2()

    button = Button(batsmen_win, text="OK", command=ok).grid(row = 2, column = 1)


def batsmen_2():
    global batsmen_win_2
    global batsmen
    global other_batsmen
    batsmen_win_2 = Toplevel(master)
    batsmen_win.withdraw()
    variable = StringVar(batsmen_win_2)
    variable.set(batting_team[0])  # default value
    title = Label(batsmen_win_2, text = "Choose the second batsmen").grid(row =0, column = 1)


    w = OptionMenu(batsmen_win_2, variable, *batting_team)
    w.grid(row = 1, column = 1)

    def ok1():
        global batsmen
        batsmen.append(variable.get())
        for players in batting_team:
            if players == batsmen[1]:
                batting_team.remove(batsmen[1])
        bowler()

    button = Button(batsmen_win_2, text="OK", command=ok1).grid(row = 2, column = 1)

def bowler():
    global bowler_win
    global batsmen
    global current_bowler
    bowler_win = Toplevel(master)
    batsmen_win_2.withdraw()
    variable = StringVar(bowler_win)
    variable.set(fielding_team[0])
    title = Label(bowler_win, text = "Please choose the bowler").grid(row = 0, column = 1)

    w = OptionMenu(bowler_win, variable, *fielding_team)
    w.grid(row = 1, column = 1)

    def ok2():
        global current_bowler
        current_bowler = variable.get()
        for players in batting_team:
            if players == current_bowler:
                fielding_team.remove(current_bowler)
        setting_batsmen()

    button = Button(bowler_win, text="OK", command=ok2).grid(row = 2, column = 1)


def setting_batsmen():
    global facing_player_in_list
    global facing
    global other
    facing = batsmen[0]
    other = batsmen[1]
    facing_player_in_list = 1
    main_play()


def main_play():
    global main_win
    global facing
    global other
    print(batsmen)
    main_win = Toplevel(master)
    bowler_win.withdraw()
    main_win.geometry("65x250")
    title = Label(main_win, text = "Current Game").grid(row = 0, column = 1)
    score = Label(main_win, text = "Current Score:").grid(row = 2, column = 1)
    line = Label(main_win, text = "--------------").grid(row = 1, column = 1)
    score = Label(main_win, text = str(runs) + "/" + str(out)).grid(row = 3, column = 1)
    line = Label(main_win, text="--------------").grid(row=4, column=1)
    cur_bat = Label(main_win, text = "Facing Batsmen: " + facing).grid(row = 5, column = 1)
    other_bat = Label(main_win, text = "Other Batsmen: " + other).grid(row = 6, column = 1)
    current_patner = Label(main_win, text = "Patnership: " + str(partnership_runs)).grid(row = 7, column = 1)
    line = Label(main_win, text="--------------").grid(row=8, column=1)
    bowler = Label(main_win, text = "Bowler: " + current_bowler).grid(row = 9, column = 1)
    line = Label(main_win, text="--------------").grid(row=10, column=1)
    button_func = Button(main_win, text = "Play", command = play_func).grid(row = 11, column = 1)

def play_func():
    global ball
    global play_win
    play_win = Toplevel(master)
    ball = ball + 1
    title = Label(play_win, text = "Select Outcome of play").grid(row = 0, column = 1)
    run_button = Button(play_win, text = "Runs", command = run_function).grid(row = 1, column = 1)
    run_button = Button(play_win, text="Out", command= out_function).grid(row=2, column=1)

def out_function():
    print("Out function")
    over_or_fin_check()



    






def run_function():
    global run_win
    global run_entry
    run_win = Toplevel(master)
    play_win.withdraw()
    title = Label(run_win, text = "Enter amount of runs scored").grid(row = 0, column = 1)
    run_entry = Entry(run_win)
    run_entry.grid(row = 1, column = 1)
    submit_runs = Button(run_win, text = "Submit", command = lambda:[run_submit(), clear_win()]).grid(row = 2, column = 1)

def clear_win():
    run_win.destroy()

def run_submit():
    global new_run
    global runs
    new_run = run_entry.get()
    new_run = int(new_run)
    runs = new_run + runs
    change_facing_players()

def change_facing_players():
    global facing_player_in_list
    global facing
    global other
    if new_run % 2 != 0:
        if facing_player_in_list == 1:
            facing = batsmen[0]
            other = batsmen[1]
            facing_player_in_list = 2
        if facing_player_in_list == 2:
            facing = batsmen[1]
            other = batsmen[0]
            facing_player_in_list = 1
    if new_run % 2 == 0:
        print("Facing is same")
    over_or_fin_check()


def over_or_fin_check():
    if ball % 6 == 0:
        over = over + 1
        change_bowler(current_bowler)
    else:
        innings_over_check()

def change_bowler(old_bowler):
    nb_win = Toplevel(master)
    run_win.withdraw()
    variable = StringVar(nb_win)
    variable.set(fielding_team[0])
    title = Label(nb_win, text="Please choose the new bowler").grid(row=0, column=1)

    w = OptionMenu(nb_win, variable, *fielding_team)
    w.grid(row=1, column=1)

    def submit_func():
        new_bowler = variable.get()
        bowler_moving_in = new_bowler
        bowler_moving_out = old_bowler
        current_bowler = new_bowler
        fielding_team.append(bowler_moving_out)
        innings_over_check()


    button = Button(bowler_win, text="Submit", command=submit_func).grid(row=2, column=1)



def innings_over_check():
    if over == over_amount:
        innings = innings + 1
        main_win.destroy()
        change_sides()
    else:
        main_win.destroy()
        main_play()


























mainloop()