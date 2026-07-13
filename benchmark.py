import pandas as pd



# =====================================================
# LOAD INDUSTRY BENCHMARKS
# =====================================================

def load_benchmarks():

    return pd.read_csv(
        "benchmarks.csv"
    )



# =====================================================
# COMPARE COMPANY WITH INDUSTRY
# =====================================================

def compare_to_benchmark(
    ratios,
    industry
):

    benchmarks = load_benchmarks()


    benchmark = benchmarks[
        benchmarks["Industry"] == industry
    ].iloc[0]


    comparison = {}


    metrics = [
        "Current Ratio",
        "Net Margin (%)",
        "Return on Assets (%)",
        "Debt to Assets (%)"
    ]


    for metric in metrics:

        comparison[metric] = {

            "Company": ratios[metric],

            "Benchmark": float(
                benchmark[metric]
            )

        }


    return comparison



# =====================================================
# GENERATE ANALYST COMMENTARY
# =====================================================

def generate_benchmark_insights(
    comparison
):

    insights = []



    # -----------------------------
    # Liquidity
    # -----------------------------

    liquidity = comparison["Current Ratio"]


    if liquidity["Company"] < liquidity["Benchmark"]:

        insights.append(
            "⚠️ Liquidity is below the industry benchmark, indicating weaker short-term financial flexibility."
        )

    else:

        insights.append(
            "🟢 Liquidity is stronger than industry peers."
        )



    # -----------------------------
    # Profitability
    # -----------------------------

    margin = comparison["Net Margin (%)"]


    if margin["Company"] < margin["Benchmark"]:

        insights.append(
            "⚠️ Profitability is below industry peers. Management may need to review pricing strategy, costs, and operational efficiency."
        )

    else:

        insights.append(
            "🟢 Profitability exceeds the industry benchmark."
        )



    # -----------------------------
    # Asset Efficiency
    # -----------------------------

    roa = comparison["Return on Assets (%)"]


    if roa["Company"] < roa["Benchmark"]:

        insights.append(
            "⚠️ Return on assets is below peers, suggesting possible inefficiencies in asset utilization."
        )

    else:

        insights.append(
            "🟢 Asset utilization is stronger than industry averages."
        )



    # -----------------------------
    # Leverage Risk
    # -----------------------------

    debt = comparison["Debt to Assets (%)"]


    if debt["Company"] > debt["Benchmark"]:

        insights.append(
            "⚠️ Debt exposure is higher than the industry benchmark, indicating increased leverage risk."
        )

    else:

        insights.append(
            "🟢 Leverage position is healthier than industry peers."
        )



    return insights