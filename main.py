from flask import Flask, render_template, request
import math
app= Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/information', methods=['GET', 'POST'])
def information():
    boxtitle = 'Click a number to read an article or click the quiz button to start the quiz'
    boxtext = ''

    if request.method == 'POST':
        number = request.form.get('number', '').strip()
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
            boxtitle = 'Click a nuber to read an article or click the quiz button to start the quiz'
            boxtext = ''

    return render_template(
        'info.html',
        boxtitle=boxtitle,
        boxtext=boxtext
    )

@app.route('/goal', methods=['GET', 'POST'])

def goal():

    goal = ''
    amount = ''
    weeks = ''
    interest = 0.001
    account_type = 'everyday'
    error = ''

    if request.method == 'POST':
        goal_text = request.form.get('goal', '').strip()
        amount_text = request.form.get('amount', '').strip()
        weeks_text = request.form.get('weeks', '').strip()
        account_type = request.form.get('account_type', 'everyday').strip()

        if account_type == "everyday":
            interest = 0.001   
        elif account_type == "savings":
            interest = 0.015   
        elif account_type == "deposit":
            interest = 0.03
        
        interest = interest / 52

        goal = float(goal_text) if goal_text else ''
        amount = float(amount_text) if amount_text else ''
        weeks = int(weeks_text) if weeks_text else ''

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
    week1 = 0
    week2 = 0
    week3 = 0
    week4 = 0
    amount = '_____'
    stability = '_____'

    if request.method == 'POST':
        week1_text = request.form.get('week1', '').strip()
        week2_text = request.form.get('week2', '').strip()
        week3_text = request.form.get('week3', '').strip()
        week4_text = request.form.get('week4', '').strip()

        week1 = int(week1_text) if week1_text else 0
        week2 = int(week2_text) if week2_text else 0
        week3 = int(week3_text) if week3_text else 0
        week4 = int(week4_text) if week4_text else 0

        totalincome = week1 + week2 + week3 + week4
        amount = round((totalincome / 4) * 0.85, 2)

    incomes = [week1, week2, week3, week4]
    changes = []

    for i in range(1, len(incomes)):
        difference = abs(incomes[i] - incomes[i-1])
        changes.append(difference)
    
    average_change = sum(changes) / len(changes) if changes else 0

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
    return render_template('quiz.html')

if __name__ == "__main__":
    app.run(debug=True, port=3000)