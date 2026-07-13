import matplotlib.pyplot as plt
import numpy as np


# =====================================================
# RATIO COMPARISON CHART
# =====================================================

def create_ratio_chart(ratios):

    metrics = [
        "Current Ratio",
        "Net Margin",
        "ROA",
        "Debt"
    ]

    values = [
        ratios["Current Ratio"],
        ratios["Net Margin (%)"],
        ratios["Return on Assets (%)"],
        ratios["Debt to Assets (%)"]
    ]


    plt.figure(figsize=(7,4))

    plt.bar(
        metrics,
        values
    )

    plt.title(
        "Financial Ratio Analysis"
    )

    plt.ylabel(
        "Value"
    )


    plt.xticks(
        rotation=25
    )


    path = "ratio_chart.png"


    plt.tight_layout()

    plt.savefig(
        path,
        dpi=300
    )

    plt.close()


    return path




# =====================================================
# RISK SCORE PIE CHART
# =====================================================

def create_risk_chart(score):


    if score >= 70:

        labels = [
            "Healthy",
            "Risk Exposure"
        ]

        values = [
            score,
            100-score
        ]


    elif score >= 40:

        labels = [
            "Moderate",
            "Risk Exposure"
        ]

        values = [
            score,
            100-score
        ]


    else:

        labels = [
            "Risk",
            "Remaining"
        ]

        values = [
            100-score,
            score
        ]



    plt.figure(figsize=(5,5))


    plt.pie(
        values,
        labels=labels,
        autopct="%1.1f%%"
    )


    plt.title(
        "Financial Health Risk Profile"
    )


    path="risk_chart.png"


    plt.savefig(
        path,
        dpi=300,
        bbox_inches="tight"
    )


    plt.close()


    return path





# =====================================================
# BENCHMARK COMPARISON CHART
# =====================================================

def create_benchmark_chart(comparison):


    metrics=list(
        comparison.keys()
    )


    company=[]

    benchmark=[]


    for metric in metrics:

        company.append(
            comparison[metric]["Company"]
        )


        benchmark.append(
            comparison[metric]["Benchmark"]
        )



    x=np.arange(
        len(metrics)
    )


    width=0.35



    plt.figure(figsize=(8,4))


    plt.bar(
        x-width/2,
        company,
        width,
        label="Company"
    )


    plt.bar(
        x+width/2,
        benchmark,
        width,
        label="Industry"
    )


    plt.xticks(
        x,
        metrics,
        rotation=30,
        ha="right"
    )


    plt.title(
        "Company vs Industry Benchmark"
    )


    plt.legend()


    plt.tight_layout()


    path="benchmark_chart.png"


    plt.savefig(
        path,
        dpi=300
    )


    plt.close()


    return path