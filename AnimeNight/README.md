# Anime Night's Gonna Be Lit
## General idea:
Basically, my friends and I hang out and watch anime a few times per semester. Recently, I started doing a "Jeopardy board" type thing where we can only see the genre of the anime. We each choose one, and then we have to watch whatever it is, no matter how bad. It's way more fun this way.
Unfortunately, there are some disadvantages to this approach: The Jeopardy site only takes so many "questions," so we can't put in all of our anime. We also can't sort the anime, so sometimes when we have new people over, they end up watching stuff that's maybe not the best introduction to anime (I'm sorry Charlene.) We also can't keep track of what we've watched recently. So I want to make my own site specifically for our anime nights. This is something I'm 100% going to do regardless of if it's for class, but I think it would be really fun.
Another reason I want to do this is because a lot of it is based around a tagging and sorting system, and something I want to try later is making a site to get my sheet music (and/or maybe knitting and stuff?), and I want that to have a tagging system (for ranges, instrumentations, etc., or sizes, garment types, etc.), but this would be a like a prototype of that system so I can do it better next time.
I'd probably use Github Pages for this (thanks for making all course materials available).

## Features I want

### Tag System

#### Tags
* title
* last episode
* last date we watched it
* genre
* rating out of 10
* content warnings(?)

### Interactivity
* Shows cards w/ genre that flip to show anime title
	* Pretty easy w/ css (:hover)
	* Or can make javascript button
* Ability to sort by tags (any watched on x date, in x genre, between x-y ratings, etc.)

## Stuff from Meeting w/ Rachel
		
* SQLlite database and python — do reading early
* Python scripts to access database — due by 2 weeks before final
* If not burnt out, then try for website
* LMSC-223 with rachel in the fall

## Project Started
### 4.5.25
* Worked on proposal for final
* Checked 261sp25 SQL lesson, reviewed in terminal
* Went and found database I made in files

#### Making the Database
Working in terminal
cd to AnimeNight folder
```
sqlite3 animeList.db
```
Columns:
	* Title
	* Genre
	* Episode (current)
	* Date (last watched)
	* Rating
	
