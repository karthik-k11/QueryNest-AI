from flask import Flask, render_template, request, jsonify
import json

from sql_generator import generate_sql
from db import create_database, save_query, get_history

app = Flask(__name__)

create_database()


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/history")
def history():

    history_data = get_history()

    return render_template(
        "history.html",
        history=history_data
    )


@app.route("/generate", methods=["POST"])
def generate():

    data = request.get_json()

    question = data["question"]

    response = generate_sql(question)

    try:

        cleaned_response = response.replace("```json", "")
        cleaned_response = cleaned_response.replace("```", "")
        cleaned_response = cleaned_response.strip()

        result = json.loads(cleaned_response)

        save_query(
            question,
            result["sql"],
            result["type"],
            result["difficulty"]
        )

        return jsonify(result)

    except Exception:

        return jsonify({
            "sql": response,
            "type": "-",
            "difficulty": "-",
            "explanation": "Unable to analyze the generated SQL."
        })


if __name__ == "__main__":
    app.run(debug=True)