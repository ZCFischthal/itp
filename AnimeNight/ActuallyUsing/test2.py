import tkinter as tk
from tkinter import ttk
import sqlite3

#windows
root = tk.Tk()
root.geometry("800x800")
root.title("ANIME NIGHT!!!")
#root.configure(background="pink")

#global variables
btns = [] #array for all buttons
columns = [] #array for one row
myColumn = 1 #so we can change what we filter for later (if we want to search for something other than genre — although that's a problem for later)
myLabel = tk.Label(root, text="") #makes label exist so we can delete it 1st time round
current_var = tk.StringVar()
combobox = ttk.Combobox(root, textvariable=current_var)
selection = []
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
                #print(columns[q]) #gets column q from row i
                tags.append(str(columns[q]))
    tags = list(dict.fromkeys(tags))
    for i in range(len(tags)):
        listbox.insert(tk.END, tags[i])
        
    
def makeFilters(): #combobox one
    #listbox = tk.Listbox(root, height=3, selectmode=tk.MULTIPLE) #make listbox
    #listbox.grid() #grid it
    #current_var = tk.StringVar() #made global
    #combobox = ttk.Combobox(root, textvariable=current_var) #made global
    combobox['values'] = []
    combobox.grid()
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
                #print(columns[q]) #gets column q from row i
                tags.append(str(columns[q]))
    tags = list(dict.fromkeys(tags))
    for i in range(len(tags)):
        #listbox.insert(tk.END, tags[i])
        new_value = tags[i]
        values = list(combobox['values'])
        combobox['values'] = values + [new_value]
        print(tags[i])
    
def createButtons2(): #listbox one
    #selection = combobox.get()
    #selection = listbox.curselection()
    selection.clear()
    global myLabel
    myLabel.grid_remove()
    for i in range(len(btns)):
        #btns[i].destroy
        btns[i].grid_remove()
    btns.clear()
    number_of_btns = -1
    selected_indices = listbox.curselection() #gets number/index of what's selected
    #selection = [""]
    #selection = selection.append(range(selected_indices))
    #print(selected_indices)
    for i in selected_indices:
        #selection[i] = listbox.get(i)
        selection.insert(i, listbox.get(i))
        #print(listbox.get(i))
        #print(selection[0])
    #selection = ",".join([listbox.get(i) for i in selected_indices]) #gets actual text from what was selected
    myLabel = tk.Label(root, text=selection)
    myLabel.grid()
    #print(selection[1])
    con = sqlite3.connect("animeList.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM anime")
    animes = cur.fetchall()
    for g in range(len(selection)):
        for i in range(len(animes)):
            columns = animes[i]
            print(animes[i])
            print("columns[MyColumn]: " + columns[myColumn])
        #print(animes[i])
            print("selection[g]: " + selection[g])
            if selection[g] != None and selection[g] == columns[myColumn]:
                cur.execute("UPDATE anime SET id=? WHERE title=?", (number_of_btns, columns[0]))
                con.commit()
                number_of_btns += 1
                btns.append(tk.Button(root, height="5", width="25", text=str(number_of_btns + 1) + " " + columns[myColumn], command=lambda c=number_of_btns: changeText(btns[c].cget("text"))))
                print(number_of_btns)
                btns[number_of_btns].grid()
            else:
                print(" ")
        #for g in range(len(selection)):
            #if selection[g] != None and selection[g] == columns[g]:
                #btns.append(tk.Button(root, height="5", width="25", text=str(i + 1) + " " + columns[myColumn], command=lambda c=i: changeText(btns[c].cget("text"))))
                #btns[i].grid()
    cur.close()  
        
        
def createButtons(): #creates the buttons
    #rows = [] #array for rows, made global
    #columns = [] #array for one row, made global
    selection = combobox.get()
    tk.Label(root, text=selection).grid()
    print(selection)
    con = sqlite3.connect("animeList.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM anime")
    animes = cur.fetchall()
    for i in range(len(animes)):
        columns = animes[i]
        #print(columns[0])
        cur.execute("UPDATE anime SET id=? WHERE title=?", (i, columns[0]))
        con.commit()
        btns.append(tk.Button(root, height="5", text=str(i + 1) + " " + columns[myColumn], command=lambda c=i: changeText(btns[c].cget("text"))))
        btns[i].grid()
    cur.close()
 
def changeText(myText): #changes text of buttons when clicked
    myID = myText[0:1] # slices string to just the number
    myID = int(myID) #str to int
    myBtn = btns[myID - 1] #pulls correct btn from global btn array 
    #print(btns)
    print(myBtn) #just checking
    myID = str(myID - 1) # int - 1 then back to str
    con = sqlite3.connect("animeList.db")
    cur = con.cursor()
    cur.execute("SELECT title FROM anime WHERE id=?", (myID)) #find right anime
    myRow = cur.fetchall() # grab it
    myTitle = str(myRow) #to str
    myTitle = myTitle[3:-4] #slice out parentheses and stuff to give just the title
    print(myText[2:])
    print(myTitle)
    if  myText[2:] != myTitle: #checking if text currently on button (minus the number) is the same as the title we pulled from db
        myBtn['text'] = f"{int(myID) + 1} {myTitle}" #changing text and keeping number at beginning
        con.close()
    else:
        con = sqlite3.connect("animeList.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM anime")
        animes = cur.fetchall()
        myID = int(myID)
        columns = animes[myID]
        myID = str(myID)
        cur.execute("SELECT ? FROM anime WHERE id = ?", (columns[myColumn], myID))
        textHere = cur.fetchall()
        print(textHere)
        textHere = str(textHere)
        textHere = textHere[3:-4]
        myBtn['text'] = f"{int(myID) + 1} {textHere}" #grab number then column above
        con.close()

#filters
makeFilters2()

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
submit_btn = tk.Button(root, width="25", text="Add Record to Database")
submit_btn.grid()





#filters not working how I want
#con = sqlite3.connect("animeList.db")
#cur = con.cursor()
#cur.execute("PRAGMA table_info('anime')") #Selects same as .schema
#schema = cur.fetchall()
#cur.execute("SELECT * FROM anime")
#schema = [column[0] for column in cur.description]
#con.close()
#print(schema[1])
#for i in range(len(schema)):
    #print(schema[i])
    #cur.execute("SELECT ? FROM anime", (schema[i],))
    #currentColumn = cur.fetchall()
    #print(currentColumn)
    #print(columns)
    #tk.Label(root, text=str(schema[i])).grid()
    #listbox = tk.Listbox(root, height=3, selectmode=tk.MULTIPLE)
    #listbox.grid()
    #listbox.insert(tk.END, str(schema[i]))

#listbox.insert(tk.END, "thing 1")
#listbox.insert(tk.END, "thing2")



#schema: title, genre, episode, date, rating, id


root.mainloop()

        
    
    
    
    #for anime in animes:
        
        #new_button = Button(root, text=f"{anime[1]}", command=lambda: changeText(btn[c].cget("text")))
        #new_button.grid()



