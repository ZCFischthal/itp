import tkinter as tk
from tkinter import ttk
import sqlite3

#windows
root = tk.Tk()
root.geometry("800x800")
root.title("ANIME NIGHT!!!")

#global variables
btns = [] #array for all buttons
columns = [] #array for one row
myColumn = 1 #so we can change what we filter for later (if we want to search for something other than genre — although that's a problem for later)
myLabel = tk.Label(root, text="") #makes label exist so we can delete it 1st time round
#current_var = tk.StringVar()
#combobox = ttk.Combobox(root, textvariable=current_var)
selection = []
myLBs = []
list_variable = tk.Variable(value=selection)
listbox = tk.Listbox(root, listvariable=list_variable, height = 3, selectmode=tk.MULTIPLE) #makes listbox


#functions
def makeFilters2(): #listbox one
    listbox.grid() #grid it
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
    #listbox = tk.Listbox(root, listvariable=list_variable, height = 3, selectmode=tk.MULTIPLE)
    #listbox.grid() #grid it
    number_of_lbs = 0
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
            tk.Label(root, text=str(schema[i])).grid()
            myLBs.append(tk.Listbox(root, height=3, selectmode=tk.MULTIPLE))
            myLBs[number_of_lbs].grid()
            number_of_lbs += 1
        else:
            print("")
        #listbox.insert(tk.END, str(schema[i]))
    print(myLBs[0])
    cur.execute("SELECT * FROM anime")
    animes = cur.fetchall() #every row
    for i in range(len(animes)):
        columns = animes[i]
        myCounter = 0
        for g in range(number_of_lbs):
            if columns[g] != None and schema[g] != "title" and schema[g] != "id":
                print(columns[g])
                print(myLBs[myCounter])
                myLBs[myCounter].insert(tk.END, columns[g])
                myCounter += 1
            #myLBs[g].insert(tk.END, columns[g])
            else:
                print("empty")
    #print(animes)
    #con.close()
    #actually searching
    
    
def oldPartOfListboxesHiding():
    # another take kill me
    tags = []
    for i in range(len(animes)):
        myTag = str(schema[i])
        print(schema[i])
        cur.execute("SELECT title FROM anime")
        #cur.execute("SELECT ? FROM anime", (myTag,))
        tags = cur.fetchall()
        print(tags)
    #another take
    columns = animes[i]
    for g in range(len(columns)):
        if columns[g] != None and schema[g] != "title" and schema[g] != "id":
            print(columns[g])
            print(myCounter)
            myLBs[0].insert(tk.END, columns[g])
            myCounter += 1
        else:
            print("empty")
    #All stuff for adding into listboxes
    myCounter = 0
    for i in range(len(animes)):
        columns = animes[i] #gets row i
        for q in range(len(columns)-1): #-1 for skipping ID (last one)
            if columns[q] != columns[0] and columns[q] != None: #get column q from row i as long as it's not the title [0] or null [None]
                tags.append(str(columns[q]))
                tags = list(dict.fromkeys(tags))
                print(tags)
                myCounter = len(tags)
                #byColumn.append(tags)
                #tags.clear()
    for g in range(number_of_lbs):
        for i in range(len(tags)):
            myLBs[g].insert(tk.END, tags[i])
    

    
    
def createButtons2(): #listbox one
    #clearing everything and resetting
    selection.clear()
    global myLabel
    myLabel.grid_remove()
    for i in range(len(btns)): 
        btns[i].grid_remove()
    btns.clear()
    number_of_btns = -1
    #getting variables
    selected_indices = listbox.curselection() #gets number/index of what's selected
    for i in selected_indices:
        selection.insert(i, listbox.get(i)) 
    myLabel = tk.Label(root, text=selection)
    myLabel.grid()
    con = sqlite3.connect("animeList.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM anime")
    animes = cur.fetchall()
    cur.execute("UPDATE anime SET id=NULL")
    con.commit()
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
                btns.append(tk.Button(root, height="5", width="25", text=str(number_of_btns + 1) + " " + columns[myColumn], command=lambda c=number_of_btns: changeText(btns[c].cget("text"))))
                #print(number_of_btns)
                btns[number_of_btns].grid()
            else:
                print(" ")
    cur.close()  
        
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

#filtering button
print_anime = tk.Button(root, text='Show Me the Good Stuff!', height="5", command = createButtons2)
print_anime.grid()

#add new anime ENTRY BOXES
#schema: title, genre, episode, date, rating, id
anime_title = tk.Entry(root, width=20)
anime_title.grid()
anime_genre = tk.Entry(root, width=20)
anime_genre.grid()

#add new anime ENTRY LABELS
title_label = tk.Label(root, text='Title: ')
title_label.grid()
genre_label = tk.Label(root, text='Genre: ')
genre_label.grid()


#add new anime BUTTON
submit_btn = tk.Button(root, width="25", text="Add Record to Database", command=submit)
submit_btn.grid()


#schema: title, genre, episode, date, rating, id


root.mainloop()




