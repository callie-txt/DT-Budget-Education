
const questions = [
    { q: "Do you know what budgeting is?", a: "yes" },
    { q: "Is HTML a programming language?", a: "no" },
    { q: "Is CSS used for styling?", a: "yes" },
    { q: "Does 2 + 2 = 5?", a: "no" },
    { q: "Is water dry?", a: "no" },
    { q: "Is Earth a planet?", a: "yes" },
    { q: "Does the sun rise in the west?", a: "no" }
];

let currentQuestion = 0;
let wrongQuestions = [];

function showQuestion() {
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
            resultText += "We recommend the articles: " + wrongQuestions.join(", ");
        } else {
            resultText += "No recommended articles.";
        }

        document.getElementById("question").innerHTML = resultText;
    }
}
