from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors


def generate_pdf(
        url,
        result,
        risk_score,
        ip_address,
        whois_data):

    data = [
        ["Field", "Value"],
        ["URL", url],
        ["Result", result],
        ["Risk Score", f"{risk_score}%"],
        ["IP Address", ip_address],
        ["Registrar", whois_data["registrar"]],
        ["Creation Date", str(whois_data["creation_date"])],
        ["Expiration Date", str(whois_data["expiration_date"])]
    ]

    pdf = SimpleDocTemplate("static/report.pdf")

    table = Table(data)

    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),

        ("BACKGROUND", (0, 1), (0, -1), colors.lightgrey),

        ("GRID", (0, 0), (-1, -1), 1, colors.black),

        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),

        ("BOTTOMPADDING", (0, 0), (-1, 0), 10),

        ("ALIGN", (0, 0), (-1, -1), "CENTER")
    ]))

    pdf.build([table])