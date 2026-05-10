function show(num) {

    if (num === 1) {
        document.getElementById("boxtitle").innerText = "Budgeting basics - income and expense.";
        document.getElementById("boxtext").innerText = "Budgeting means planning how you use your money. It’s about knowing how much you earn and deciding in advance how much you can spend and save. A simple budget helps you avoid running out of money and gives you a clear overview of your finances.";
    }

    if (num === 2) {
        document.getElementById("boxtitle").innerText = "Income smoothing helps with irregular income";
        document.getElementById("boxtext").innerText = "If your income changes from week to week you could try Income Smoothing. It works by calculating an average income and base your spending on that. You can check out the Income-Smoothing-Calculator to find out what might work for you.";
    }

    if (num === 3) {
        document.getElementById("boxtitle").innerText = "Avoid overspending by tracking habits.";
        document.getElementById("boxtext").innerText = "Overspending often happens without noticing. Small daily expenses add up quickly. Becoming aware of your spending habits is the first step to controlling them and making better financial decisions.";
    }

    if (num === 4) {
        document.getElementById("boxtitle").innerText = "Track every dollar you spend.";
        document.getElementById("boxtext").innerText = "Tracking your expenses means writing down or recording everything you spend. This helps you understand where your money goes and identify areas where you can cut back.";
    }

    if (num === 5) {
        document.getElementById("boxtitle").innerText = "Saving regularly builds financial security.";
        document.getElementById("boxtext").innerText = "Saving regularly, even small amounts, builds financial stability over time. It helps you prepare for unexpected expenses and reduces financial stress in the long run.";
    }

    if (num === 6) {
        document.getElementById("boxtitle").innerText = "Set clear financial goals.";
        document.getElementById("boxtext").innerText = "Financial goals give you direction. Whether it’s saving for something specific or building long-term security, having a goal makes it easier to stay motivated and disciplined with your money.";
    }
   
    if (num === 7) {
        document.getElementById("boxtitle").innerText = "Consistency is key in budgeting.";
        document.getElementById("boxtext").innerText = "Creating a budget is one thing, but sticking to it is what really matters. Consistency helps you build better habits and stay in control of your finances over time.";
    }

    if (num === 8) {
        document.getElementById("boxtitle").innerText = "Control your money, don't let it control you.";
        document.getElementById("boxtext").innerText = "Being in control of your money means making intentional decisions about spending and saving. When you understand your finances, you feel more confident and less stressed about money.";
    }

}