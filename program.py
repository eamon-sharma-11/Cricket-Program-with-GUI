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


def sizing(window):
    window.update()
    w = window.winfo_width()
    h = window.winfo_height()
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    window.geometry('+%d+%d' % (x, y))





def help_menu():
    top = Toplevel(master)
    sizing(top)
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
    main_win.withdraw()
    sizing(top_1)
    top_1.title("Hows That?")
    def start_team2():
        global team_1
        global t2_entry
        global top_2
        team_1 = t1_entry.get()
        top_2 = Toplevel(master)
        top_1.withdraw()
        sizing(top_2)
        top_2.title("Hows That?")
        team2_name = Label(top_2, text="Enter Team 2's team name: ").grid(row=0, column=1)
        previous = "Team 1: " + team_1
        previouslb = Label(top_2, text = previous).grid(row=2, column=1)
        t2_entry = Entry(top_2, width=20)
        t2_entry.grid(row=1, column=1)
        submit_button = Button(top_2, text="SUBMIT", command=save_team2_names).grid(row=3, column=1)

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
        sizing(confirm_screen)
        t1_name = Label(confirm_screen, text = "Team 1: " + team_1).grid(row = 1, column = 1)
        t2_name = Label(confirm_screen, text="Team 2: " + team_2).grid(row = 1, column = 2)
        confirm_button = Button(confirm_screen, text = "Submit", width = 10, command = team_name_1).grid(row = 4, column = 1)
        redo = Button(confirm_screen, text="Redo", width=10, command= lambda: [start_team1(), clear()]).grid(row=4, column=2)

def clear():
    confirm_screen.withdraw()


sizing(master)
master.title("How's That")
label_ = Label(master, text = "Hows that is").pack()
label_2 = Label(master, text = "now loading").pack()






#SETTING UP MAIN SCREEN
def main():
    global main_win
    master.withdraw()
    main_win = Toplevel(master)
    sizing(main_win)
    welcome_label = Label(main_win, text = 'Welcome to "Hows That?"')
    white_space_welcome = Label(main_win, text = " ")
    white_space_welcome2 = Label(main_win, text = " ")
    white_space_welcome3 = Label(main_win, text = " ")

    help_menu_button = Button(main_win, text = "HELP", command = help_menu)
    start_button = Button(main_win, text = "START", command = start_team1)
    exit_button = Button(main_win, text = "EXIT", command = sys.exit)


    welcome_label.grid(row = 0, column = 1)
    white_space_welcome.grid(row = 1, column = 1)
    white_space_welcome2.grid(row = 2, column = 1)
    white_space_welcome3.grid(row = 3, column = 1)
    help_menu_button.grid(row = 4, column = 0)
    start_button.grid(row = 4, column = 1)
    exit_button.grid(row = 4, column = 2)

master.after(3000, main())
####AFTER CONFIRMING TEAMS

def team_name_1():
    global team_name_input
    global team_amount_test
    team_name_input = Toplevel(master)
    confirm_screen.withdraw()
    sizing(team_name_input)
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
        sizing(team_name_input2)
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
        sizing(final_confirm)
        con_title = Label(final_confirm, text = "Please ensure that all information is correct").grid(row = 0, column = 1)
        t1_con = Label(final_confirm, text = str(team_1) + ": " + str(t1_amount) + " players").grid(row = 1, column = 1)
        t2_con = Label(final_confirm, text = str(team_2) + ": " + str(t2_amount) + " players").grid(row = 2, column = 1)
        button_con = Button(final_confirm, text = "Confirm", command = input_stub).grid(row = 3, column = 1)
        button_redo = Button(final_confirm, text="Redo", command = save_team2_names).grid(row=4, column=1)



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
        sizing(t1_input)
        title = Label(t1_input, text = team_1 + " Input").grid(row = 0, column = 1)
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
                    sizing(t1_confirm)
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
        sizing(t2_input)
        title = Label(t2_input, text = team_2 + " Input").grid(row = 0, column = 1)
        request = Label(t2_input, text = "Please enter player " + str(display_num2) + " name").grid(row = 1, column = 1)
        name_entry = Entry(t2_input)
        name_entry.grid(row = 2, column = 1)
        display_num2 = display_num2 + 1
        valid_button = Button(t2_input, text = "Submit", command = lambda: t2_validation(team_2_array)).grid(row = 4, column = 1)
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
                    sizing(t2_confirm)
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
    sizing(full_confirm)
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
    sizing(choosing_sides)
    title = Label(choosing_sides, text = "Which team is batting first?").grid(row = 0, column = 1)
    t1_batting_button = Button(choosing_sides, text = team_1, command = lambda: [t1_batting(team_1_array, team_2_array), team_set(1)]).grid(row = 1,column = 1)
    t2_batting_button = Button(choosing_sides, text=team_2, command= lambda: [t1_batting(team_2_array, team_1_array), team_set(2)]).grid(row=2, column=1)

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


