import pandas as pd


# =====================================================
# CALCULATE YEARLY GROWTH
# =====================================================

def calculate_growth(
    current,
    previous
):

    if previous == 0:
        return 0

    return round(
        ((current - previous) / previous) * 100,
        2
    )



# =====================================================
# BUILD FINANCIAL TREND TABLE
# =====================================================

def create_trend_table(
    yearly_data
):

    df = pd.DataFrame(yearly_data)


    df = df.sort_values(
        by="Year"
    )


    return df



# =====================================================
# CALCULATE TREND METRICS
# =====================================================

def calculate_trends(
    df
):

    trends = {}


    if len(df) < 2:

        return {
            "Error":
            "At least two years of data are required."
        }



    latest = df.iloc[-1]
    previous = df.iloc[-2]



    trends["Revenue Growth (%)"] = calculate_growth(
        latest["Revenue"],
        previous["Revenue"]
    )


    trends["Profit Growth (%)"] = calculate_growth(
        latest["Net Income"],
        previous["Net Income"]
    )


    trends["Debt Change (%)"] = calculate_growth(
        latest["Total Debt"],
        previous["Total Debt"]
    )


    trends["Asset Growth (%)"] = calculate_growth(
        latest["Total Assets"],
        previous["Total Assets"]
    )


    return trends



# =====================================================
# GENERATE AUDIT TREND INSIGHTS
# =====================================================

def generate_trend_insights(
    trends
):

    insights = []


    # Revenue

    if trends["Revenue Growth (%)"] > 10:

        insights.append(
            "🟢 Revenue growth is strong, indicating business expansion."
        )

    elif trends["Revenue Growth (%)"] < 0:

        insights.append(
            "🔴 Revenue declined compared with the previous period."
        )

    else:

        insights.append(
            "🟡 Revenue growth remains moderate."
        )



    # Profitability

    if trends["Profit Growth (%)"] < trends["Revenue Growth (%)"]:

        insights.append(
            "🟡 Profit growth is slower than revenue growth, suggesting possible margin pressure."
        )

    else:

        insights.append(
            "🟢 Profitability is improving alongside revenue."
        )



    # Debt

    if trends["Debt Change (%)"] > 10:

        insights.append(
            "🔴 Debt is increasing significantly and should be monitored."
        )

    elif trends["Debt Change (%)"] < 0:

        insights.append(
            "🟢 Debt reduction indicates improving leverage management."
        )

    else:

        insights.append(
            "🟡 Debt levels remain relatively stable."
        )


    return insights