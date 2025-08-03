from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    today = datetime.now()
    birthday = datetime(2025, 8, 8, 12, 0, 0)  # 8 August, 12 PM
    days_left = (birthday - today).days
    hours_left = (birthday - today).seconds // 3600
    show_locked = today < birthday

    return render_template('index.html', 
                           days_left=days_left,
                           hours_left=hours_left,
                           show_locked=show_locked,
                           today_date=today)

if __name__ == '__main__':
    app.run(debug=True)