def list_teams_stub(bt, ft):
    global list_teams
    player_count_3 = 1
    player_count_4 = 1
    list_teams = Toplevel(master)
    choosing_sides.withdraw()
    sizing(list_teams)
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
    sizing(match_type)
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
    sizing(cust_over)
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
    sizing(batsmen_win)
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
    sizing(batsmen_win_2)
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
    sizing(bowler_win)
    variable = StringVar(bowler_win)
    variable.set(fielding_team[0])
    title = Label(bowler_win, text = "Please choose the bowler").grid(row = 0, column = 1)

    w = OptionMenu(bowler_win, variable, *fielding_team)
    w.grid(row = 1, column = 1)

    def ok2():
        global current_bowler
        global fielding_team
        current_bowler = variable.get()
        for players in batting_team:
            if players == current_bowler:
                fielding_team.remove(current_bowler)
        setting_batsmen(current_bowler)

    button = Button(bowler_win, text="OK", command=ok2).grid(row = 2, column = 1)


def setting_batsmen(bol):
    global facing_player_in_list
    global facing
    global other
    facing = batsmen[0]
    other = batsmen[1]
    facing_player_in_list = 1
    main_play(0, facing, other, 0, 0, current_bowler = bol)


def main_play(runs, facing, other, over, ball, current_bowler):
    global main_win
    print(batsmen)
    main_win = Toplevel(master)
    sizing(main_win)
    bowler_win.withdraw()
    #Defining Frame
    top_frame = Frame(main_win, bg='lavender', width=450, height=50, pady=3)
    center = Frame(main_win, bg='gray2', width=50, height=40, padx=3, pady=3)
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

    ctr_left = Frame(center, bg='lavender', width=100, height=145)
    ctr_mid = Frame(center, bg='light green', width=250, height=145, padx=3, pady=3)
    ctr_right = Frame(center, bg='lavender', width=100, height=145, padx=3, pady=3)

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

    score_title = Label(ctr_left, text="Score:", font=10)
    score_title.grid(row=0, column=1, pady=60, padx=20)
    score = Label(ctr_left, text="Runs: " + str(runs), font=10)
    score.grid(row=1, column=1, padx=20)
    out_label = Label(ctr_left, text="Outs: " + str(out), font=10)
    out_label.grid(row=2, column=1, pady=60)

    info_title = Label(ctr_right, text="Info:", font=10)
    info_title.grid(row=0, column=1, pady=60, padx=20)
    ball_amount = Label(ctr_right, text="Balls: " + str(ball), font=10)
    ball_amount.grid(row=1, column=1, padx=20)
    over_label = Label(ctr_right, text="Over: " + str(over), font=10)
    over_label.grid(row=2, column=1, pady=60)

    # Bottom frame button

    move_on = Button(btm_frame, text="Play!", command= lambda: play_func(ball, runs, facing, other, over, current_bowler), height=5, width=30, font=10)
    move_on.grid(column=1, row=1, )
    move_on = Button(btm_frame, text="Exit!", command=sys.exit, height=5, width=30, font=10)
    move_on.grid(column=2, row=1, )

    current_facing = Label(btm_frame2, text="Batting: " + team_facing, font=20)
    other_facing = Label(btm_frame2, text="Bowling: " + team_not, font=20)
    current_facing.grid(row=0, column=1, padx=130, pady=18)
    other_facing.grid(row=0, column=2)




def play_func(balls, run, facing, other, over, current_bowler):
    global play_win
    play_win = Toplevel(master)
    sizing(play_win)
    ball = balls + 1
    title = Label(play_win, text = "Select Outcome of play").grid(row = 0, column = 1)
    run_button = Button(play_win, text = "Runs", command = lambda: run_function(ball, run, facing, other, over, current_bowler)).grid(row = 1, column = 1)
    run_button = Button(play_win, text="Out", command= lambda: out_function(ball, run, facing, other, over, current_bowler)).grid(row=2, column=1)
    return ball

def out_function(ball, run, facing, other, over, current_bowler):
    global partnership_runs
    partnership_runs = 0
    print("Out function")
    if len(batting_team) == 0:
        change_sides()
    else:
        out_win = Toplevel(master)
        play_win.withdraw()
        sizing(out_win)
        out_players.append(facing)
        facing = other
        variable = StringVar(out_win)
        variable.set(batting_team[0])  # default value
        title = Label(out_win, text="Choose the new batsmen").grid(row=0, column=1)

        w = OptionMenu(out_win, variable, *batting_team)
        w.grid(row=1, column=1)

        def ok5(ball, run, facing, other, over, current_bowler):
            other = variable.get()
            for players in batting_team:
                if players == other:
                    batting_team.remove(other)
            out_win.destroy()
            over_or_fin_check(ball, run, facing, other, over, current_bowler)

        button = Button(out_win, text="OK", command=lambda: ok5(ball, run, facing, other, over, current_bowler)).grid(row=2, column=1)


