# Proposal

## Working Title
"Anime Night's Gonna Be Lit!!!!"

## Elevator Pitch
My project is a system for picking anime for anime night with my friends, using SQLite and Python.

## 3 Resources
* *Think Python, Second Edition* by Allen B. Downey (plus supplemental material)
	* Learning python
* Stack Overflow
	* Debugging help
* MyAnimeList
	* Example database
* https://docs.python.org/3/library/sqlite3.html
	* For help w/ python accessing sqlite
* Your 02SQL stuff
	* Also for help w/ SQL

## Summary
*In a paragraph or more, detail your project. What will your software do? What features will it have? How will it be executed?*
My friends and I hang out and watch anime. We've been doing this for a long time, and recently I "gamified" it, so we have to choose anime based on genre without knowing what the anime will be. A few weeks ago, we had a couple new people over, and unfortunately, all of the anime we picked were not only bad, but weird (especially for a first timer). Our current system has no way of sorting the anime. So, what I want to do is set up a system for us — 
* Database
	* ALL anime we've watched/are watching
	* Paramaters:
		* Current episode
		* When we last watched it
		* Genre
		* Rating (out of 10)
		* Sortable by multiple filters
		* Easy to add new filters, change or combine filters
* Interface
	* Show specified number of "cards" with one or more filters visible (rating, date, genre, etc.)
		* When clicked on, flip to reveal anime
		* Ability to stay open, showing what we've watched last night, or reshuffle
	* Sidebar
		* Filters (include exclude)
		* Date range
		* Rating range
		* Reshuffle button
		* Add new
			* Way to add new anime w/o having to code it in

I'll be using sqlite and python (already read the assigned chapters).

## This project will not overlap with any other classes

## Outcomes
_In the world of software, most everything takes longer to implement than you expect. And so it's not uncommon to accomplish less in a fixed amount of time than you hope.
In a sentence (or list of features), define a GOOD outcome for your final project. I.e., what WILL you accomplish no matter what?
TODO
In a sentence (or list of features), define a BETTER outcome for your final project. I.e., what do you THINK you can accomplish before the final project's deadline?
TODO
In a sentence (or list of features), define a BEST outcome for your final project. I.e., what do you HOPE to accomplish before the final project's deadline?_

#### Ideal
All of the features outlined under "Summary"

#### Realistic
The "Database" features under "Summary," as well as a sketch of/plan for the "Interface," but not fully realized or connected

#### Even More Realistic
Only the "Database" portion outlined under "Summary"

## Calendar
*In a paragraph or more, outline your next steps WITH A SPECIFIC CALENDAR. What new skills will you need to acquire? What topics will you need to research?*

### My Beautiful Calendar
#### Key
**Bold = done**
*Italics = changed mind*

* 4/5
	* **Make database, get 2 anime in for testing**
	* **Connect python and sqlite**
		* **Figure out how to get user input with python**
		* **Figure out how to get python user input into database**
	* **Start figuring out interface**
* Week of 4/13:
	* Continue with interface (definitely hardest part)
		* Figure out buttons (for filtering)
		* Sliders (for time ranges, rating ranges)
	* This is a really busy week bc I'm putting on a show so I'm not putting anything else down
* Week of 4/20:
	* Recover from show lmao
	* Connect interface and database
* Week of 4/27:
	* Finish anything leftover from previous week
* Week of 5/4:
	* Make it look nice
* Week of 4/11:
	* Worry about other finals, hopefully
	
