import tkinter as tk
from tkinter import ttk
import sqlite3
import re
import random
from ttkthemes import ThemedTk


#windows
root = tk.Tk()
#root = ThemedTk(theme="blue")
root.geometry("1500x800")
root.title("ANIME NIGHT!!!")
style = ttk.Style(root)
#style.theme_use("arc")
#print(style.theme_names())
#print(style.theme_use())
    
frame2 = ttk.Frame(root)
frame2.pack(fill=tk.BOTH, expand=1)
canvas2 = tk.Canvas(frame2)
scrollbar2 = ttk.Scrollbar(frame2, orient="vertical", command=canvas2.yview)
canvas2.configure(yscrollcommand=scrollbar2.set)
content_frame2 = ttk.Frame(canvas2)
content_frame2.bind("<Configure>", lambda e: canvas2.configure(scrollregion=canvas2.bbox("all")))
canvas2.create_window((0, 0), window=content_frame2, anchor="nw")
canvas2.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
scrollbar2.pack(side=tk.RIGHT, fill=tk.Y)
listBoxFrame = tk.Frame(content_frame2)
buttonFrame = tk.Frame(content_frame2)
entryFrame = tk.Frame(content_frame2)
entryFrame.pack()
listBoxFrame.pack()
buttonFrame.pack()



#global variables
btns = [] #array for all buttons
btnsEntry = []
my_entry = []
selLb = []
columns = [] #array for one row
myColumn = 1 #so we can change what we filter for later (if we want to search for something other than genre — although that's a problem for later)
number_of_lbs = 0
selection = []
myLBs = []

#functions
# new window functions
def updateAnime(btnValue):
    number=0
    con = sqlite3.connect("animeList.db")
    cur = con.cursor()
    number = re.findall(r'\d+', btnValue)
    number = int(number[0])
    entryValue = number * 5
    number = number + 3
    number = str(number)
    update_statement = "UPDATE anime SET genre=?, episode=?, date=?, rating=? WHERE oid=?"
    cur.execute(update_statement, (my_entry[entryValue+1].get(), my_entry[entryValue+2].get(), my_entry[entryValue+3].get(), my_entry[entryValue+4].get(), number,))
    con.commit()
    cur.execute("SELECT * FROM anime WHERE oid=?", (number,))
    yeet=cur.fetchall()
    print(yeet)
    

def open_new_window():
    global new_window
    global my_entry
    global btnsEntry
    number_of_values = 0
    myRow = 0
    myColumn=0
    new_window = tk.Toplevel(root)  # Create a new window
    new_window.title("let's update")
    new_window.geometry("1500x800")

    #new Window scrollbar
    frame = ttk.Frame(new_window)
    frame.pack(fill=tk.BOTH, expand=1)
    canvas = tk.Canvas(frame)
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    content_frame = ttk.Frame(canvas)
    content_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=content_frame, anchor="nw")
    canvas.pack()
    scrollbar.pack()
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    con = sqlite3.connect("animeList.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM anime")
    schema = [column[0] for column in cur.description]
    for i in range(len(schema)-1):
        tk.Label(content_frame, text=schema[i]).grid(row=0, column=number_of_values)
        number_of_values +=1
    number_of_values = 0
    cur.execute("SELECT * FROM anime")
    animes = cur.fetchall()
    cur.execute("UPDATE anime SET id=NULL")
    con.commit()
    
    for i in range(len(animes)):
        column = animes[i]
        for b in range(len(column)-1):
            var = tk.StringVar(value=f"{column[b]}")
            my_entry.append(tk.Entry(content_frame, textvariable=var, width=20))
            my_entry[number_of_values].grid(row=myRow+1, column=myColumn)
            myColumn+=1
            number_of_values+=1
        myColumn += 1
        btnsEntry.append(tk.Button(content_frame, text=f"{myRow} Update", command=lambda c=myRow: updateAnime(btnsEntry[c].cget("text"))))
        btnsEntry[myRow].grid(row=myRow+1, column=myColumn)
        myRow+=1
        myColumn = 0
    con.close()

def makeListBoxes():
    global number_of_lbs
    tags = []
    con = sqlite3.connect("animeList.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM anime")
    schema = [column[0] for column in cur.description]
    for i in range(len(schema)):
        if schema[i] != "title" and schema[i] != "id":
            hereLabel=tk.Label(listBoxFrame, text=str(schema[i]))
            hereLabel.config(font=("kindergarten", 44))
            hereLabel.grid(column=number_of_lbs + 1, row=0)
            myLBs.append(tk.Listbox(listBoxFrame, width=13, height=5, selectmode=tk.MULTIPLE, exportselection=0))
            myLBs[number_of_lbs].config(font=("kindergarten", 44))
            myLBs[number_of_lbs].grid(column=number_of_lbs + 1, row=1, padx=5, pady=5)
            number_of_lbs += 1
        else:
            print("")
    cur.execute("SELECT * FROM anime")
    animes = cur.fetchall() #every row
    for i in range(len(animes)):
        columns = animes[i]
        myCounter = 0
        tagsInTags = []
        for g in range(len(columns)):
            if columns[g] != None and schema[g] != "title" and schema[g] != "id":
                myLBs[myCounter].insert(tk.END, columns[g])
                myCounter += 1
            else:
                print(" ")
    lbs = []
    for t in range(number_of_lbs):
        lbs.clear()
        me = myLBs[t].get(0, tk.END)
        myLBs[t].delete(0, tk.END)
        for g in range(len(me)):
            lbs.append(me[g])
        lbs = list(dict.fromkeys(lbs))
        for g in range(len(lbs)):
            myLBs[t].insert(tk.END, lbs[g])
            #print(lbs[g])
        #print(lbs)

