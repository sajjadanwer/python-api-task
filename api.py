from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/datetime')
def date_time():
    current_datetime = datetime.now()
    return f"Current Date and Time: {current_datetime.strftime('%d-%m-%Y')}"
    
if __name__ == '__main__':
    app.run()
