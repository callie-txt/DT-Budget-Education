from flask import Flask, render_template, request

app= Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/information')
def information():
    return render_template('info.html')

@app.route('/goal', methods=['GET', 'POST'])
def goal():
    goal = ''
    amount = ''
    weeks = ''

    if request.method == 'POST':
        goal_text = request.form.get('goal', '').strip()
        amount_text = request.form.get('amount', '').strip()
        weeks_text = request.form.get('weeks', '').strip()

        goal = int(goal_text) if goal_text else ''
        amount = int(amount_text) if amount_text else ''
        weeks = int(weeks_text) if weeks_text else ''

        if goal == '' and amount != '' and weeks != '':
            goal = amount * weeks
        elif amount == '' and goal != '' and weeks != '':
            amount = goal // weeks
        elif weeks == '' and goal != '' and amount != '':
            weeks = goal // amount
        else:
            goal = ''
            amount = ''
            weeks = ''

    return render_template(
        'goal.html',
        goal=goal,
        amount=amount,
        weeks=weeks,
    )

@app.route('/income', methods=['GET', 'POST'])
def income():
    week1 = ''
    week2 = ''
    week3 = ''
    week4 = ''
    amount = '_____'
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

    return render_template(
        'income.html',
        week1=week1,
        week2=week2,
        week3=week3,
        week4=week4, 
        amount=amount,)

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

if __name__ == "__main__":
    app.run(debug=True, port=3000)