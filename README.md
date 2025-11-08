This is where we will explain how to run this project from the git side
this will never be read by someone who accesses are website
right now it is setup in such a way as to only launch to a local host from
your computer this is beacuse I don't know how to do it anyother way

Anyway... right now to set up and run the program you need to 

git clone *this directory*
bash ./setup_linux.sh

then if you want to run the website
run.sh

Notes:
All requirments to run should be handled by run.sh if you add a new condition to run update run.sh
If you add a new python package and in the requirements.txt
The base template shouldn't need to be change, look to example.html for how to make a new page

Todo
A database of some kind to store data (SQL, or SQLite, or something similar)
Write all files, methods, and functions nesscary for someone who knows nothing about them to be able to use them(Functionallity like add a new entry to a row, drop an entry, ect)
Find some web hosing servace so project can run indepently of a persons computer
Add nav bar to base.html (So a user to locate other pages)
Adjust style.css so website dosen't look like garbage

(Website is very bearbones right now but once we know what functionallity we want i can add more stuff)

