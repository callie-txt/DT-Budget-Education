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

@app.route('/income')
def income():
    return render_template('income.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

if __name__ == "__main__":
    app.run(debug=True)