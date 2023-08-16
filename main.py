from flask import Flask, render_template, redirect
import datetime


app = Flask(__name__)


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


@app.route('/schedule/<int:schedule_id>')
def schedule(schedule_id):
    schedules = [
        {"title": "Introduction to Ethics",
         'number': "PHIL103",
         'semester': "Fall 2023",
         'source': 'includes/schedule_s23_phil255.html'},
        {'title': "",
         'number': "PHILXXX",
         'semester': "Fall 2023",
         'source': 'includes/schedule_s23_phil255.html'},
    ]
    template_values = schedules[schedule_id]
    template_values['id_jump'] = id_jump
    template_values['week_jump'] = week_jump
    return render_template('schedule.html', **template_values)


@app.route('/extra')
def slides():
    return redirect("https://tu-my.sharepoint.com/:f:/g/personal/mpedroso_towson_edu/Ep8gC8AZpFJAi_Dyw6hA5SsB4z21Ziu98-iGHnd6zdJXwQ?e=cySgLo")

# start the server with the 'run()' method
if __name__ == "__main__":
    app.run(debug=True, port=8080)
