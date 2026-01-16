from flask import Flask, render_template, request
import re

app = Flask(__name__)

# Skill keywords (you can add more)
SKILLS = [
    "python", "java", "c", "c++", "html", "css", "javascript",
    "sql", "dbms", "machine learning", "ai", "flask", "django"
]

@app.route("/", methods=["GET", "POST"])
def index():
    score = 0
    found_skills = []
    missing_skills = []

    if request.method == "POST":
        resume_text = request.form["resume"].lower()

        for skill in SKILLS:
            if re.search(r"\b" + re.escape(skill) + r"\b", resume_text):
                found_skills.append(skill)
                score += 5
            else:
                missing_skills.append(skill)

        if score > 100:
            score = 100

    return render_template(
        "index.html",
        score=score,
        found_skills=found_skills,
        missing_skills=missing_skills
    )

if __name__ == "__main__":
    app.run(debug=True)
