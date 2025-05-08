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
leftFrame = tk.Frame(secondFrame)
leftFrame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
rightFrame = tk.Frame(secondFrame)
rightFrame.pack(side=tk.RIGHT, expand=True, fill=tk.Y)


#global variables
btns = [] #array for all buttons
columns = [] #array for one row
myColumn = 1 #so we can change what we filter for later (if we want to search for something other than genre — although that's a problem for later)
myLabel = tk.Label(secondFrame, text="") #makes label exist so we can delete it 1st time round
#current_var = tk.StringVar()
#combobox = ttk.Combobox(secondFrame, textvariable=current_var)
number_of_lbs = 0
selection = []
myLBs = []
list_variable = tk.Variable(value=selection)
listbox = tk.Listbox(secondFrame, listvariable=list_variable, height = 3, selectmode=tk.MULTIPLE) #makes listbox


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
    #list_variable = tk.Variable(value=selection)
    #listbox = tk.Listbox(secondFrame, listvariable=list_variable, height = 3, selectmode=tk.MULTIPLE)
    #listbox.pack() #pack it
    global number_of_lbs
    tags = []
    con = sqlite3.connect("animeList.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM anime")
    schema = [column[0] for column in cur.description]
    for i in range(len(schema)):
        #cur.execute("SELECT ? FROM anime", (schema[i],))
        #currentColumn = cur.fetchall()
        #print(currentColumn)
        if schema[i] != "title" and schema[i] != "id":
            #print(schema[i])
            tk.Label(secondFrame, text=str(schema[i])).pack()
            myLBs.append(tk.Listbox(secondFrame, height=3, selectmode=tk.MULTIPLE))
            myLBs[number_of_lbs].pack()
            number_of_lbs += 1
        else:
            print("")
        #listbox.insert(tk.END, str(schema[i]))
    #print(myLBs[0])
    cur.execute("SELECT * FROM anime")
    animes = cur.fetchall() #every row
    for i in range(len(animes)):
        columns = animes[i]
        myCounter = 0
        tagsInTags = []
        #for g in range(number_of_lbs):
        for g in range(len(columns)):
            if columns[g] != None and schema[g] != "title" and schema[g] != "id":
                #print(columns[g])
                #print(myLBs[myCounter])
                myLBs[myCounter].insert(tk.END, columns[g])
                myCounter += 1
            #myLBs[g].insert(tk.END, columns[g])
            else:
                print("empty")
    lbs = []
    for t in range(number_of_lbs):
        lbs.clear()
        me = myLBs[t].get(0, tk.END)
        myLBs[t].delete(0, tk.END)
        for g in range(len(me)):
            #print(me[g])
            lbs.append(me[g])
        lbs = list(dict.fromkeys(lbs))
        for g in range(len(lbs)):
            myLBs[t].insert(tk.END, lbs[g])
            print(lbs[g])
        print(lbs)
            
            
            #if columns[g] != None and schema[g] != "id":# and schema[g] != "title" and schema[g] != "id":
                #tagsInTags.append([1])
                #tagsInTags[myCounter].append(str(columns[g]))
                #print(tagsInTags[myCounter])
                #print(tagsInTags)
                #tags.append([1])
                #tags[myCounter].append(str(columns[g]))
                #myCounter += 1
        #print(tagsInTags)
        #print(tags[0])
        #myCounter = 0
        #for g in range(len(columns)):
     #   print(tags[myCounter])
            #tags[myCounter] = list(dict.fromkeys(tagsInTags[myCounter]))
            #myCounter += 1
                #print(columns[g])
                #print(myLBs[myCounter])
                #tags[myCounter].append(str(columns[g]))
                #tags.append([1])
                #print(tags[myCounter])
                #myLBs[myCounter].insert(tk.END, columns[g])
                
            #myLBs[g].insert(tk.END, columns[g])
            #else:
                #print("empty")
    #myCounter = 0
    #for g in range(number_of_lbs):
        #if columns[g] != None:# and schema[g] != "title" and schema[g] != "id":
            #print(tags[myCounter])
                #tags[myCounter] = list(dict.fromkeys(tags[myCounter]))
            #myLBs[myCounter].insert(tk.END, tags[myCounter])
            #myCounter += 1
                
                
    #print(animes)
    #con.close()
    #actually searching

def createButtons2(): #listbox one
    #clearing everything and resetting
    selection.clear()
    #global myLabel
    #myLabel.destroy()
    #myLabel.pack_remove()
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
            #myLabel = tk.Label(secondFrame, text=selection)
            #myLabel.pack()
    #actually searching
    for g in range(len(selection)):
        for i in range(len(animes)):
            columns = animes[i]
            #print(animes[i])
            #print("columns[MyColumn]: " + columns[myColumn])
            #print("selection[g]: " + selection[g])
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

def changeText(myText): #changes text of buttons when clicked
    myID = myText[0:1] # slices string to just the number
    print("myID: " + myID)
    myID = int(myID) #str to int
    myBtn = btns[myID - 1] #pulls correct btn from global btn array 
    #print(btns)
    #print(myBtn) #just checking
    myID = str(myID - 1) # int - 1 then back to str
    print("myID: " + myID)
    con = sqlite3.connect("animeList.db")
    cur = con.cursor()
    cur.execute("SELECT title FROM anime WHERE id=?", (myID)) #find right anime
    myRow = cur.fetchall() # grab it
    myTitle = str(myRow) #to str
    myTitle = myTitle[3:-4] #slice out parentheses and stuff to give just the title
    #print(myText[2:])
    #print(myTitle)
    if  myText[2:] != myTitle: #checking if text currently on button (minus the number) is the same as the title we pulled from db
        myBtn['text'] = f"{int(myID) + 1} {myTitle}" #changing text and keeping number at beginning
        #print("myBtn['text']: " + myBtn['text'])
        #print("myText: " + myText)
        #print("myTitle: " + myTitle)
        #print("myID: " + myID)
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
        #cur.execute("SELECT ? FROM anime WHERE id = ?", (columns[myColumn], myID))
        cur.execute("SELECT genre FROM anime WHERE id = ?", (myID))
        textHere = cur.fetchall()
        textHere = str(textHere)
        textHere = textHere[3:-4]
        #print("textHere: " + textHere)
        #print("myID: " + myID)
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
    
#filters
#makeFilters2()
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