def createButtons2(): #listbox one
    #clearing everything and resetting
    lbCounter = 0
    makeBtn = False
    global selLb
    selection.clear()
    for i in range(len(btns)):
        btns[i].destroy() 
    btns.clear()
    number_of_btns = -1
    row_number = 0
    column_number = 0
    con = sqlite3.connect("animeList.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM anime")
    animes = cur.fetchall()
    animeList=animes
    print(animeList)
    cur.execute("UPDATE anime SET id=NULL")
    con.commit()
    #getting variables
    global number_of_lbs
    for t in range(number_of_lbs):
        selected_indices = myLBs[t].curselection() #gets number/index of what's selected
        print(selected_indices)
        if selected_indices != None:
            for i in selected_indices:
                selection.insert(i, myLBs[t].get(i))
                print(selection)
                selLb.append(lbCounter)
        lbCounter += 1
    print(selLb)
        
    #actually searching
    random.shuffle(animes)
    print(selection)
    for g in range(len(selection)):
        for i in range(len(animes)):
            columns = animes[i]
            for f in range(len(selLb)):
                myColumn = selLb[f] + 1
                #print(selection[g])
                #print(columns[myColumn])
                if selection[g] != None and selection[g] == columns[myColumn]:
                    makeBtn = True
                    print("true")
                    
                else:
                    makeBtn = False
                    print("false")
            if makeBtn == True:
                number_of_btns += 1
                cur.execute("UPDATE anime SET id=? WHERE title=?", (number_of_btns, columns[0],))
                con.commit()
                
                btns.append(tk.Button(buttonFrame, width="25", text=str(number_of_btns + 1) + " " + columns[1], command=lambda c=number_of_btns: changeText2(btns[c].cget("text"))))
                if column_number > 1:
                    row_number += 1
                    column_number = 0
                btns[number_of_btns].config(font=("kindergarten", 44))
                btns[number_of_btns].grid(row=row_number, column=column_number)
                column_number += 1    
    cur.close()  

def changeText2(myText):
    numbers = re.findall(r'\d+', myText)
    #print(numbers)
    #print(myText)
    myID = int(numbers[0])
    myBtn = btns[myID - 1]
    myID = str(myID - 1)
    con = sqlite3.connect("animeList.db")
    cur = con.cursor()
    cur.execute("SELECT title FROM anime WHERE id=?", (myID,)) #find right anime
    myRow = cur.fetchall() # grab it
    myTitle = str(myRow) #to str
    #print("myTitle: " + myTitle)
    myTitle = myTitle[3:-4] #slice out parentheses and stuff to give just the title
    #print("myTitle: " + myTitle)
    myTitle = f"{int(myID) + 1} {myTitle}"
    #print("myTitle: " + myTitle)
    if myText != myTitle:
        myBtn['text'] = myTitle
        con.close()
    else:
        con = sqlite3.connect("animeList.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM anime")
        animes = cur.fetchall()
        myID = int(myID)
        columns = animes[myID]
        myID = str(myID)
        #print("myID: " + myID)
        cur.execute("SELECT genre FROM anime WHERE id = ?", (myID,))
        textHere = cur.fetchall()
        textHere = str(textHere)
        textHere = textHere[3:-4]
        myBtn['text'] = f"{int(myID) + 1} {textHere}" #grab number then column above
        con.close()

#function to add new row/anime
def submit():
    con = sqlite3.connect("animeList.db")
    cur = con.cursor()
    cur.execute("INSERT INTO anime(title, genre) VALUES (?, ?)",(anime_title.get(),anime_genre.get()))
    con.commit()
    con.close()
    anime_title.delete(0, tk.END)
    anime_genre.delete(0, tk.END)

makeListBoxes()
#swin.bind("<MouseWheel>", scroll)

#filtering button
print_anime = tk.Button(listBoxFrame, text='Show Me the Good Stuff!', height="5", command = createButtons2)
print_anime.grid(row=1, column=0)

#add new anime ENTRY BOXES
#schema: title, genre, episode, date, rating, id
anime_title = tk.Entry(entryFrame, width=20)
anime_title.grid(row=2, column=2)
anime_genre = tk.Entry(entryFrame, width=20)
anime_genre.grid(row=3, column=2)

#add new anime ENTRY LABELS
explain_label = tk.Label(entryFrame, text="Use this to add new anime")
explain_label.grid(row = 1, column = 2)
title_label = tk.Label(entryFrame, text='Title: ')
title_label.grid(row=2, column=1)
genre_label = tk.Label(entryFrame, text='Genre: ')
genre_label.grid(row=3, column=1)


#add new anime BUTTON
submit_btn = tk.Button(entryFrame, width="25", text="Add New Anime to Database", command=submit)
submit_btn.grid(column=2)

#update anime button
update_anime_btn = tk.Button(entryFrame, text="Click here to update anime in new window", command=open_new_window)
update_anime_btn.grid(row=0, column=1, columnspan=2)


#schema: title, genre, episode, date, rating, id


root.mainloop()




