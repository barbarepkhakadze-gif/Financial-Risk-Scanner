
import streamlit as st

import anomaly_detector

print("DEBUG FILE:", anomaly_detector.__file__)
print("DEBUG FUNCTIONS:", dir(anomaly_detector))


# =====================================================
# CORE MODULES
# =====================================================

from parser import read_financial_statement
from calculator import calculate_financial_ratios
from risk_engine import calculate_risk_score
from insights import generate_insights
from charts import display_ratio_chart
from report import create_report



# =====================================================
# BENCHMARKING
# =====================================================

from benchmark import (
    compare_to_benchmark,
    load_benchmarks,
    generate_benchmark_insights
)


# =====================================================
# AUDIT INTELLIGENCE
# =====================================================

from ai_insights import generate_ai_summary


# =====================================================
# COMPANY PROFILE
# =====================================================

from company_profile import (
    create_company_profile,
    generate_health_snapshot
)


# =====================================================
# HISTORICAL ANALYSIS
# =====================================================

from historical_reader import read_historical_files

from trend_engine import (
    create_trend_table,
    calculate_trends,
    generate_trend_insights
)



# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Financial Statement Risk Scanner",
    page_icon="📊",
    layout="wide"
)



# =====================================================
# HEADER
# =====================================================

st.title(
    "Financial Statement Risk Scanner"
)

st.subheader(
    "Automated Financial Analysis & Audit Risk Assessment Platform"
)


st.divider()



st.write(
"""
This platform analyzes company financial statements and evaluates:

- Liquidity Risk
- Profitability Performance
- Debt & Leverage Risk
- Operational Efficiency
- Industry Benchmark Performance
- Audit Risk Indicators
- Financial Trends
"""
)


st.divider()



# =====================================================
# DASHBOARD
# =====================================================

col1, col2, col3 = st.columns(3)


with col1:
    st.metric(
        "System Status",
        "Awaiting Upload"
    )


with col2:
    st.metric(
        "Analysis Modules",
        "Present below"
    )


with col3:
    st.metric(
        "Risk Score",
        "Calculated After Upload"
    )



st.divider()



# =====================================================
# FILE UPLOAD
# =====================================================

st.header(
    "Upload Financial Statements"
)


uploaded_file = st.file_uploader(
    "Upload Excel (.xlsx) or CSV (.csv)",
    type=["xlsx","csv"]
)



# =====================================================
# MAIN ENGINE
# =====================================================

