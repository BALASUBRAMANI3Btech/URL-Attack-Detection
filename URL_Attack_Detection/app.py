from flask import Flask, render_template, request, send_file
import joblib

from feature_extraction import extract_features
from ip_features import get_ip
from whois_features import get_whois_info
from dns_features import get_dns_records
from db_operations import save_scan
from dashboard_data import get_dashboard_data
from charts import create_pie_chart
from pdf_report import generate_pdf

app = Flask(__name__)

# Load trained ML model
model = joblib.load("model.pkl")


@app.route("/", methods=["GET", "POST"])
def home():

    result = ""
    risk_score = ""
    ip_address = ""

    whois_data = {
        "registrar": "",
        "creation_date": "",
        "expiration_date": ""
    }

    dns_data = {
        "A": [],
        "MX": [],
        "NS": []
    }

    if request.method == "POST":

        # Get URL from user
        url = request.form["url"]

        # Feature Extraction
        features = extract_features(url)

        # ML Prediction
        prediction = model.predict([features])

        # Risk Score
        probability = model.predict_proba([features])
        risk_score = round(probability[0][1] * 100, 2)

        if prediction[0] == 0:
            result = "✅ Safe URL"
        else:
            result = "⚠️ Malicious URL"

        # Extract Domain
        domain = url.replace("https://", "")
        domain = domain.replace("http://", "")
        domain = domain.split("/")[0]

        # Get IP Address
        ip_address = get_ip(url)

        # WHOIS Information
        whois_data = get_whois_info(domain)

        # DNS Records
        dns_data = get_dns_records(domain)

        # Save Scan
        save_scan(
            url,
            result,
            risk_score,
            ip_address
        )

        # Generate PDF Report
        generate_pdf(
            url,
            result,
            risk_score,
            ip_address,
            whois_data
        )

    # Dashboard Statistics
    dashboard = get_dashboard_data()

    # Generate Pie Chart
    create_pie_chart()

    return render_template(
        "index.html",
        result=result,
        risk_score=risk_score,
        ip_address=ip_address,
        whois_data=whois_data,
        dns_data=dns_data,
        dashboard=dashboard
    )


@app.route("/download-report")
def download_report():
    return send_file(
        "static/report.pdf",
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)