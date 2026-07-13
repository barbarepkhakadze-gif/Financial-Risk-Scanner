def generate_insights(ratios):
    """
    Generates professional financial analysis commentary.
    """

    insights = []


    # Liquidity

    current_ratio = ratios["Current Ratio"]

    if current_ratio >= 1.5:
        insights.append(
            """
            **Liquidity Assessment 🟢**

            The company demonstrates strong short-term liquidity.
            Current assets appear sufficient to cover immediate obligations.
            """
        )

    elif current_ratio >= 1:
        insights.append(
            """
            **Liquidity Assessment 🟡**

            The company can meet current obligations; however,
            liquidity remains below a strong benchmark.
            """
        )

    else:
        insights.append(
            """
            **Liquidity Assessment 🔴**

            The company may experience difficulty meeting
            short-term financial obligations.
            """
        )


    # Profitability

    margin = ratios["Net Margin (%)"]

    if margin >= 15:
        insights.append(
            """
            **Profitability Assessment 🟢**

            Strong profitability indicates effective cost control
            and healthy earnings generation.
            """
        )

    elif margin >= 5:
        insights.append(
            """
            **Profitability Assessment 🟡**

            Profitability is positive but could require monitoring.
            """
        )

    else:
        insights.append(
            """
            **Profitability Assessment 🔴**

            Low profitability may indicate operational pressure.
            """
        )


    return insights
