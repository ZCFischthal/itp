from tkinter import *
import sqlite3

#function to add new row
def submit():
    connection = sqlite3.connect("inventory.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO items(name,quantity,price) VALUES (?,?,?)",(item_name.get(),item_quantity.get(),item_price.get()))
    connection.commit()
    connection.close()
    item_name.delete(0, END)
    item_quantity.delete(0, END)
    item_price.delete(0, END)
  
#function to show everything 
def query():
    connection = sqlite3.connect("inventory.db")
    cursor = connection.cursor()
    cursor.execute("SELECT *, oid FROM items")
    records = cursor.fetchall()
    print(records)
    print_records = ''
    for record in records:
        print_records += str(record[0]) + ", " + str(record[1]) + " items, $" + "{:.2f}".format(float(record[2])) + ", ID" + "\t" + str(record[3]) +"\n"
    query_label = Label(window, text=print_records)
    query_label.grid(row=5, column=0, columnspan=2)
    connection.commit()
    connection.close()

#functions for updating
def update():
    connection = sqlite3.connect("inventory.db")
    cursor = connection.cursor()
    record_id = select_box.get()

    cursor.execute(
        'UPDATE items SET name=?, quantity=?, price=? WHERE oid=?',
        (item_name_editor.get(),item_quantity_editor.get(),item_price_editor.get(),record_id)
    )
    connection.commit()
    connection.close()
    editor.destroy()

def edit():
    global editor
    editor = Tk()
    editor.geometry("450x125")
    editor.title("Edit Inventory")
    connection = sqlite3.connect("inventory.db")
    cursor = connection.cursor()
    record_id = select_box.get()

    cursor.execute("SELECT * FROM items WHERE oid=?",(record_id))
    records = cursor.fetchall()

    global item_name_editor
    global item_quantity_editor
    global item_price_editor

    item_name_editor = Entry(editor, width=20)
    item_name_editor.grid(row=0, column=1, sticky=W)
    item_quantity_editor = Entry(editor, width=20)
    item_quantity_editor.grid(row=1, column=1, sticky=W)
    item_price_editor = Entry(editor, width=20)
    item_price_editor.grid(row=2, column=1, sticky=W)

    item_name_label_editor = Label(editor, text='Name ')
    item_name_label_editor.grid(row=0, column=0, sticky=E)
    item_quantity_label_editor = Label(editor,  text='Quantity ')
    item_quantity_label_editor.grid(row=1, column=0, sticky=E)
    item_price_label_editor = Label(editor, text ='Price ($) ')
    item_price_label_editor.grid(row=2,column=0, sticky=E)

    for record in records:
        item_name_editor.insert(0, record[0])
        item_quantity_editor.insert(0, record[1])
        item_price_editor.insert(0, record[2])
    save_btn = Button(editor, text="Save Record", command=update)
    save_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=145)
    connection.commit()
    connection.close()

#Create table
connection = sqlite3.connect("inventory.db")
cursor = connection.cursor()
#cursor.execute("CREATE TABLE items (name TEXT, quantity INTEGER, price INTEGER)")
connection.commit()
connection.close() 

#create window
window = Tk()
window.geometry("400x450")
window.title("Inventory Summary")

#create entry boxes
item_name = Entry(window, width=20)
item_name.grid(row=0, column=1, pady=2, sticky=W)
item_quantity = Entry(window, width=20)
item_quantity.grid(row=1, column=1, pady=2, sticky=W)
item_price = Entry(window, width=20)
item_price.grid(row=2, column=1, pady=2, sticky=W)

item_name_label = Label(window, text='Name ')
item_name_label.grid(row=0, column=0, pady=2, sticky=E)
item_quantity_label = Label(window,  text='Quantity ')
item_quantity_label.grid(row=1, column=0, pady=2, sticky=E)
item_price_label = Label(window, text ='Price ($) ')
item_price_label.grid(row=2,column=0, pady=2, sticky=E)

#button to add new row
submit_btn = Button(window, text="Add Record to Database", command=submit)
submit_btn.grid(row=3, column=0, columnspan=2, pady=2)

#button to show everything
query_btn = Button(window, text="Show Records", command=query)
query_btn.grid(row=4, column=0, columnspan=2, pady=2)

#update records
select_box=Entry(window, width=20)
select_box.grid(row=6, column=1, pady=2, sticky=W)

select_box_label = Label(window, text='Select ID ')
select_box_label.grid(row=6, column=0, pady=2, sticky=E)

#button to update records
edit_btn = Button(window, text="Update Record", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, pady=2)



window.mainloop()



#import tkinter as tk
#from tkinter import ttk
#import sqlite3

