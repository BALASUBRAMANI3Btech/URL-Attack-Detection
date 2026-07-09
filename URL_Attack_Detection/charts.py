import importlib

matplotlib = importlib.import_module("matplotlib")
matplotlib.use("Agg")
plt = importlib.import_module("matplotlib.pyplot")
import sqlite3


def create_pie_chart():

    conn = sqlite3.connect("url_scans.db")
    cursor = conn.cursor()

    # Count Safe URLs
    cursor.execute("SELECT COUNT(*) FROM scans WHERE result='✅ Safe URL'")
    safe = cursor.fetchone()[0]

    # Count Malicious URLs
    cursor.execute("SELECT COUNT(*) FROM scans WHERE result='⚠️ Malicious URL'")
    malicious = cursor.fetchone()[0]

    conn.close()

    plt.figure(figsize=(5, 5))

    plt.pie(
        [safe, malicious],
        labels=["Safe", "Malicious"],
        autopct="%1.1f%%",
        colors=["green", "red"],
        startangle=90
    )

    plt.title("URL Scan Results")

    plt.savefig("static/pie_chart.png")

    plt.close()