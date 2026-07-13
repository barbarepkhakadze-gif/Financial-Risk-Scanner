import pandas as pd
import streamlit as st
import altair as alt


def display_ratio_chart(ratios):
    """
    Creates a professional financial ratio visualization.
    """

    chart_data = pd.DataFrame(
        {
            "Metric": [
                "Current Ratio",
                "Net Margin (%)",
                "Return on Assets (%)",
                "Debt to Assets (%)"
            ],
            "Value": [
                ratios["Current Ratio"],
                ratios["Net Margin (%)"],
                ratios["Return on Assets (%)"],
                ratios["Debt to Assets (%)"]
            ]
        }
    )


    chart = (
        alt.Chart(chart_data)
        .mark_bar()
        .encode(
            x=alt.X(
                "Value",
                title="Value"
            ),
            y=alt.Y(
                "Metric",
                title="Financial Metric",
                sort="-x"
            ),
            tooltip=[
                "Metric",
                "Value"
            ]
        )
        .properties(
            height=300
        )
    )


    st.altair_chart(
        chart,
        use_container_width=True
    )