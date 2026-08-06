
#Imports Flask functions for crating webpages and handeling user input
from flask import Flask, render_template, request
#Imports math for advanced calculations in the savings calculator 
import math
app= Flask(__name__)

@app.route('/')
def home():
    # Displays the home page when the user visits the website.
    return render_template('home.html') 

@app.route('/information', methods=['GET', 'POST'])
def information():

    # Displays an article based on the selected number and updates it with post requests
    boxtitle = 'Click a number to read an article or click the quiz button to start the quiz'
    boxtext = ''

    if request.method == 'POST':
         # Recives the selected article number from the user input.
        number = request.form.get('number', '').strip()
        # Uses conditional statements to display the matching article content.
        if number == "1":
            boxtitle = "Budgeting basics - income and expense."
            boxtext = "Budgeting means planning how you use your money. It’s about knowing how much you earn and deciding in advance how much you can spend and save. A simple budget helps you avoid running out of money and gives you a clear overview of your finances."
        elif number == "2":
            boxtitle = "Income smoothing helps with irregular income"
            boxtext = "If your income changes from week to week you could try Income Smoothing. It works by calculating an average income and base your spending on that. You can check out the Income-Smoothing-Calculator to find out what might work for you."
        elif number == "3":
            boxtitle = "Avoid overspending by tracking habits."
            boxtext = "Overspending often happens without noticing. Small daily expenses add up quickly. Becoming aware of your spending habits is the first step to controlling them and making better financial decisions."
        elif number == "4":
            boxtitle = "Track every dollar you spend."
            boxtext = "Tracking your expenses means writing down or recording everything you spend. This helps you understand where your money goes and identify areas where you can cut back."
        elif number == "5":
            boxtitle = "Saving regularly builds financial security."
            boxtext = "Saving regularly, even small amounts, builds financial stability over time. It helps you prepare for unexpected expenses and reduces financial stress in the long run"
        elif number == "6":
            boxtitle = "Set clear financial goals."
            boxtext = "Saving regularly, even small amounts, builds financial stability over time. It helps you prepare for unexpected expenses and reduces financial stress in the long run."
        elif number == "7":
            boxtitle = "Consistency is key in budgeting."
            boxtext = "Creating a budget is one thing, but sticking to it is what really matters. Consistency helps you build better habits and stay in control of your finances over time."
        elif number == "8":
            boxtitle = "Control your money, don't let it control you."
            boxtext = "Being in control of your money means making intentional decisions about spending and saving. When you understand your finances, you feel more confident and less stressed about money."
        else:
            boxtitle = 'Click a number to read an article or click the quiz button to start the quiz'
            boxtext = ''

# sends the text to the webpage template to be displayed on the website
    return render_template( 
        'info.html',
        boxtitle=boxtitle,
        boxtext=boxtext
    )

@app.route('/goal', methods=['GET', 'POST'])

def goal():
#Calculates the missing value depending on which input field is empty.

    goal = ''
    amount = ''
    weeks = ''
    interest = 0.001
    account_type = 'everyday'
    error = ''

    # Recieves the input values submitted by the user through the form.
    # Uses compound interest formulas based on the selected account type.
    if request.method == 'POST': 
        goal_text = request.form.get('goal', '').strip()
        amount_text = request.form.get('amount', '').strip()
        weeks_text = request.form.get('weeks', '').strip()
        account_type = request.form.get('account_type', 'everyday').strip()

        # Sets the interest rate based on the selected account type.
        if account_type == "everyday":
            interest = 0.001   
        elif account_type == "savings":
            interest = 0.015   
        elif account_type == "deposit":
            interest = 0.03

        # Converts the annual interest rate to a weekly interest rate
        interest = interest / 52

        # Converts the input values to float or int if they are not empty, otherwise sets them to empty string
        goal = float(goal_text) if goal_text else ''
        amount = float(amount_text) if amount_text else ''
        weeks = int(weeks_text) if weeks_text else ''

        # Calculates the missing value based on the other two values and the interest rate of the selected account type
        # Calculates only the missing value because the user leaves one input field empty.
        if goal == '' and amount != '' and weeks != '':
            goal = amount * (((1 + interest) ** weeks) - 1) / interest
            goal = round(goal, 2)

        elif amount == '' and goal != '' and weeks != '':
            amount = (goal * interest) / (((1 + interest) ** weeks) - 1)
            amount = round(amount, 2)

        elif weeks == '' and goal != '' and amount != '':
            weeks = math.log((goal * interest / amount) + 1) / math.log(1 + interest)
            weeks = math.ceil(weeks)

    else:
        
        goal = ''
        amount = ''
        weeks = ''
        error = ''

    return render_template(
        'goal.html',
        goal=goal,
        amount=amount,
        weeks=weeks,
        interest=interest,
        account_type=account_type,
        error=error
    )

@app.route('/income', methods=['GET', 'POST'])
def income():
    # Calculates a recommended weekly spending amount from irregular income.
    # Analyses income changes and provides stability feedback.
    week1 = 0
    week2 = 0
    week3 = 0
    week4 = 0
    amount = '_____'
    stability = '_____'

    if request.method == 'POST':
        # receives the users weekly income inputs from the form 
        week1_text = request.form.get('week1', '').strip()
        week2_text = request.form.get('week2', '').strip()
        week3_text = request.form.get('week3', '').strip()
        week4_text = request.form.get('week4', '').strip()

        #coverts input into integers 
        #empty inputs are treatet as zero income 
        week1 = int(week1_text) if week1_text else 0
        week2 = int(week2_text) if week2_text else 0
        week3 = int(week3_text) if week3_text else 0
        week4 = int(week4_text) if week4_text else 0

        # Calculates the recommended spending amount using 85% of the average income.
        # The remaining 15% can be used for saving.
        totalincome = week1 + week2 + week3 + week4
        amount = round((totalincome / 4) * 0.85, 2)

    #stores weekly income in a list so changes can be compared 
    incomes = [week1, week2, week3, week4]
    changes = []

    # Calculates the difference between consecutive weeks to measure income changes.
    # The average change is used to determine income stability. 
    for i in range(1, len(incomes)):
        difference = abs(incomes[i] - incomes[i-1])
        changes.append(difference)

    #Finds the average income change to determine stability.
    average_change = sum(changes) / len(changes) if changes else 0

    #provides feedback based on the calculated stability level.
    if average_change < 50:
        stability = "Your income is stable. You can rely on your earnings and plan your spending confidently."
    elif average_change < 150:
        stability = "Your income is moderately stable. Consider saving extra money during higher income weeks."
    else:
        stability = "Your income is unstable. We recommend building an emergency buffer and avoiding relying on your highest income weeks."
    

    return render_template(
        'income.html',
        week1=week1,
        week2=week2,
        week3=week3,
        week4=week4, 
        amount=amount,
        stability=stability)

@app.route('/quiz')
def quiz():
    #Displayes the quiz webpage where users can test their budgeting knowledge. 
    #Quiz functionality is handled separately in quiz.js.
    return render_template('quiz.html')

if __name__ == "__main__":
    #starts the Flask application when this file is run directly
    app.run(debug=True, port=3000)