from flask import render_template
import datetime

app = Flask(__name__)

# Define the two kids
# Adri is even week, T is odd in 2024
kids = ["Adrianna", "Travis"]

@app.route('/')
def home():
    # Get the current week number
    week_number = datetime.date.today().isocalendar()[1]
    
    # If the week number is even, select the first kid, otherwise select the second
    kid = kids[week_number % 2]
    
    #return f"{kid} needs to check the trash and recycling today."
    return render_template('trash_template.html', kid=kid)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)
