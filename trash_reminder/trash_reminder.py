from flask import render_template
from flask import Flask
import datetime

app = Flask(__name__)

# Define the two kids
# Adri is even week, T is odd in 2024
kids = ["Adrianna", "Travis"]

@app.route('/')
def home():
    # Get the current week number
    week_number = datetime.date.today().isocalendar()[1]

## Added 2025-0816
    # get the day of the week
    day_of_week = datetime.date.today().isocalendar()[2]
    
    # If the week number is even, select the first kid, otherwise select the second
    kid = kids[week_number % 2]
    
    # If the day of the week is not Monday, return a message indicating that it's not trash day
    if day_of_week != 1:  # 1 corresponds to Monday

        #return f"{kid} needs to check the trash and recycling today."
        return render_template('trash_template.html', kid=kid)
    else:
        # If it is Monday, return a message indicating that it's trash day
        return render_template('trash_template_Monday.html', kid=kid, trash_day=True)
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)
