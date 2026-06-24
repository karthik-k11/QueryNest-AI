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

A user will ask a question.

Return ONLY a valid JSON object.

Do NOT wrap the JSON inside markdown.

Do NOT use ```.

Do NOT write json.

Return ONLY this format:

{{
    "sql":"...",
    "type":"...",
    "difficulty":"...",
    "explanation":"..."
}}

Rules:

- sql must contain only the SQL query.
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

- difficulty must be one of:
  Beginner
  Intermediate
  Advanced

- explanation must be one short beginner-friendly sentence.

User Question:

{user_question}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text.strip()