const questionInput = document.getElementById("question");

const sqlOutput = document.getElementById("sql-output");

const sqlType = document.getElementById("sql-type");

const difficulty = document.getElementById("difficulty");

const explanation = document.getElementById("explanation");

document.querySelectorAll(".example").forEach(button => {

    button.addEventListener("click", () => {

        questionInput.value = button.innerText;

    });

});

document.getElementById("copy-btn").addEventListener("click", () => {

    navigator.clipboard.writeText(sqlOutput.innerText);

    const button = document.getElementById("copy-btn");

    button.innerText = "Copied";

    setTimeout(() => {

        button.innerText = "Copy SQL";

    }, 1500);

});

document.getElementById("generate-btn").addEventListener("click", async () => {

    const question = questionInput.value.trim();

    if (question === "") {

        alert("Please enter a question.");

        return;

    }

    sqlOutput.innerText = "Generating SQL...";

    sqlType.innerText = "...";

    difficulty.innerText = "...";

    explanation.innerText = "Generating explanation...";

    try {

        const response = await fetch("/generate", {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify({

                question: question

            })

        });

        const data = await response.json();

        sqlOutput.innerText = data.sql;

        sqlType.innerText = data.type;

        difficulty.innerText = data.difficulty;

        explanation.innerText = data.explanation;

    }

    catch (error) {

        sqlOutput.innerText = "Something went wrong.";

        sqlType.innerText = "-";

        difficulty.innerText = "-";

        explanation.innerText = "Unable to generate explanation.";

        console.error(error);

    }

});