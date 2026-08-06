
const questions = [
    { q: "Do you know what budgeting is?", a: "yes" },
    { q: "Is your income irregular?", a: "no" },
    { q: "Do you feel like you spend too much money?", a: "no" },
    { q: "Do you know where your money goes?", a: "yes" },
    { q: "Do you currently save money?", a: "yes" },
    { q: "Do you have a specific savings goal?", a: "yes" },
    { q: "Do you sometimes run out of money?", a: "no" },
    { q: "Do you plan your spending in advance?", a: "yes" },
];

// Stores the current position in the quiz and keeps track of questions answered incorrectly.
let currentQuestion = 0;
let wrongQuestions = [];
const totalQuestions = questions.length;

function showQuestion() {
    // Displays the current question and updates the buttons shown to the user.
    document.getElementById("question-counter").innerHTML = `${currentQuestion + 1}/${totalQuestions}`;
    document.getElementById("question").innerHTML =
        questions[currentQuestion].q;
    document.getElementById("yes-button").style.display = "block";
    document.getElementById("no-button").style.display = "block";
    document.getElementById("info-button").style.display = "none";
}

showQuestion();

function answer(userAnswer) {
    // Checks whether the user's answer matches the correct answer
    // and stores the question number if the answer is incorrect.
    const correct = questions[currentQuestion].a;
    if (userAnswer !== correct) {
        wrongQuestions.push(currentQuestion); 
    }

    currentQuestion++;

    // Displays the next question if there are questions remaining.
    if (currentQuestion < questions.length) {
        showQuestion();
    } else {

        // Creates a recommendation message based on the questions
        // the user answered incorrectly.
        let resultText= " ";

        if (wrongQuestions.length > 0) {
            resultText += "We recommend the articles: " + wrongQuestions.map(q => q + 1).join(", ");
        } else {
            resultText += "No recommended articles.";
        }
        
        // Replaces the quiz with the final result and shows the information button.
        document.getElementById("question").innerHTML = resultText;
        document.getElementById("question-counter").innerHTML = `${totalQuestions}/${totalQuestions}`;
        document.getElementById("info-button").style.display = "flex";
    }
}