#root = tk.Tk()

#Func to change button text
#def changeText(blankForNow):
    #print(blankForNow)
    #con = sqlite3.connect("animeList.db")
    #cur = con.cursor()
    #allTitles = cur.execute("SELECT title FROM anime")
    #titles = allTitles.fetchall()
    #print(f'{titles[myRow]}')
    #button['text'] = 'huzzah'
    
#button = tk.Button(root, text='click me', command = changeText)
#button.pack()

#Function that gets our titles
#def listTitles():
    #con = sqlite3.connect("animeList.db")
    #cur = con.cursor()
    #cur.execute("ALTER TABLE anime ADD COLUMN 'id' integer") — already did
    #myColumn = 0
    #myRow = 0
    #wholeDb = cur.execute("SELECT * FROM anime")
        #finds everything from anime
    #allAnime = wholeDb.fetchall()
        #everything, so [#] gives which row
    #myAnime = allAnime[myRow]
        #just my row, so [] gives the column
    #print(myTitles)
    #print("All Anime: ")
    #for genres in myAnime:
    #cur.execute("UPDATE anime SET id = 4 WHERE genre = 'comedy'")
    #myTitle = cur.execute("SELECT title FROM anime WHERE id = 4")
    #print(f'Yeehaw + {myTitle}')
    #myRow += 1
    #i += 1
    
    #for my_genres in genres:
        #print(f'my_genres {my_genres}')
        #print(f'genres {genres}')
        #cur.execute("UPDATE anime SET id = ? WHERE genre = ?", (i, my_genres[i]))
        #tk.Button(root, text=f"{my_genres[1]}", command=lambda: changeText()).pack()
        #tk.Button(root, text=f"{my_genres[1]}", command=lambda: changeText(f"ahhh")).pack()
        #i += 1
        #"my_genres" is all the rows, so the [#] is giving which column
        #"genres" is everything
    
#Button and stuff for listTitles function
#show_titles = tk.Button(root, text="Show Titles", command=listTitles)
#show_titles.pack()





#sqlite stuff
#import sqlite3
#con = sqlite3.connect("animeList.db")
#cur = con.cursor()
#res = cur.execute("SELECT name FROM sqlite_master") 
    #— finds db
#dbName = res.fetchall()
#print(dbName)
#cur.execute("INSERT INTO anime (title, genre) VALUES ('The Disastrous Life of Saiki K.', 'comedy')")
#con.commit()
#res = cur.execute("SELECT title FROM anime")
    #finds titles
#myTitle = res.fetchall()
#print(myTitle)



#root = tk.Tk()
#Always last — actually tells it to make it
#root.mainloop()


#Window properties
#root.title("My Example") 
    #title
#root.configure(background="pink") 
    #window color
#root.minsize(200, 200) 
    #window minsize
#root.maxsize(500, 500) 
    #window maxsize
#root.geometry("300x300+50+50") 
    #window 1st/default size

#widgets — more exist than this, accessible here: https://tkdocs.com/tutorial/widgets.html

#def selection_changed(event):
    #selection = event.widget.curselection()
    #if selection:
        #index = selection[0]
        #label.config(text=f"{event.widget.get(index)} selected!")
        #event.widget.get(index)

#listbox = tk.Listbox(root)
#for item in ["One", "Two", "Three"]:
    #listbox.insert(tk.END, item)
#listbox.bind("<<ListboxSelect>>", selection_changed)
#listbox.pack(padx=5, pady=5, fill="both", expand=True)

# A helper label to show the selected value
#label = tk.Label(root, text="One selected!")
#label.pack(padx=5, pady=5, fill="x")

#widgets = [
    #tk.Label, 
        #non-interactive
    #tk.Checkbutton, 
        #checkbox
    #ttk.Combobox, 
        #dropdown, requires "from tkinter import ttk"
    #tk.Listbox,
        #like combobox, but can select multiple at once
    #tk.Entry, 
        #text entry
    #tk.Button, 
        #button
    #tk.Radiobutton, 
        #toggle with only 1 active item
    #tk.Scale, 
        #slider
    #tk.Spinbox, 
        #integer spinner
#]

#for widget in widgets:
   # try:
        #widget = widget(root, text=widget.__name__)
    #except tk.TclError:
        #widget = widget(root)
    #widget.pack(padx=5, pady=5, fill="x")


#Labels
#tk.Label(root, text="yeehaw!").pack() 
    #root tells you which window, pack tells you placement
#tk.Label(root, text="Abraham Linkin").pack() 
    #funnier mispelled

#Can display images with following code:
#image = tk.PhotoImage(file="filepath")
#tk.Label(root, image=image).pack()


