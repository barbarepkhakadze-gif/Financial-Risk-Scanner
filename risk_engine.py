def calculate_risk_score(ratios):
    """
    Calculates overall financial risk score.
    Higher score = healthier company.
    """

    score = 100
    findings = []

    # Liquidity
    current_ratio = ratios["Current Ratio"]

    if current_ratio < 1:
        score -= 25
        findings.append("🔴 Weak liquidity: Current Ratio below 1.0")

    elif current_ratio < 1.5:
        score -= 10
        findings.append("🟡 Moderate liquidity position")

    else:
        findings.append("🟢 Strong liquidity position")


    # Profitability
    net_margin = ratios["Net Margin (%)"]

    if net_margin < 5:
        score -= 20
        findings.append("🔴 Low profitability")

    elif net_margin < 15:
        score -= 10
        findings.append("🟡 Moderate profitability")

    else:
        findings.append("🟢 Strong profitability")


    # Leverage
    debt_ratio = ratios["Debt to Assets (%)"]

    if debt_ratio > 70:
        score -= 25
        findings.append("🔴 High debt exposure")

    elif debt_ratio > 40:
        score -= 10
        findings.append("🟡 Elevated leverage")

    else:
        findings.append("🟢 Controlled leverage")


    # Final risk category

    if score >= 80:
        risk_level = "LOW RISK 🟢"

    elif score >= 60:
        risk_level = "MODERATE RISK 🟡"

    else:
        risk_level = "HIGH RISK 🔴"


    return score, risk_level, findings