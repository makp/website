from flask import Flask, render_template, redirect
import datetime


app = Flask(__name__)
# , template_folder = 'pages'


date_today = datetime.datetime.now()  # .strftime('%Y, %m, %d')
week_today = date_today.isocalendar()[1]
week_first = datetime.date(2021, 8, 30).isocalendar()[1]
week_jump = (week_today - week_first) + 1
# week_jump = 2
id_jump = 'Week' + str(week_jump)


# use decorators to map a URL to a function
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/pubs')
def publications():
    return render_template('publications.html')


@app.route('/research')
def research():
    return render_template('research.html')


@app.route('/teaching')
def teaching():
    return render_template('teaching.html')


@app.route('/schedule1')
def schedule1():
    template_values = {
        'title': "Environmental Ethics",
        'number': "PHIL255",
        'semester': "Spring 2022",
        'source': 'includes/schedule_s22_phil255.html',
        'id_jump': id_jump,
        'week_jump': week_jump}
    return render_template('schedule.html', **template_values)


@app.route('/schedule2')
def schedule2():
    template_values = {
        'title': "What Makes Us Moral",
        'number': "PHIL342",
        'semester': "Fall 2022",
        'source': 'includes/schedule_f22_phil342.html',
        'id_jump': id_jump,
        'week_jump': week_jump}
    return render_template('schedule.html', **template_values)


@app.route('/schedule3')
def schedule3():
    template_values = {
        'title': "Sex, Death, & Outlaws",
        'number': "PHIL212",
        'semester': "Spring 2020",
        'source': 'includes/schedule_s20_phil212.html',
        'id_jump': id_jump,
        'week_jump': week_jump
    }
    return render_template('schedule.html', **template_values)


@app.route('/schedule4')
def schedule4():
    template_values = {
        'title': "The Evolution of Complexity",
        'number': "PHIL460",
        'semester': "Spring 2019",
        'source': 'includes/schedule_s19_phil460.html',
        'id_jump': id_jump,
        'week_jump': week_jump
    }
    return render_template('schedule.html', **template_values)


@app.route('/schedule5')
def schedule5():
    template_values = {
        'title': "Environmental Ethics",
        'number': "PHIL255",
        'semester': "Fall 2022",
        'source': 'includes/schedule_f22_phil255.html',
        'id_jump': id_jump,
        'week_jump': week_jump
    }
    return render_template('schedule.html', **template_values)


@app.route('/schedule6')
def schedule6():
    template_values = {
        'title': "What Makes Us Moral",
        'number': "PHIL342",
        'semester': "Spring 2022",
        'source': 'includes/schedule_s22_phil342.html',
        'id_jump': id_jump,
        'week_jump': week_jump}
    return render_template('schedule.html', **template_values)


@app.route('/extra')
def slides():
    return redirect("https://tu-my.sharepoint.com/:f:/g/personal/mpedroso_towson_edu/Ep8gC8AZpFJAi_Dyw6hA5SsBbWs1NxlaKtJIvpLBVIl5KQ?e=6Xqu1w")

# start the server with the 'run()' method
if __name__ == "__main__":
    app.run(debug=True, port=8080)
