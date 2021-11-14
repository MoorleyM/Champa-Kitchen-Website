from flask import Flask, render_template
from _datetime import datetime
from menu import starterMenu, traditionalMenu, soup_salad, pho_noodle, curry, main_course, noodle_lover
from menu import vegetarian, side_dishes, hot_drinks, cold_drinks, lunch_menu

app = Flask(__name__)


@app.route("/")
def home():
    current_year = datetime.now().year
    return render_template("index.html", year=current_year)


@app.route("/Menu")
def menu():
    current_year = datetime.now().year
    s_menu = starterMenu
    t_menu = traditionalMenu
    ss_menu = soup_salad
    pho_menu = pho_noodle
    c_menu = curry
    m_menu = main_course
    n_menu = noodle_lover
    v_menu = vegetarian
    si_menu = side_dishes
    h_drinks = hot_drinks
    c_drinks = cold_drinks
    l_menu = lunch_menu
    return render_template("menu.html", year=current_year, s_items=s_menu, t_items=t_menu, ss_items=ss_menu,
                           pho_items=pho_menu, c_items=c_menu, m_items=m_menu, n_items=n_menu, v_items=v_menu,
                           si_items=si_menu, h_items=h_drinks, co_items=c_drinks, l_items=l_menu)


@app.route("/Info")
def contact():
    current_year = datetime.now().year
    return render_template("info.html", year=current_year)


@app.route("/Gallery")
def gallery():
    current_year = datetime.now().year
    return render_template("gallery.html", year=current_year)


if __name__ == "__main__":
    app.run(debug=True)
