# =====================================================
# AUDIT ANOMALY DETECTOR
# =====================================================


def detect_anomalies(
    ratios,
    financials,
    comparison=None
):

    anomalies = []


    # -----------------------------
    # Liquidity Analysis
    # -----------------------------

    current_ratio = ratios.get(
        "Current Ratio",
        0
    )


    if current_ratio < 1:

        anomalies.append(
            {
                "Severity": "High",
                "Risk": "Liquidity Risk",
                "Finding": "Current ratio is below 1. Company may struggle to meet short-term obligations."
            }
        )


    elif current_ratio < 1.5:

        anomalies.append(
            {
                "Severity": "Medium",
                "Risk": "Liquidity Risk",
                "Finding": "Liquidity position requires monitoring."
            }
        )



    # -----------------------------
    # Profitability Analysis
    # -----------------------------

    margin = ratios.get(
        "Net Margin (%)",
        0
    )


    if margin < 5:

        anomalies.append(
            {
                "Severity": "Medium",
                "Risk": "Profitability Risk",
                "Finding": "Profit margins are below healthy levels."
            }
        )



    # -----------------------------
    # Debt Analysis
    # -----------------------------

    debt = ratios.get(
        "Debt to Assets (%)",
        0
    )


    if debt > 60:

        anomalies.append(
            {
                "Severity": "High",
                "Risk": "Leverage Risk",
                "Finding": "Debt exposure is significantly elevated."
            }
        )



    # -----------------------------
    # Benchmark Comparison
    # -----------------------------

    if comparison:

        if (
            comparison["Debt to Assets (%)"]["Company"]
            >
            comparison["Debt to Assets (%)"]["Benchmark"]
        ):

            anomalies.append(
                {
                    "Severity": "Medium",
                    "Risk": "Benchmark Deviation",
                    "Finding": "Debt level exceeds industry benchmark."
                }
            )



    return anomalies