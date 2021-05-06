from tkinter import *
import sqlite3

root = Tk()


#-----/CONNECT TO DATABASE/-----
conn = sqlite3.connect('ladder.db')

#-----/CREATE CURSOR/-----
c = conn.cursor()

#-----/CREATE TABLE/-----

#c.execute("""CREATE TABLE ladder (
		#Team_Name text,
		#Amount_of_Players integer,
		#Games integer,
		#Won integer,
		#Loss integer,
		#Tie integer
		#)""")


#-----/CREATE TEXT BOXES/-----
team_name = Entry(root, width = 30)
team_name.grid(row = 0, column = 1, padx = 20)

Player_Amount = Entry(root, width = 30)
Player_Amount.grid(row = 1, column = 1, padx = 20)

Games = Entry(root, width = 30)
Games.grid(row = 2, column = 1, padx = 20)

Won = Entry(root, width = 30)
Won.grid(row = 3, column = 1, padx = 20)

Loss = Entry(root, width = 30)
Loss.grid(row = 4, column = 1, padx = 20)

Tie = Entry(root, width = 30)
Tie.grid(row = 5, column = 1, padx = 20)

#-----/CREATE TEXT BOX LABELS/-----

team_name_label = Label(root = "Team Name")
team_name_label.grid(row = 0, column = 0)

Player_Amount_label = Label(root = "Team Name")
Player_Amount_label.grid(row = 0, column = 0)

Games_label = Label(root = "Team Name")
Games_label.grid(row = 0, column = 0)

Won_label = Label(root = "Team Name")
Won_label.grid(row = 0, column = 0)

Loss_label = Label(root = "Team Name")
Loss_label.grid(row = 0, column = 0)

Tie_label = Label(root = "Team Name")
Tie_label.grid(row = 0, column = 0)

#-----/COMMIT CHANGES/-----
conn.commit()

#-----/CLOSE DATABASE/-----
conn.close()

root.mainloop()