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











