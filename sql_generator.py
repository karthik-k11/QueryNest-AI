from config import client


DATABASE_SCHEMA = """
employees(
    employee_id,
    employee_name,
    department,
    salary,
    hire_date
)

students(
    student_id,
    student_name,
    department,
    age
)

customers(
    customer_id,
    customer_name,
    city
)

orders(
    order_id,
    customer_id,
    order_date,
    total_amount
)
"""


def generate_sql(user_question):

    prompt = f"""
You are an expert AI SQL Assistant.

Database Schema:

{DATABASE_SCHEMA}

Return ONLY a valid JSON object.

Do NOT use markdown.

Return ONLY:

{{
    "sql":"...",
    "type":"...",
    "difficulty":"...",
    "explanation":"..."
}}

Rules:

- sql must contain only SQL.
- type must be one of:
SELECT
INSERT
UPDATE
DELETE
CREATE TABLE
ALTER TABLE
DROP TABLE
JOIN
GROUP BY

- difficulty:
Beginner
Intermediate
Advanced

- explanation:
One short beginner-friendly sentence.

User Question:

{user_question}
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        if not response.text:

            raise Exception("Empty response from Gemini.")

        return response.text.strip()

    except Exception as e:

        return f"""{{
            "sql":"Error",
            "type":"-",
            "difficulty":"-",
            "explanation":"{str(e)}"
        }}"""