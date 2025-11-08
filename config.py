from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)



# Website string information




def init_base_html():
    # Navbar
    app_name = "app_name placerholder"
    logo_path = "/static/images/waze.ico"
    search_name = "Search"
    info_url = url_for('home')
    search_url = url_for('home')

    return render_template('base.html', app_name=app_name,
                            logo_path=logo_path, 
                            search_name=search_name, 
                            info_url=info_url, 
                            search_url=search_url)