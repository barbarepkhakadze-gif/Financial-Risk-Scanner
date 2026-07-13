# =====================================================
# COMPANY PROFILE & TREND ANALYSIS ENGINE
# =====================================================

from datetime import datetime


# =====================================================
# CREATE COMPANY PROFILE
# =====================================================

def create_company_profile(
    company_name,
    industry,
    reporting_period
):

    profile = {

        "Company Name": company_name,

        "Industry": industry,

        "Reporting Period": reporting_period,

        "Generated": datetime.now().strftime(
            "%B %Y"
        )

    }

    return profile



# =====================================================
# GROWTH CALCULATION
# =====================================================

def calculate_growth(
    current_value,
    previous_value
):

    if previous_value == 0:
        return 0

    growth = (
        (current_value - previous_value)
        /
        previous_value
    ) * 100


    return round(
        growth,
        2
    )



# =====================================================
# TREND INSIGHTS
# =====================================================

def generate_trend_insights(
    growth_data
):

    insights = []


    revenue_growth = growth_data.get(
        "Revenue Growth",
        0
    )


    profit_growth = growth_data.get(
        "Profit Growth",
        0
    )



    if revenue_growth > 10:

        insights.append(
            "🟢 Strong revenue expansion detected."
        )

    elif revenue_growth < 0:

        insights.append(
            "🔴 Revenue decline requires investigation."
        )

    else:

        insights.append(
            "🟡 Revenue growth remains moderate."
        )



    if profit_growth > revenue_growth:

        insights.append(
            "🟢 Profitability is improving faster than revenue."
        )

    elif profit_growth < revenue_growth:

        insights.append(
            "🟡 Profit margins may be under pressure."
        )


    return insights



# =====================================================
# FINANCIAL HEALTH SNAPSHOT
# =====================================================

def generate_health_snapshot(
    ratios,
    risk_score
):

    snapshot = {}


    snapshot["Liquidity"] = (
        "Strong"
        if ratios["Current Ratio"] >= 1.5
        else
        "Needs Monitoring"
    )


    snapshot["Profitability"] = (
        "Strong"
        if ratios["Net Margin (%)"] >= 15
        else
        "Moderate"
    )


    snapshot["Leverage"] = (
        "Controlled"
        if ratios["Debt to Assets (%)"] <= 40
        else
        "Elevated"
    )


    snapshot["Overall Score"] = risk_score


    return snapshot