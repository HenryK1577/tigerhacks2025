<h1>Scripts</h1>

*Scripts are relational and can only be run in the scripts directory after they have run they put you back in the top directory*

<h3>setup_linux.sh</h3>
This is a bash script that sets up everything this program needs to run you should exicute it when you clone the directory from git


<h3>clean.sh</h3>
This is is a function that gives you a view of what the git hub repo will look like. This isn't nessicary to run because all the irrelivant files will be ignored by the .gitignore however I like how clean it makes the code lool.

>------------

``` bash
# Replace my_script 
cd scripts
chmod +x my_script.sh
. my_script.sh
```

>------------

<h1>How to run severs</h1>
Create two bash terminals

In the first

``` bash
cd flask_backend
source .venv/bin/activate
flask --app app.py run --debug
```

In the second

``` bash
cd react_frontend
npm run dev
```
