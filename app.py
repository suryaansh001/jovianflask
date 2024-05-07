from flask import Flask, render_template

app = Flask(__name__)
JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'salary': 'Rs.10,00,000'
    },
    {
        'id': 2,
        'title': 'Flask Developer',
        'salary': 'Rs.15,00,000'  
    },
    {
        'id': 3,
        'title': 'Data Scientist',
        'salary': 'Rs.20,00,000'
    }
]


@app.route("/")  # empty route means homepage and is denoted by "/"
def hello_world():
    return render_template('home.html', jobs=JOBS)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