if uploaded_file:


    st.success(
        "File uploaded successfully!"
    )



    # -------------------------------
    # READ DATA
    # -------------------------------

    data = read_financial_statement(
        uploaded_file
    )


    st.subheader(
        "Financial Data Preview"
    )


    st.dataframe(
        data
    )



    # -------------------------------
    # FINANCIAL DICTIONARY
    # -------------------------------


    financials = dict(
        zip(
            data["Metric"],
            data["Value"]
        )
    )


    st.subheader(
        "Extracted Financial Data"
    )


    st.write(
        financials
    )



    # -------------------------------
    # KEY METRICS
    # -------------------------------


    revenue = financials["Revenue"]

    net_income = financials["Net Income"]

    total_assets = financials["Total Assets"]



    st.subheader(
        "Key Financial Metrics"
    )


    st.write(
        f"Revenue: ${revenue:,.0f}"
    )


    st.write(
        f"Net Income: ${net_income:,.0f}"
    )


    st.write(
        f"Total Assets: ${total_assets:,.0f}"
    )


    st.divider()



    # -------------------------------
    # RATIOS
    # -------------------------------


    st.subheader(
        "Financial Health Dashboard"
    )


    ratios = calculate_financial_ratios(
        financials
    )


    col1,col2,col3,col4 = st.columns(4)


    with col1:
        st.metric(
            "Current Ratio",
            ratios["Current Ratio"]
        )


    with col2:
        st.metric(
            "Net Margin",
            f'{ratios["Net Margin (%)"]}%'
        )


    with col3:
        st.metric(
            "Return on Assets",
            f'{ratios["Return on Assets (%)"]}%'
        )


    with col4:
        st.metric(
            "Debt to Assets",
            f'{ratios["Debt to Assets (%)"]}%'
        )



    st.divider()



    # -------------------------------
    # RISK ENGINE
    # -------------------------------


    st.subheader(
        "Financial Risk Assessment"
    )


    score, risk_level, findings = calculate_risk_score(
        ratios
    )


    st.metric(
        "Financial Health Score",
        f"{score}/100"
    )


    st.write(
        f"Overall Assessment: **{risk_level}**"
    )


    for finding in findings:
        st.write(
            finding
        )



    st.divider()



    # -------------------------------
    # INSIGHTS
    # -------------------------------


    st.subheader(
        "Audit Analysis"
    )


    insights = generate_insights(
        ratios
    )


    for insight in insights:
        st.markdown(
            insight
        )



    st.divider()



    # -------------------------------
    # CHARTS
    # -------------------------------


    st.subheader(
        "Financial Ratio Visualization"
    )


    display_ratio_chart(
        ratios
    )
        

    
    # =====================================================
    # INDUSTRY BENCHMARKING
    # =====================================================


    st.divider()


    st.subheader(
        "Industry Benchmark Analysis"
    )


    benchmarks = load_benchmarks()


    industry = st.selectbox(
        "Select Company Industry",
        benchmarks["Industry"].tolist()
    )



    comparison = compare_to_benchmark(
        ratios,
        industry
    )



    st.write(
        f"Comparison against **{industry} industry benchmark**"
    )



    for metric, values in comparison.items():


        st.markdown(
            f"### {metric}"
        )


        col1,col2 = st.columns(2)



        with col1:

            st.metric(
                "Company",
                round(
                    values["Company"],
                    2
                )
            )



        with col2:

            st.metric(
                "Industry Benchmark",
                round(
                    float(values["Benchmark"]),
                    2
                )
            )



    # =====================================================
    # BENCHMARK COMMENTARY
    # =====================================================


    st.divider()


    st.subheader(
        "Benchmark Analyst Commentary"
    )


    benchmark_insights = generate_benchmark_insights(
        comparison
    )



    for insight in benchmark_insights:

        st.write(
            insight
        )




    # =====================================================
    # COMPANY PROFILE
    # =====================================================


    st.divider()


    st.subheader(
        "Company Profile"
    )



    company_name = st.text_input(
        "Company Name",
        "Sample Company"
    )



    company_industry = st.text_input(
        "Industry",
        industry
    )



    reporting_period = st.text_input(
        "Reporting Period",
        "FY2025"
    )



    profile = create_company_profile(
        company_name,
        company_industry,
        reporting_period
    )



    st.write(
        profile
    )



    # =====================================================
    # HEALTH SNAPSHOT
    # =====================================================


    st.subheader(
        "Financial Health Snapshot"
    )


    snapshot = generate_health_snapshot(
        ratios,
        score
    )



    for key,value in snapshot.items():

        st.metric(
            key,
            value
        )



    # =====================================================
    # HISTORICAL TREND ANALYSIS
    # =====================================================


    st.divider()


    st.subheader(
        "Historical Financial Trend Analysis"
    )



    historical_files = st.file_uploader(
        "Upload previous years financial statements",
        type=["xlsx"],
        accept_multiple_files=True,
        key="historical_upload"
    )



    if historical_files:


        historical_data = read_historical_files(
            historical_files
        )



        if len(historical_data) >= 2:


            trend_table = create_trend_table(
                historical_data
            )


            st.subheader(
                "Historical Financial Data"
            )


            st.dataframe(
                trend_table
            )



            trends = calculate_trends(
                trend_table
            )



            st.subheader(
                "Trend Metrics"
            )


            col1,col2,col3,col4 = st.columns(4)



            with col1:

                st.metric(
                    "Revenue Growth",
                    f"{trends['Revenue Growth (%)']}%"
                )


            with col2:

                st.metric(
                    "Profit Growth",
                    f"{trends['Profit Growth (%)']}%"
                )


            with col3:

                st.metric(
                    "Debt Change",
                    f"{trends['Debt Change (%)']}%"
                )


            with col4:

                st.metric(
                    "Asset Growth",
                    f"{trends['Asset Growth (%)']}%"
                )



            st.subheader(
                "Trend Analyst Commentary"
            )


            trend_comments = generate_trend_insights(
                trends
            )



            for comment in trend_comments:

                st.write(
                    comment
                )



        else:


            st.warning(
                "Upload at least two years of financial statements."
            )

        # =====================================================
    # ADVANCED PDF AUDIT REPORT GENERATOR
    # =====================================================


    st.divider()


    st.subheader(
        "Generate Comprehensive Audit Report"
    )



    if st.button(
        "Generate Audit Report",
        key="final_pdf_button"
    ):



        create_report(

            "Financial_Risk_Report.pdf",

            financials,

            ratios,

            score,

            risk_level,

            findings,

            comparison,

            benchmark_insights

        )



        with open(

            "Financial_Risk_Report.pdf",

            "rb"

        ) as file:



            st.download_button(

                label="Download Financial Risk Report",

                data=file,

                file_name="Financial_Risk_Report.pdf",

                mime="application/pdf",

                key="final_pdf_download"

            )