Looked at documentation to find how to input date (string as "YYYY-MM-DD" is best for me)
Typing this here first, then copying it over (so I don't mess up in the terminal)

```
CREATE TABLE 'anime' ('Title' text, 'Genre' text, 'Date' text, 'Rating' integer);
```

Tested to make sure input worked

```
INSERT INTO anime (Date) VALUES('2025-11-11');
SELECT Date FROM anime;
```

Got back '2025-11-11' yay!

Forgot to do an "episode" column, so added that

```
ALTER TABLE anime ADD COLUMN 'episode' integer;
```

Got annoyed typing capitals for column names, so changed them

```
ALTER TABLE anime RENAME COLUMN Title TO title;
```
Etc.

#### Python
Didn't feel like inputting anime right now, so switched gears to python. Used https://www.allendowney.com/wp/books/think-python-2e/ (from our textbook), skipped to end and installed Jupyter (already have python on computer).
Got a nice theme so I could make it look nice (it's blue and pink)

#### Connecting python and sqlite
Followed steps outlined here (skipping making the database and stuff bc I did that in sqlite already):
https://docs.python.org/3/library/sqlite3.html

Added some anime to sql db in python, checked to make sure it actually committed.

##### User Input into Database

Tried:
```
myTitle = input()
cur.execute("INSERT INTO anime (title) VALUES (myTitle)")
```
Got:
```
OperationalError                          Traceback (most recent call last)
Cell In[46], line 1
----> 1 cur.execute("INSERT INTO anime (title) VALUES (myTitle)")

OperationalError: no such column: myTitle
```
Tragic
Looked up how to actually do it (as opposed to just attempting it the way it'd be done if I ruled the world)
https://stackoverflow.com/questions/55955690/ask-for-user-input-and-insert-in-db-in-python-with-sqlite3
Would not have guessed that jeez

#### GUI
Gotta figure out how that's happening
Checked our book, has a chapter on interface design
Looks like I installed python with homebrew (I literally don't remember when I did this, maybe back in 2nd semester when I made a Renpy game???)
So I need to get tkinter — https://www.python.org/downloads/release/python-3132/
(didn't want to deal with Anaconda or whatever the book guy was recommending)

### 4.9.2025
It got mad at me so I redid everything oh well
(For more detail: "animeList.db" didn't seem to exist anymore in Jupyter. I tried to open it in terminal, it also didn't find it. I looked in the folder it should've been in, it was not there. Trag.)
Redoing it was pretty easy though — this time I created the database entirely in Jupyter. It's literally just sql in ("") but it's nicer having it all in one place as opposed to going into the terminal



### 4.16.2025
Back to GUI stuff
https://www.pythonguis.com/tutorials/create-gui-tkinter/
Tested a bunch of stuff following above tutorial


### 4.24.2025
#### In Class Stuff
/opt/anaconda3/bin/python3
Set everything up to work in TextMate which is WAY nicer than the thing the book guy wanted
During break (30 min), made new folder "ActuallyUsing" for stuff that's not just tests, made new SQL database, made python script (empty)
Plan for later:
	* populate lists from database (make into a function)
	* User input through python to database (make into a function)
	* More GUI stuff
		* Buttons top priority
		
### 4.25.2025
Put 4 anime into db so I can test and stuff
Started up all that python stuff again ahhhhhh i'm so tired i hate orchestration and composition let me tell you literally torturous (this is important documentation bc I stayed up until 4 just to make dorico do some bull)

Working in test.py
Returned here: https://www.pythonguis.com/tutorials/create-gui-tkinter/


might be nice to use combobox, populate w/ sql db somehow?
```
myCombobox = ttk.Combobox(root, values["anime1", "anime2", "anime3"])
```

```
def selection_changed(event):
    label.config(text=f"{event.widget.get()} selected!")

combobox = ttk.Combobox(root, values=["One", "Two", "Three"])
combobox.set("One")
combobox.bind("<<ComboboxSelected>>", selection_changed)
combobox.grid(padx=5, pady=5, fill="x")

/# A helper label to show the selected value
label = tk.Label(root, text="One selected!")
label.grid(padx=5, pady=5, fill="x")

```
Maybe use listbox for filters and entry to add new anime

Got tkinter GUI and sqlite to work together —
made function that gets titles:
```
def listTitles():
    con = sqlite3.connect("animeList.db")
    cur = con.cursor()
    res = cur.execute("SELECT title FROM anime")
    myTitle = res.fetchall()
    print(myTitle)
    tk.Label(root, text=myTitle).grid()
```
Then have tk stuff:
```
show_titles = tk.Button(root, text="Show Titles", command=listTitles)
show_titles.grid()
```
For some reason, it shows up like this:
"Yugioh {{Code Geass}} {{Mob Psycho 100}} {{Bobobo-Bo Bo-BoBo}}" (yes that last one is real idk either)
Technically I have a cast party in like 10 minutes but honestly I'm so sick of people I might just keep at this a bit longer anyway

Next steps:
* Make filtering system (ahhhhhhhhh)
* Make buttons from what we select using the genres
	* Populate list
* Make it so text of button (and maybe color) changes when we click
* Figure out why we have the curly brackets
* Make thing so we can insert stuff


Curly Brackets solved by doing it right:
https://www.freecodecamp.org/news/work-with-sqlite-in-python-handbook/#heading-how-to-query-data
```
def listTitles():
    con = sqlite3.connect("animeList.db")
    cur = con.cursor()
    res = cur.execute("SELECT title FROM anime")
        #finds titles
    myTitle = res.fetchall()
    #print(myTitle)
    print("All Anime: ")
    for titles in myTitle:
        print(titles)
        tk.Label(root, text=titles).grid()

show_titles = tk.Button(root, text="Show Titles", command=listTitles)
show_titles.grid()
```
above got rid of one set of curly brackets per thing

Adding "str(titles)" as below changed it so curly brackets are gone, but now there's "'(),'" for each

```
tk.Label(root, text=str(titles)).grid()
```
this looks useful
https://www.pybeginners.com/python-projects/how-to-make-a-to-do-app-with-python-sqlite-and-tkinter/

But now I'm going to my party oops

### 4.26.2025
https://ashleygingeleski.com/2021/01/30/how-to-build-an-inventory-app-with-tkinter/ — seems promising. Tragically didn't really help

focusing on changing button text now
https://pythonexamples.org/python-tkinter-change-button-text-dynamically/
Easy!!!!! Yay!!!!!!

Ok so:
changeText function that can change text from anime genre to anime title
listTitles function that creates a button for each anime, with the text as the genre

```
tk.Button(root, text=f"{my_genres[i]}", command=changeText).grid()
```
Above did a lot for me, but need to get changeText func so that it changes the button that called it and then so it changes to the title (right now it's as below)
```
def changeText():
    button['text'] = 'huzzah'
```

Biggest issue is using same function with multiple buttons, need the button and text to be variable
https://www.w3schools.com/python/python_lambda.asp
https://stackoverflow.com/questions/6920302/how-to-pass-arguments-to-a-button-command-in-tkinter

Also need to figure out how to separate columns from sqlite w/o having to cur.execute and fetchall() every column
Oh duh use "WHERE" ex. "SELECT genre FROM anime WHERE title=my_genres[i]" 

running into issues where all my variables are local so not getting passed on

so, doing below (passing actual integer through lambda) works, but we need integer to increase each time ahhhhh
```
def changeText(myRow):
    print(f'{titles[myRow]}')

def listTitles():
        tk.Button(root, text=f"{my_genres[1]}", command=lambda: changeText(0)).grid()
```

Could create extra column for an id#, then have it assign id #s to each as they go through?
Tried following

```
cur.execute("UPDATE anime SET id = ? WHERE genre = ?", (i, my_genres[i]))
tk.Button(root, text=f"{my_genres[1]}", command=print(id)).grid
```

Got: "sqlite3.OperationalError: database is locked"
https://stackoverflow.com/questions/3172929/operationalerror-database-is-locked
Just tried it a second time and got something different — "<built-in function id>" for all 4 anime currently in the database. No buttons were created
I'm an idiot and forgot parentheses after grid ahhhhhhhhhh
That didn't fix it though

Tested so many different things ahhhhh i'm dying here

```
def listTitles():
    con = sqlite3.connect("animeList.db")
    cur = con.cursor()
    #cur.execute("ALTER TABLE anime ADD COLUMN 'id' integer") — already did
    myColumn = 0
    myRow = 0
    wholeDb = cur.execute("SELECT * FROM anime")
        #finds everything from anime
    allAnime = wholeDb.fetchall()
        #everything, so [#] gives which row
    myAnime = allAnime[myRow]
        #just my row, so [] gives the column
    #print(myTitles)
    print("All Anime: ")
    #for genres in myAnime:
    cur.execute("UPDATE anime SET id = 4 WHERE genre = 'comedy'")
    myTitle = cur.execute("SELECT title FROM anime WHERE id = ?", (myRow))
    print(f'Yeehaw + {myTitle}')
    myRow += 1
```
Think it through:
For each row in database, want new button storing all of that row's info

I copied almost all code from "https://ashleygingeleski.com/2021/01/30/how-to-build-an-inventory-app-with-tkinter/"
It works, now just need to figure out how to use the parts I need
Started working in test2.py bc test.py is really messy lmao


LET'S GOOOOOO!!!!!!!!!! I DID IT!!!!!!!!
Ok so:
* We've got our button, "print_anime"
* It calls a function that creates our buttons
	* That function pulls all the rows from our db into a global array, then uses a for loop to make buttons for each row, naming each with a number and the genre associated with that row
	* Each button passes on their text to a function that changes the text by doing the following:
		* slices the text so it's just the number at the beginning
		* grabs the button from the button array that matches that number
		* grabs the title of the row associated with the id matching that number
		* slices the title down bc for some reason it always includes the parentheses around the title
		* changes the text of the button we grabbed to the title we grabbed

Added "myColumn = 1" and made "columns[1]" into "columns[myColumn]" so we can change what we filter for later

Now I want it so it switches back and forth when I click on it
Trying:
```
    if myTitle != myText:
        myBtn['text'] = f"{int(myID) + 1} {myTitle}" #changing text and keeping number at beginning
    else:
        cur.execute("SELECT ? FROM anime WHERE id = ?", (myColumn, myID))
    con.close()
```
Didn't change at all, but realized "myText" has number at beginning
Changed to "if myText[2:] != myText" so we slice off number
Now it's changing the first time but it's still not changing back
printing myText[2:] and myTitle each time, can see they look the same??
I'm stupid and forgot to tell it to actually switch the text if they are the same ughhhhh
Did that literally so embarassing like yaeh the code's not gonna code if you don't code it jjeeeeeeez


### 4.27.2025
Two major things left — entering (and updating) anime, and filtering
Gonna start with filtering real quick
Basically just affect print_anime button so that it takes an entry (listbox might be nice) for different columns
https://pythonexamples.org/python-tkinter-listbox/

tested following:
```
listbox = tk.Listbox(root, height=3, selectmode=tk.MULTIPLE)
listbox.grid()
listbox.insert(tk.END, "thing 1")
listbox.insert(tk.END, "thing2")
```
Works

so we can pull all columns — PRAGMA table_info('anime')
https://iifx.dev/en/articles/2472226
https://sqlite.org/pragma.html

Want it to show column titles with values of columns selectable underneath
So maybe listbox for each column
So populate array[] with columns[], then populate columns[] with column values[]????

Below pulls and displays column names
```
cur.execute("SELECT * FROM anime")
schema = [column[0] for column in cur.description]

for i in range(len(schema)):
    listbox.insert(tk.END, str(schema[i]))
```
### 4.28.2025
Ok think through what I want end result to be

* Filter system
	* Show all tags
	* Select multiple tags
	* Only make buttons from these

```
con = sqlite3.connect("animeList.db")
cur = con.cursor()
cur.execute("SELECT * FROM anime")
animes = cur.fetchall() #every row
for i in range(len(animes)):
    columns = animes[i] #gets row i
    for q in range(len(columns)):
        print(columns[q]) #gets column q from row i
```
above separates out everything
Need to figure out how to show each thing only 1x, and don't show titles here
https://www.reddit.com/r/sqlite/comments/13yfdm6/querying_table_with_null_value_without_using_is/

```
for i in range(len(animes)):
    columns = animes[i] #gets row i
    for q in range(len(columns)):
        if columns[q] != columns[0] and columns[q] != None:
            print(columns[q]) #gets column q from row i
```

Now need to get rid of id numbers

```
for q in range(len(columns)-1):
```

adding listbox
```
listbox = tk.Listbox(root, height=3, selectmode=tk.MULTIPLE) #make lsitbox
listbox.grid() #grid it
con = sqlite3.connect("animeList.db")
cur = con.cursor()
cur.execute("SELECT * FROM anime")
animes = cur.fetchall() #every row
for i in range(len(animes)):
    columns = animes[i] #gets row i
    for q in range(len(columns)-1):
        if columns[q] != columns[0] and columns[q] != None:
            print(columns[q]) #gets column q from row i
            listbox.insert(tk.END, str(columns[q]))
```

now need to get rid of repeats
https://www.w3schools.com/python/python_howto_remove_duplicates.asp
lmao this just cut it into every letter

Alright, below works

```
listbox = tk.Listbox(root, height=3, selectmode=tk.MULTIPLE) #make lsitbox
listbox.grid() #grid it
tags = [] #make it exist
con = sqlite3.connect("animeList.db")
cur = con.cursor()
cur.execute("SELECT * FROM anime")
animes = cur.fetchall() #every row
for i in range(len(animes)):
    columns = animes[i] #gets row i
    for q in range(len(columns)-1): #-1 for skipping ID
        if columns[q] != columns[0] and columns[q] != None:
            print(columns[q]) #gets column q from row i
            tags.append(str(columns[q])) #add tags we got to list
tags = list(dict.fromkeys(tags)) #get rid of repeats
print(tags)
```

Ok, so this makes the options in our listbox

```
for i in range(len(tags)):
    listbox.insert(tk.END, tags[i])
    print(tags[i])
```
ok, so now I need to connect all that stuff for the listbox to the button that generates the buttons
Also make all that stuff into a function bc it's so much lmao
Ideally we'd be doing like cur.execute("SELECT * FROM anime WHERE") and then uses the ? thing, but we don't know how many variables we're going to have
Could switch from listbox to multiple comboboxes — so one for genre, one rating, etc
Actually that might be best, bc we can't have multiple genres or anything anyway (didn't set it up like that)

https://pythonassets.com/posts/drop-down-list-combobox-in-tk-tkinter/

```
def makeFilters():
    #listbox = tk.Listbox(root, height=3, selectmode=tk.MULTIPLE) #make lsitbox
    #listbox.grid() #grid it
    current_var = tk.StringVar()
    combobox = ttk.Combobox(root, textvariable=current_var)
    combobox['values'] = []
    combobox.grid()
    tags = []
    con = sqlite3.connect("animeList.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM anime")
    animes = cur.fetchall() #every row
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
```		
Ok, next thing is to use what we did to generate listboxes by column so we get one for each thing, then can populate it the way we have above
Actually no next thing is connecting combobox to button otherwise we'll be so annoyed when we generate them

added "selection = combobox.get()" to top of makeButtons function
moved combobox out of function to where all of my global variables are so it can be accessed
added "tk.Label(root, text=selection).grid()" so we can see what it picks

ok, so then probably want something like
""select * from anime WHERE ? = ?" (column, selection)"
Need some way to only select which ones we want — maybe "column" and "selection" are both variables, we put them in a for loop going through all the selections we have, although that's more like an OR than an AND search, and we probably want an AND search
basically need ""SELECT * FROM anime WHERE ? = ? AND ? = ?"" with the amount of "? = ?" determined by the number of columns we have
Could have it be non-dynamic so it's "genre = ? AND rating = ?" but then if we change anything we're screwed so
Nested sqlite queries looks promising

switched from grid to grid to see if i can make it look nicer, will probably be useful then

Maybe we could do like 
options = "SELECT * FROM anime"
and then start looping through the rest by taking from the options instead somehow?
But like surely there's an easier way ugh

Ok, so:
1. get all comboboxes into a list
2. in "for i in range(len(animes)):" make another loop that goes for the length of the comboboxes
3. this loop checks whether the current anime's column matches the current combobox
```
for g in range(len(selection)):
	if selection[g] != None and selection[g] == columns[g]:
		#stuff for buttons
```
tested it. it didn't work likely bc we didn't do anything for making a combobox list

Really annoying me rn. Maybe we go back to doing listboxes but have it so everything is "OR" instead of "AND"? So we'll get comedy OR action? Or we make a bunch of listboxes like we'd been planning to, so we can have OR within columns and AND between columns (ex. comedy OR action AND rating of 4)
That might work a lot better actually ugh

### 4.30.2025
Ok back to listboxes

https://www.pythontutorial.net/tkinter/tkinter-listbox/ kind of got this working, except it only works with the first listbox selection for some reason — doesn't work for second, doesn't work for multiple
Basically this is the code: 
```
selection = ",".join([listbox.get(i) for i in selected_indices])
```
Issue is that "selection" is being read as just a long string as opposed to multiple strings within a variable (figured this out by using print(selection[0]), because if it was an array/list, it would print out a whole word, but since it's one string it prints as just the letter at that position)
I have no idea how to fix that

https://www.w3schools.com/python/python_lists_add.asp — 
```
selection.insert(i, listbox.get(i))
```
This works sort of

LET'S GOOOOOOO I gave up on explaining the problem above bc I was too busy trying to fix it but here's the solution:

So, there were a couple of problems
1. In og code, we had:
```
if selection[i] != None and selection[i] == columns[myColumn]:
	(all the stuff for making the buttons)
	btns[i].grid
```
it's all the "i" that was the problem — we added an extra 2 for loops above this for loop, so all the variables were higher than what we actually wanted. The nested for loops we ended up with are "i in range(len(selection))" and "i in range(len(animes))." So, for each item in selection, we were cycling through all of animes, which meant that when we had our if statement depending on selection[i], it wasn't actually checking for the selection in the higher/first loop, but for the selection that matched whichever anime we were on. Same thing happened with btns[i].grid — by the time we actually met the conditions of the if statement, we were way past 0, so we were trying to do btns[5].grid or something, but there was only 1 button at that point.

So I solved it by just adding more variables. We now have:
```
    for g in range(len(selection)):
        for i in range(len(animes)):
            columns = animes[i]
            print(animes[i])
            cur.execute("UPDATE anime SET id=? WHERE title=?", (i, columns[0]))
            con.commit()
            print("columns[MyColumn]: " + columns[myColumn])
        #print(animes[i])
            print("selection[g]: " + selection[g])
            if selection[g] != None and selection[g] == columns[myColumn]:
                number_of_btns += 1
                btns.append(tk.Button(root, height="5", width="25", text=str(i + 1) + " " + columns[myColumn], command=lambda c=number_of_btns: changeText(btns[c].cget("text"))))
                print(number_of_btns)
                btns[number_of_btns].grid()
            else:
                print(" ")
```
And it works beautifully! The only thing I want to fix now is deleting all existing buttons each time we click the print_buttons button

https://www.geeksforgeeks.org/how-to-hide-recover-and-delete-tkinter-widgets/
Ok that's not working and I've also realized a new problem
Bc we're not clearing selection, now when we get to btns[number_of_btns].grid after the first time, it's still just making btns[0], except that's a value from the first time round
Also destroying buttons isn't working
```
    for i in range(len(btns)):
        btns[i].destroy
```
ok, for first issue, tried "selection.clear()" Not sure why but after that it doesn't take any previous values even if clicked on again.
Did:
```
def createButtons(2):
	selection.clear()
	for i in range(len(btns)):
		btns[i].destroy
	btns.clear()
```
That solved clearing issue, but still doesn't delete buttons
https://www.delftstack.com/howto/python-tkinter/how-to-hide-recover-and-delete-tkinter-widgets/ THIS WORKS!
```
	for i in range(len(btns)):
		btns[i].grid_remove()
```
I also changed "tk.Label(root, text=selection).grid()" (used to put what we searched for down) to "MyLabel=tk.Label(root, text=selection).grid()" and added a .grid_remove() at the top of func for it, too
Which ended up being way more complicated than I thought it would be, of course — had to put it up top with my global functions ("myLabel=tk.Label(root, text="")"), then tell the function that it existed globally ("global myLabel"), and then I could grid_remove() it

But now it works so so beautifully

Ok now I want to actually use the grid function to make things look nice
Actually nevermind it's not that important rn — what is important is getting the system for adding more anime
And I will do that tomorrow because it's a little embarrassing how late it's gotten (fun fact it is now May)

### 5.1.2025
ok new problem: change text doesn't work (list index out of range, classic)
it only doesn't work if I'm filtering out what would be the 1st button, so I think the issue is this:
when we create the buttons, we have this line of code:
```
cur.execute("UPDATE anime SET id=? WHERE title=?", (i, columns[0]))
```
But this is actually *before* the if statement where we actually make the buttons, so even though not all rows are being made into buttons, all rows are still getting numbers, which means that when the changeText function is looking for the button matching the id number, it can't find it bc there is no button 4 or whatever.
Proposed solution: just move that bit of code under the if statement that makes the buttons, also put it under a bool so it only does it 1x
No I'm still dumb bc it's setting the id to the i from i in range(len(animes)), so it's still going to go up no matter what
Also because changeText is changing text by the number written on the button, we also need to change that to "text=str(number_of_btns)"

YEAH THAT WORKED

ok now for adding new anime

if you remember from way back when, I found someone that had made a submit form w/ tkinter, python, and sqlite, and I copied all of their code into my test.py document
well that's back finally now

So I did the visual side of that (haven't made the actual functions yet) but unfortunately I have realized there's another problem with the button changeText function

Basically, the last button will just show a number instead of working like it used to.
I made a new file — test4.py — and deleted all the stuff I'm not using anymore so it's easier to look at and figure out what the problem is

I GOT IT!
```
number_of_btns = -1

cur.execute("UPDATE anime SET id=NULL")

```
and then I also put "number_of_btns += 1" at the top of the if statement that makes the buttons (I should really have named that)

Basically the problem was that there were multiple anime with the same id so it wasn't working

OK finally it's time to add new anime woohoo!

I copied the submit function from the submission code I borrowed

I SCREWED UP AND SUBMITTED THE SAME ONE TWICE HOW DID I DO THAT FIRST TRY I THOUGHT I'D BE ABLE TO AVOID THAT PROBLEM FOR AT LEAST A DAY!!!!!!!!!!!!!!!!!!!!!

Could try for an if statement i guess but ugh i'm so sick of if statements. and for loops. it never ends. much like a badly made for loop

Ok I went into terminal and deleted the Full Metal Alchemists I inputted, then added ONE Full Metal Alchemist back in with the python stuff, then tested it and it works now

I still need to solve the duplicate problem :(

Don't want to so I'm looking into making it pretty instead: https://pythoneo.com/how-to-make-tkinter-look-good/

https://www.reddit.com/r/learnpython/comments/auq4ln/is_it_actually_possible_to_create_a_rather_good/

Duplicate problem
Alright I tried:
```
"INSERT INTO anime(title, genre) VALUES (?, ?)"
```
Which did not work. Also now there's a new issue with the button changeText function, for some reason when I click on the last one it switches genre ahhhhhh
I literally don't understand!!!!!!!!!!!!!!!!! WHY ARE YOU HURTING ME LIKE THIS

I commented out all my print functions, then added a couple in changeText function. It looks like myID is one lower than it needs to be now.

Actually I was wrong about that I have no idea what's wrong and I'm taking a break.

Break over
I'm guessing what's happening is it's still counting the wrong id somehow? Because what I'm seeing is an issue with subsequent rows where the genre is different — so if it goes "action, comedy, action," the last action will come back as comedy at the end for some reason

Doing this:
```
cur.execute("SELECT genre FROM anime WHERE id = ?", (myID))
```
instead of this:
```
cur.execute("SELECT ? FROM anime WHERE id = ?", (columns[myColumn], myID))
```
works. don't know why. choosing to not care until it becomes an issue again.

MOVING ON! Duplicates issue
So it sounds like I can use a "UNIQUE" constraint to make it so titles can't be duplicated
BUT it also sounds like that's not possible to add/you have to put that in when you create a table
which I don't really want to do
But I will try — plan is to move current db out of the folder, make a new one with the same name but with unique constraint, and see what's up

### 5.2.2025
Had to stop bc I was at a show (I was in the show unfortunately. Fortunately it was a show about monkeys and I got to play a very patriotic bald eagle) and then I had other homework that was due sooner.
Things I have left to do are:
1. unique constraint
2. more filters (by rating, etc.)
3. update function (probably a new window?)
I want to finish as much as possible for tomorrow because we are actually having an anime night (well, afternoon).

2. More Filters:
	* So we have this variable in our createButtons function (in a for loop) — columns=animes[i] — so columns is 1 row. Then we have columns[myColumn], which gives us just 1 column of that row
		* Ex. columns = animes[0] means that columns is the entire row for Yugioh, so then columns[0] gives us the title of Yugioh, columns[1] gives us the genre, etc.
	* So, if we want to search more columns, we just need to change the number in columns — columns[1] for genre, 2 for episode, 3 date, 4 rating
	* So then there's several steps
		1. get all filters into the listbox
		2. get filters FROM listbox
		3. sort through data
	* There's also the question of if we want it to be AND searching or OR searching
I think multiple listboxes is probably still the best idea. That way, we can search the columns by the listbox, and we can use OR searching within listboxes and AND searching out of them (so, when searching for genres, we'll get every genre we select, but we won't get anime that are rating 5 OR comedy).

```
    number_of_lbs = 0
    tags = []
    con = sqlite3.connect("animeList.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM anime")
    schema = [column[0] for column in cur.description]
    for i in range(len(schema)-1):
        cur.execute("SELECT ? FROM anime", (schema[i],))
        currentColumn = cur.fetchall()
        #print(currentColumn)
        if schema[i] != "title":
            print(schema[i])
            tk.Label(root, text=str(schema[i])).grid()
            myLBs.append(tk.Listbox(root, height=3, selectmode=tk.MULTIPLE))
            myLBs[number_of_lbs].grid()
            number_of_lbs += 1
        else:
            print("")
```
I hesitate to say it out of fear of jinxing myself but that went shockingly well. It took like basically no time. And worked almost 1st try.
Anyway, that's just for making the listboxes (not including one for title or ID(actually changed those lines from "for i in range(len(schema)-1):" to no "-1" there and instead "if schema[i] != "title" **and schema[i] != "id":**" just bc then if id isn't the last one anymore it would still work))

So now for inserting into listboxes

So I've got the following:
```
    for g in range(number_of_lbs):
        for i in range(len(tags)):
            myLBs[g].insert(tk.END, tags[i])
```
This of course just inserts all the tags into all the boxes, whereas I need it to insert only certain tags (ex. only genres in the genre listbox)

```
    myCounter = 0
    for i in range(len(animes)):
        columns = animes[i] #gets row i
        for q in range(len(columns)-1): #-1 for skipping ID (last one)
            if columns[q] != columns[0] and columns[q] != None: #get column q from row i as long as it's not the title [0] or null [None]
                tags.append(str(columns[q]))
                tags = list(dict.fromkeys(tags))
                print(tags)
                #byColumn.append([tags[myCounter]])
                myCounter += 1
                #byColumn.append(tags)
                #tags.clear()
    for g in range(number_of_lbs):
        for i in range(len(tags)):
            myLBs[g].insert(tk.END, byColumn[i])
```
Above is where I'm at currently. I think I'm getting there, but right now the issue is that we're adding to myCounter every time we cycle through, but bc we have dict.fromkeys preventing repeats, myCounter is getting higher than the number of tags.

Ok so "myCounter = len(tags)" works
but i still don't know how to get things into just the one listbox i need them in ahhhhhh
I thought maybe I could do a list of lists, with each list being one set of tags, but I couldn't figure that out at all

So I think we should be able to use the column variable somehow
Like, instead of going anime by anime/row by row, we go column by column to get all the tags
so like for i in range(len(schema)) grab everything for column[i], etc.

https://stackoverflow.com/questions/51112900/how-do-i-get-all-values-of-a-column-in-sqlite3
ok that wasn't helpful at all
What I've decided to do instead is steal from some earlier stuff I did — basically I had i in range(len(animes)), then columns = animes[i], and then columns[i] which would give me 1 column for 1 row

```
    for i in range(len(animes)):
        columns = animes[i]
        for g in range(len(columns)):
            print(columns[g])    
```

So now I need to get rid of first and last of animes — same as before, use if statement
Except actually I'm wrong bc this is still going from column to column

tried this:
```
    for i in range(len(animes)):
        print(schema[i])
        cur.execute("SELECT ? FROM anime", (schema[i],))
        tags = cur.fetchall()
        print(tags)
```
which is not working for some reason, even though when I replace the ? with a column name it works, and when I print schema[i] it gives a column name, but instead it just prints tags as column names and I don't understand

Ok i thought a lot and looped around back to the beginning of maybe happy ending (aNy mAiL FrOM jAmES ChOi??) and I got it
```
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
```
I tested it without the if statement first, so it would show that it's actually filtering by column (since the only filled ones rn are title and genre)

So, next thing is making the filtering work again with the buttons

Saved as test5.py just in case

made number_of_lbs global, and then below worked

```
    for t in range(number_of_lbs):
        selected_indices = myLBs[t].curselection() #gets number/index of what's selected
        for i in selected_indices:
            selection.insert(i, myLBs[t].get(i)) 
            myLabel = tk.Label(root, text=selection)
            myLabel.grid()

```
I did forget about the no repeats thing for inserting into listboxes oops lets do that again
Unfortunately earlier thing doesn't work, because we're not adding into each listbox at once (like, fully fill listbox 1, then listbox 2, but instead dropping 1 value into listbox 1, then value 2 into listbox 2, then back to listbox 1)

https://www.pythonforbeginners.com/basics/list-of-lists-in-python#htoc-what-is-a-list-of-lists-in-python 

that didn't help either it is now saturday

### 5.3.2025
I pray for sleep
Ok so I think I've figured out how to do this but in the stupidest way possible
I literally couldn't figure out how to make a list of lists so instead what I've done is still inserted all the values into their listboxes with as many duplicates as they want, but THEN, I pull them all from the listboxes into a new list, which I then subject to the no duplicates code (list(dict.fromkeys(list))), and then I delete everything from the listbox and refill it with the new list
It's so dumb like there's gotta be an easier way but whatever

```
    for t in range(number_of_lbs):
        lbs.clear()
        me = myLBs[t].get(0, tk.END)
        for g in range(len(me)):
            #print(me[g])
            lbs.append(me[g])
        lbs = list(dict.fromkeys(lbs))
        print(lbs)
```
above is working at least for what it's printing
Now we need to clear and refill listboxes
https://stackoverflow.com/questions/48833763/how-to-clear-tkinter-listbox-python 
— this with some finagling worked for clearing

```
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
```
so the above works except now buttons aren't working for some reason
no wait it's bc I'm dumb and still have titles in the listboxes even though those aren't allowed L (that one if statement that I commented out so I could test it and then I forgot I did that)
Now it works
And maybe it's bedtime

Nope scrollbar
https://www.pythontutorial.net/tkinter/tkinter-scrollbar/
ok so it's only at the top

https://stackoverflow.com/questions/19860047/python-tkinter-scrollbar-for-entire-window
this worked, except I had to use grid, not grid, so I had to change everything to grid. Luckily only caused 1 problem, with the start of createButtons where we get rid of labels and buttons

I want to tie it to the mouse too but maybe that's a problem for later bc it's really late

so it'll look a little nicer in the future
https://www.pythontutorial.net/tkinter/tkinter-grid/

Ok, for when I wake up:
Update function, so we can put in ratings and stuff (opens new window?)
May also want to have current adding anime thing have all columns instead of just title and genre?
Make it look better — have most stuff in middle, buttons under in rows

Also for debugging tomorrow:
labels for what we selected aren't getting destroyed (maybe just get rid of — yeah just did that. it doesn't really add much anyway)
so nvmd
OK I DID DISCOVER A DEBUGGING ISSUE — ids above 9 are getting split into 2 and it's only turning 1st number's button — so ex. 10 is read as 1, 0, and so the first button's text changes
UGH
I guess we make it a string and then an integer?

I'm awake
https://www.geeksforgeeks.org/python-extract-numbers-from-string/ I don't know why I didn't do this in the first place
Actually this doesn't work bc it's filling a list 
https://pythonguides.com/extract-numbers-from-a-string-in-python/

```
def changeText2(myText):
    numbers = re.findall(r'\d+', myText)
    print(numbers)
```
Above works

```
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
```
Above works for text change!

Ok, next thing is making it look nicer, and then I'll do the update function if there's time

I saved as test6.py (so I can go back if it's not working, forgot to explain why I keep doing that lol) and then took out everything I'm not using anymore (stuff I commented out, old functions, etc.)

maybe we make top level frame side = LEFT, then have frames within be TOP, with one for filters and one for buttons

that looked like shit

So I switched everything back to grid (at least top level stuff for now)
https://stackoverflow.com/questions/43731784/tkinter-canvas-scrollbar-with-grid used this to get the scrollbar to do what I wanted
Right now, the frame is just in the corner, so now I need to figure out how to fill the window with grid
Ok, changed it so top level stuff is pack and lower level is grid

Ok, I thought a lot and got it looking kind of ok-ish enough. Also I'm in test7.py now oof
I want to try randomizing the anime order now

That was really easy yay https://www.geeksforgeeks.org/python-ways-to-shuffle-a-list/ 
i just put it right above where we make the buttons

Update function is probably for another day, but I do want to try making a new window open
https://www.geeksforgeeks.org/open-a-new-window-with-a-button-in-python-tkinter/
https://stackoverflow.com/questions/43636683/how-to-code-for-a-new-window


ANIME AFTERNOON HAS BEGUN
First issue — text small
I made it bigger but then everything was bigger anyway it works now and it's a fun font (the important stuff)
Second issue — scrollbar doesn't work anymore
https://en.ittrip.xyz/python/tkinter-scrollbar-guide-2

### 5.6.2025
So like idk about the scrollbar and I'm just not going to worry about that rn
I'm going to do the update system 1st bc that's the most important thing

Ok so, what should this look like
Type in an anime name, it pops up, then you can edit it?
Or we see all anime listed out, you select one, it updates?
Here's how to do the backend at least: https://www.sqlitetutorial.net/sqlite-python/update/
But IDK about Gui, I'll have to keep looking I think
Ok looked up "database gui examples" and looked at the images, and it seems like a table/excel looking thing is the best bet

I'm doing the buttons spawning thing again
```
    for i in range(len(animes)):
        column = animes[i]
        print("column:")
        print(column)
        for b in range(len(column)-1):
            #print(column[b])
            var = tk.StringVar(value=f"{column[b]}")
            my_entry.append(tk.Entry(new_window, textvariable=var, width=20))
            my_entry[b].grid(row=myRow, column=myColumn)
            myColumn+=1
        myRow+=1
        myColumn = 0

```
So I've got the above but for some reason it's only making the first row
no wait I think I'm stupid
yeah I changed it from "my_entry[b].grid()" to "my_entry[number_of_values].grid()" with "number_of_values" going up one w/ each appended entry and it works now duh

ok other two things I need to make this work:
1. actual update function (probably use the text in 1st column to find the anime, then do regular .commit thing)
2. scrolling (WAY too many anime lol)

### 5.7.2025
The final day. I'm pissed off for reasons unrelated to this project but that have had effects on my ability to do everything I wanted for this project. I'm quitting musical theatre to instead go on a revenge quest against Christopher Liam Moore, Bridget Kathleen O'Leary, and Isabeau Miller. I'm not going to hurt them physically but I am going to make them regret wronging me.
Ok so I'm being dramatic and also maybe I shouldn't be using documentation as my diary and also it's never smart to write down revenge intentions bc you rarely want them to KNOW your intentions before hand. Still. I'm mad.
I'm trying to focus on doing the things I need to do but all I can do is stew and it's been probably 10 hours at this point, but two days have been ruined by these people. I'm just furious because I put my time and effort into something and they shat on it. And it's not like the thing I was working on was a new way of doing stool samples. Then shitting on it would be fine. But NO. They had to talk in circles about how I'm a terrible ally to the queer community (I am a part of the community) for DARING to take on the DANGEROUS topic of WRITING ABOUT QUEER PEOPLE OH NO.
AHHHHHHHHHHHHHYHHHHHHHYTWHNSFRYYNFGBH V
I hit my keyboard so hard textmate fullscreened


I did some other stuff and technically it is now

### 5.8.2025
The final day for realsies
https://www.sqlitetutorial.net/sqlite-python/update/
https://www.skotechlearn.com/2020/08/get-tkinter-entry-or-text-value-in-python.html

Ok I had something going but I was planning to use ids to help me, and unfortunately we don't really have those
hold up implicit id i'm a genius and should've been using that all along ugh
https://www.sqlitetutorial.net/sqlite-autoincrement/


I used basically all the same code that I used for making the button functions earlier
Made a bunch of tiny errors like I always do (commas in wrong place etc.) but got it working pretty quick — it prints the correct thing when I need it to
Now I need to figure out how to pull from the entry things, which would be easy except we need to know which number it is

Row 0 = 0,1,2,3,4
Row 1 = 5,6,7,8,9
Row 2 = 10,11,12,13,14
Row 3 = 15-19
Row 4 = 20-24
So I think if we multiply the row number by 5 that gives us our first entry box

Tested that and it works
So then we just increment up and it gives us all the columns
This isn't gonna be variable for now so if we ever add a column we're fucked but oh well
Tested "print(my_entry[entryValue].get())" works
Tested "print(my_entry[entryValue+1].get())" works
Tested:
```
    update_statement = "UPDATE anime SET genre=?, episode=?, date=?, rating=? WHERE oid=?"
    cur.execute(update_statement, (my_entry[entryValue+1].get(), my_entry[entryValue+2].get(), my_entry[entryValue+3].get(), my_entry[entryValue+4].get(), number,))
    cur.execute("SELECT * FROM anime WHERE oid=?", (number,))
    yeet=cur.fetchall()
    print(yeet)
```
Worked! Didn't commit just in case but it does in fact work

Ok, scroll time?
https://www.tutorialspoint.com/implementing-a-scrollbar-using-grid-manager-on-a-tkinter-window
I copied exactly what they have and it didn't work
Ah I didn't copy all of it there was more
Ok so now it's all there but it's not the size of the window

I have it kind of working now
```
    frame = ttk.Frame(new_window)
    frame.pack(fill=tk.BOTH, expand=1)
    canvas = tk.Canvas(frame)
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    content_frame = ttk.Frame(canvas)
    content_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=content_frame, anchor="nw")
    canvas.pack(fill=tk.Y, expand=1)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

```
I'm playing around with the canvas and scrollbar packs rn. Basically, the canvas one isn't actually showing everything
https://pypi.org/project/pynput/
https://pytutorial.com/master-mouse-scrolling-with-pynputmousescroll-in-python/
praying rn
yeah nothing and idk enough about this to fix it rn
ok so i didn't have mouse installed, then i installed, but now textmate doesn't like some part of it ("unsupported platform 'Darwin'")
seems like its a mac issue, kinda shocked this is the first of those i've run into

It's really late so I think when I wake up I'm gonna look at this:
https://www.youtube.com/watch?v=0WafQCaok6g

good fuckin morning
the video didn't work ahhhhhhhhhh
I got it though — I used the same code I had yesterday and just changed the canvas.pack from fill=tk.Y to fill=tk.BOTH and it works

This was just doing the scrollbar for the update window, I still need it for the main window

Also I'm going to make it so changes commit now
Wait first some labels
Ok got that so the update window says which thing is which now

also I'm in test9 now, when I'm done I'll save as "animenight" or something

ok I got scrollbar working for main window — copied what I did for the update window and then added 3 additional frames for the 3 things I have

I'm now looking back at the top to see what else I wanted to do

ok so one thing is being able to choose a range of dates or ratings, but since we have the listboxes, even though that means clicking each individual one, i think we're good there

I'd said I wanted a sidebar but I kinda like the design I have now instead

I also technically don't have a reshuffle button, but it will automatically reshuffle everytime we search again so that's fine.

I guess the only thing left is making it look cool

https://python-tutorials.in/tkinter-themes/
I get how that works now

I installed ttkthemes https://ttkthemes.readthedocs.io/en/latest/installation.html
https://ttkthemes.readthedocs.io/en/latest/example.html

Actually I don't care I'm making my powerpoint
Ok, just realized I fucked up and forgot to make it so we can actually create buttons from any listbox — have to check which it is and filter for correct column

it's this line when making buttons: "if selection[g] != None and selection[g] == columns[myColumn]:"
"myColumn" is set to 0, so we need to set it to the correct column by the listbox

Oy
check if selection is null, have additional number if not null add number to other list and increment myColumn that way

ok also realizing you can't select from multiple lbs at once
jeez I really screwed this one up

https://stackoverflow.com/questions/756662/how-to-select-at-the-same-time-from-two-listbox

```
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
```
That prints what I need it to

```
    for g in range(len(selection)):
        for i in range(len(animes)):
            columns = animes[i]
            for f in range(len(selLb)):
                myColumn = selLb[f] + 1
                print(selection[g])
                print(columns[myColumn])
                if selection[g] != None and selection[g] == columns[myColumn]:
                    print("i live!!!!")
                    number_of_btns += 1
                    cur.execute("UPDATE anime SET id=? WHERE title=?", (number_of_btns, columns[0],))
                    con.commit()
                    btns.append(tk.Button(buttonFrame, width="25", text=str(number_of_btns + 1) + " " + columns[myColumn], command=lambda c=number_of_btns: changeText2(btns[c].cget("text"))))
                    if column_number > 1:
                        row_number += 1
                        column_number = 0
                        btns[number_of_btns].config(font=("kindergarten", 44))
                        btns[number_of_btns].grid(row=row_number, column=column_number)
                        column_number += 1
                else:
                    print(" ")
    cur.close()  
```
So it's not actually making the buttons (which is why I've got it printing "i live!!!!!!" bc I thought maybe the if statements were broken or something, but it is printing that)

oh I think I know what happened
When I added the extra for loop for the selLb, I had to indent everything again and I think I indented some stuff too much

LUCKILY I HAVE a billion copies of previous versions so I can check what the indentation was supposed to be

It is working now
HOWEVER, it's not additive — so it's creating the buttons if they fit ANY of the listbox selections as opposed to if they fit ALL of the listbox selections

https://pytutorial.com/python-remove-all-but-specific-elements-from-list/ THIS WAS COMPLETELY USELESS

I did it on my own with a bool

```
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
			#(do all the code for making the buttons)
```
Ok so I added in ratings for all the anime
Ummmm realized there's an issue which is they're in the order they were input, not the order of their values

GOT IT WITH ONE MINUTE TO SPARE LET'S GOOOOOO

```
    lbs = []
    list_str = []
    list_int = []
    for t in range(number_of_lbs):
        lbs.clear()
        me = myLBs[t].get(0, tk.END)
        myLBs[t].delete(0, tk.END)
        for g in range(len(me)):
            if me[g] != "None":
                lbs.append(me[g])
        lbs = list(dict.fromkeys(lbs))
        print(lbs)
        lbs.sort()
        for g in range(len(lbs)):
            myLBs[t].insert(tk.END, lbs[g])
```





