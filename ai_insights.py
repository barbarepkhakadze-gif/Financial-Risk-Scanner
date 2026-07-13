def generate_ai_summary(
    ratios,
    score,
    risk_level,
    anomalies
):

    summary = []

    summary.append(
        f"The company received a Financial Health Score of {score}/100 "
        f"and is classified as {risk_level}."
    )

    if ratios["Net Margin (%)"] >= 10:
        summary.append(
            "Profitability indicators demonstrate healthy earnings performance."
        )
    else:
        summary.append(
            "Profitability remains below the desired level."
        )

    if ratios["Debt to Assets (%)"] < 40:
        summary.append(
            "Leverage appears well controlled."
        )
    else:
        summary.append(
            "Debt levels require continued monitoring."
        )

    if anomalies:
        summary.append(
            f"{len(anomalies)} potential audit risk area(s) were identified."
        )
    else:
        summary.append(
            "No significant financial anomalies were detected."
        )

    return summary