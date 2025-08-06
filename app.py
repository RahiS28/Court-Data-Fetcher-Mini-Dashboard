from flask import Flask, render_template, request
from scraper import fetch_case_data
from models import init_db, log_query

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        case_type = request.form.get("case_type")
        case_number = request.form.get("case_number")
        filing_year = request.form.get("filing_year")

        raw_html, parsed_data = fetch_case_data(case_type, case_number, filing_year)
        log_query(case_type, case_number, filing_year, raw_html)

        if parsed_data is None:
            return render_template("result.html", error="Could not fetch case data.")
        return render_template("result.html", data=parsed_data)

    return render_template("index.html")

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
