import tkinter as tk
from tkinter import ttk
import sqlite3
import re

#windows
root = tk.Tk()
root.geometry("800x800")
root.title("ANIME NIGHT!!!")
mainFrame = tk.Frame(root)
mainFrame.pack(fill=tk.BOTH, expand=1)
sFrame = tk.Frame(mainFrame)
sFrame.pack(fill=tk.Y, side=tk.RIGHT)
myCanvas = tk.Canvas(mainFrame)
myCanvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
swin = tk.Scrollbar(mainFrame, orient=tk.VERTICAL, command=myCanvas.yview)
swin.pack(side=tk.RIGHT, fill=tk.Y)
myCanvas.configure(yscrollcommand=swin.set)
myCanvas.bind("<Configure>",lambda e: myCanvas.config(scrollregion= myCanvas.bbox(tk.ALL)))
secondFrame = tk.Frame(myCanvas)
myCanvas.create_window((0,0),window=secondFrame, anchor="nw")



#global variables
btns = [] #array for all buttons
columns = [] #array for one row
myColumn = 1 #so we can change what we filter for later (if we want to search for something other than genre — although that's a problem for later)
number_of_lbs = 0
selection = []
myLBs = []


#functions
def scroll(event):
    swin.yview_scroll(int(-1*(event.delta/120)), "units")

def makeFilters2(): #listbox one
    listbox.pack() #pack it
    tags = []
    con = sqlite3.connect("animeList.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM anime")
    animes = cur.fetchall() #every row
    con.close()
    for i in range(len(animes)):
        columns = animes[i] #gets row i
        for q in range(len(columns)-1): #-1 for skipping ID (last one)
            if columns[q] != columns[0] and columns[q] != None: #get column q from row i as long as it's not the title [0] or null [None]
                tags.append(str(columns[q]))
    tags = list(dict.fromkeys(tags))
    for i in range(len(tags)):
        listbox.insert(tk.END, tags[i])
    
def makeListBoxes():
    global number_of_lbs
    tags = []
    con = sqlite3.connect("animeList.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM anime")
    schema = [column[0] for column in cur.description]
    for i in range(len(schema)):
        if schema[i] != "title" and schema[i] != "id":
            tk.Label(secondFrame, text=str(schema[i])).pack()
            myLBs.append(tk.Listbox(secondFrame, height=3, selectmode=tk.MULTIPLE))
            myLBs[number_of_lbs].pack()
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
                print("empty")
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
            print(lbs[g])
        print(lbs)

def createButtons2(): #listbox one
    #clearing everything and resetting
    selection.clear()
    for i in range(len(btns)):
        btns[i].destroy() 
        #btns[i].pack_remove()
    btns.clear()
    number_of_btns = -1
    con = sqlite3.connect("animeList.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM anime")
    animes = cur.fetchall()
    cur.execute("UPDATE anime SET id=NULL")
    con.commit()
    #getting variables
    global number_of_lbs
    for t in range(number_of_lbs):
        selected_indices = myLBs[t].curselection() #gets number/index of what's selected
        for i in selected_indices:
            selection.insert(i, myLBs[t].get(i))
            print(selection)
    #actually searching
    for g in range(len(selection)):
        for i in range(len(animes)):
            columns = animes[i]
            if selection[g] != None and selection[g] == columns[myColumn]:
                number_of_btns += 1
                cur.execute("UPDATE anime SET id=? WHERE title=?", (number_of_btns, columns[0],))
                con.commit()
                btns.append(tk.Button(secondFrame, height="5", width="25", text=str(number_of_btns + 1) + " " + columns[myColumn], command=lambda c=number_of_btns: changeText2(btns[c].cget("text"))))
                #print(number_of_btns)
                btns[number_of_btns].pack()
            else:
                print(" ")
    cur.close()  

def changeText2(myText):
    numbers = re.findall(r'\d+', myText)
    print(numbers)
    print(myText)
    myID = int(numbers[0])
    myBtn = btns[myID - 1]
    myID = str(myID - 1)
    con = sqlite3.connect("animeList.db")
    cur = con.cursor()
    cur.execute("SELECT title FROM anime WHERE id=?", (myID,)) #find right anime
    myRow = cur.fetchall() # grab it
    myTitle = str(myRow) #to str
    print("myTitle: " + myTitle)
    myTitle = myTitle[3:-4] #slice out parentheses and stuff to give just the title
    print("myTitle: " + myTitle)
    myTitle = f"{int(myID) + 1} {myTitle}"
    print("myTitle: " + myTitle)
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
        print("myID: " + myID)
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
swin.bind("<MouseWheel>", scroll)

#filtering button
print_anime = tk.Button(secondFrame, text='Show Me the Good Stuff!', height="5", command = createButtons2)
print_anime.pack()

#add new anime ENTRY BOXES
#schema: title, genre, episode, date, rating, id
anime_title = tk.Entry(secondFrame, width=20)
anime_title.pack()
anime_genre = tk.Entry(secondFrame, width=20)
anime_genre.pack()

#add new anime ENTRY LABELS
title_label = tk.Label(secondFrame, text='Title: ')
title_label.pack()
genre_label = tk.Label(secondFrame, text='Genre: ')
genre_label.pack()


#add new anime BUTTON
submit_btn = tk.Button(secondFrame, width="25", text="Add Record to Database", command=submit)
submit_btn.pack()


#schema: title, genre, episode, date, rating, id


root.mainloop()




