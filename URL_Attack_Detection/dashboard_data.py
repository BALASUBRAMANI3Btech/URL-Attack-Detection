import sqlite3


def get_dashboard_data():

    conn = sqlite3.connect("url_scans.db")

    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM scans")
    total_scans = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM scans WHERE result='✅ Safe URL'"
    )
    safe_urls = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM scans WHERE result='⚠️ Malicious URL'"
    )
    malicious_urls = cursor.fetchone()[0]

    conn.close()

    return {
        "total_scans": total_scans,
        "safe_urls": safe_urls,
        "malicious_urls": malicious_urls
    }