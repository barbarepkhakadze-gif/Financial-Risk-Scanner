def generate_audit_risk_report(anomalies):

    report = []

    if not anomalies:
        report.append(
            "🟢 No significant audit risk indicators detected."
        )

    else:
        for item in anomalies:

            report.append(
                f"""
{item['Severity']} Risk

Risk Area:
{item['Risk']}

Observation:
{item['Finding']}
"""
            )

    return report