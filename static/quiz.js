
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

let currentQuestion = 0;
let wrongQuestions = [];
const totalQuestions = questions.length;

function showQuestion() {
    document.getElementById("question-counter").innerHTML = `${currentQuestion + 1}/${totalQuestions}`;
    document.getElementById("question").innerHTML =
        questions[currentQuestion].q;
}

showQuestion();

function answer(userAnswer) {
    const correct = questions[currentQuestion].a;
    if (userAnswer !== correct) {
        wrongQuestions.push(currentQuestion); 
    }

    currentQuestion++;

    if (currentQuestion < questions.length) {
        showQuestion();
    } else {
        let resultText= " ";

        if (wrongQuestions.length > 0) {
            resultText += "We recommend the articles: " + wrongQuestions.map(q => q + 1).join(", ");
        } else {
            resultText += "No recommended articles.";
        }
        document.getElementById("question").innerHTML = resultText;
    }
}
