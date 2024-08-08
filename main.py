from flask import Flask, redirect, render_template

from courses_info import CURRENT_SEMESTER, semesters

app = Flask(__name__)


# FIXME: Jump to current week function
# def calculate_week_jump():
#     date_today = datetime.datetime.now()
#     week_today = date_today.isocalendar()[1]
#     week_first = datetime.date(2021, 8, 30).isocalendar()[1]
#     return (week_today - week_first) + 1
# week_jump = calculate_week_jump()
# id_jump = 'Week' + str(week_jump)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/pubs")
def publications():
    return render_template("publications.html")


@app.route("/research")
def research():
    return render_template("research.html")


@app.route("/teaching")
def teaching():
    current_semester = CURRENT_SEMESTER.replace("_", " ")
    courses_info = semesters[CURRENT_SEMESTER]
    return render_template(
        "teaching.html", semester=current_semester, courses=courses_info
    )


@app.route("/schedule/<int:schedule_id>")
def schedule(schedule_id):
    schedule_id = schedule_id - 1
    current_schedules = semesters[CURRENT_SEMESTER]
    schedules = []
    for course_number, course_info in current_schedules.items():
        schedules.append(
            {
                "title": course_info["course_name"],
                "number": course_number,
                "semester": CURRENT_SEMESTER.replace("_", " "),
                "source": course_info["schedule_html"],
            }
        )
    template_values = schedules[schedule_id]
    # template_values['id_jump'] = id_jump
    # template_values['week_jump'] = week_jump
    return render_template("schedule.html", **template_values)


@app.route("/extra")
def slides():
    return redirect(
        "https://tu-my.sharepoint.com/:f:/g/personal/mpedroso_towson_edu/"
        "Ep8gC8AZpFJAi_Dyw6hA5SsB4z21Ziu98-iGHnd6zdJXwQ?e=cySgLo"
    )


# start the server with the 'run()' method
if __name__ == "__main__":
    app.run(debug=True, port=8080)
