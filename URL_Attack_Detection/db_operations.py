import sqlite3

DATABASE = "url_scans.db"


def save_scan(url, result, risk_score, ip_address):
    """
    Save a URL scan result into the database.
    """

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO scans
        (url, result, risk_score, ip_address)
        VALUES (?, ?, ?, ?)
    """, (url, result, risk_score, ip_address))

    conn.commit()
    conn.close()


def get_recent_scans(limit=10):
    """
    Return the most recent URL scans.
    """

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            url,
            result,
            risk_score,
            ip_address,
            scan_time
        FROM scans
        ORDER BY id DESC
        LIMIT ?
    """, (limit,))

    rows = cursor.fetchall()

    conn.close()

    return rows


def get_total_scans():
    """
    Return total number of scans.
    """

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM scans")

    total = cursor.fetchone()[0]

    conn.close()

    return total


def get_safe_count():
    """
    Return number of safe URLs.
    """

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM scans
        WHERE result='✅ Safe URL'
    """)

    count = cursor.fetchone()[0]

    conn.close()

    return count


def get_malicious_count():
    """
    Return number of malicious URLs.
    """

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM scans
        WHERE result='⚠️ Malicious URL'
    """)

    count = cursor.fetchone()[0]

    conn.close()

    return count