def run_function(balls, run, facing, other, over, current_bowler):
    global run_win
    run_win = Toplevel(master)
    play_win.withdraw()
    sizing(run_win)
    title = Label(run_win, text = "Enter amount of runs scored").grid(row = 0, column = 1)
    run_entry = Entry(run_win)
    run_entry.grid(row = 1, column = 1)
    submit_runs = Button(run_win, text = "Submit", command = lambda:[run_submit(run_entry, balls, run, facing, other, over, current_bowler), clear_win()]).grid(row = 2, column = 1)

def clear_win():
    run_win.destroy()

def run_submit(entry, balls, run, facing, other, over, current_bowler):
    global partnership_runs
    new_run = entry.get()
    new_run = int(new_run)
    runs = new_run + run
    partnership_runs = new_run + partnership_runs
    change_facing_players(balls, runs, facing, other, over, new_run, current_bowler)

def change_facing_players(balls, run, facing, other, over, new_run, current_bowler):
    global facing_player_in_list
    if new_run % 2 != 0:
        if facing_player_in_list == 1:
            facing = batsmen[0]
            other = batsmen[1]
            facing_player_in_list = 2
            return facing
            return other
        if facing_player_in_list == 2:
            facing = batsmen[1]
            other = batsmen[0]
            facing_player_in_list = 1
            return facing
            return other
    if new_run % 2 == 0:
        print("Facing is same")
    over_or_fin_check(balls, run, facing, other, over, current_bowler)


def over_or_fin_check(ball, run, facing, other, over, current_bowler):
    if ball % 6 == 0:
        updated_over = over + 1
        change_bowler(current_bowler, ball, run, facing, other, updated_over)
    else:
        innings_over_check(ball, run, facing, other, over, current_bowler)

def change_bowler(old_bowler, balls, run, facing, other, over):
    nb_win = Toplevel(master)
    run_win.withdraw()
    sizing(nb_win)
    variable = StringVar(nb_win)
    variable.set(fielding_team[0])
    title = Label(nb_win, text="Please choose the new bowler").grid(row=0, column=1)

    w = OptionMenu(nb_win, variable, *fielding_team)
    w.grid(row=1, column=1)

    def submit_func(old_bowler, balls, run, facing, other, over):
        new_bowler = variable.get()
        bowler_moving_in = new_bowler
        bowler_moving_out = old_bowler
        current_bowler = new_bowler
        fielding_team.append(bowler_moving_out)
        nb_win.destroy()
        innings_over_check(balls, run, facing, other, over, current_bowler)


    button = Button(nb_win, text="Submit", command= lambda: submit_func(old_bowler, balls, run, facing, other)).grid(row=2, column=1)



def innings_over_check(ball, run, facing, other, over, current_bowler):
    global innings
    if over == over_amount:
        innings = innings + 1
        main_win.destroy()
        change_sides()
    elif innings == 3:
        end_game()
    else:
        main_win.destroy()
        main_play(run, facing, other, over, ball, current_bowler)


def change_sides():
    global fielding_team
    global batting_team
    global batting_team_copy
    global team_1_runs_final
    global team_1_out_final
    global team_1_overs_final
    global team_2_runs_final
    global team_2_out_final
    global team_2_overs_final
    global first_team
    global team_not
    global team_facing
    global runs
    team_1_runs_final = 0
    team_2_runs_final = 0
    fielding_team.append(current_bowler)

    ###FIRST TEAM SAVE SCORE
    if first_team == "t1":
        team_1_runs_final = runs
        team_1_out_final = out
        team_1_overs_final = over
        first_team = t2
        team_facing = team_2
        team_not = team_1
    if first_team == "t2":
        team_2_runs_final = runs
        team_2_out_final = out
        team_2_overs_final = over
        first_team = t1
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
    runs = 0
    out = 0
    ball = 0
    patnership

    batsmen_1()



def end_game():
    end_win = Toplevel(master)
    main_win.withdraw()
    sizing(end_win)
    print("Endgame")
    sizing(end_win)
    Title = Label(end_win, text = "Results").grid(row = 0, column = 1)
    T1_results = Label(end_win, text = team_1).grid(row = 1, column = 0)
    T1_results2 = Label(end_win, text = "Runs: " + team_1_runs_final).grid(row = 2, column = 0)
    T1_results3 = Label(end_win, text = "Outs: " + team_1_out_final).grid(row = 3, column = 0)
    T1_results3 = Label(end_win, text = "Overs: " + team_1_overs_final).grid(row = 4, column = 0)
    T2_results = Label(end_win, text=team_2).grid(row=1, column=2)
    T2_results2 = Label(end_win, text="Runs: " + team_2_runs_final).grid(row=2, column=2)
    T2_results3 = Label(end_win, text="Outs: " + team_2_out_final).grid(row=3, column=2)
    T2_results3 = Label(end_win, text="Overs: " + team_2_overs_final).grid(row=4, column=2)
    exit = Button(end_win, text = "Exit", command = sys.exit).grid(row = 5, column = 0)
    main = Button(end_win, text = "Menu", command = start_team1()).grid(row = 5, column = 2)























mainloop()