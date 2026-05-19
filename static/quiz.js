
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

function showQuestion() {
    document.getElementById("question").innerHTML =
        questions[currentQuestion].q;
}

showQuestion();

