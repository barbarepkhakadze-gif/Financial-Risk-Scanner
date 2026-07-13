from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak,
    Image
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter

from datetime import datetime


from pdf_charts import (
    create_ratio_chart,
    create_risk_chart,
    create_benchmark_chart
)



def create_report(
    filename,
    company_name,
    company_industry,
    reporting_period,
    financials,
    ratios,
    score,
    risk_level,
    findings,
    comparison=None,
    benchmark_insights=None
):


    doc = SimpleDocTemplate(
        filename,
        pagesize=letter
    )


    styles=getSampleStyleSheet()


    content=[]



    # =====================================================
    # CREATE CHARTS
    # =====================================================


    ratio_chart=create_ratio_chart(
        ratios
    )


    risk_chart=create_risk_chart(
        score
    )


    benchmark_chart=None


    if comparison:

        benchmark_chart=create_benchmark_chart(
            comparison
        )




    # =====================================================
    # COVER PAGE
    # =====================================================

    content.append(
        Paragraph(
        "FINANCIAL STATEMENT<br/>RISK ASSESSMENT REPORT",
        styles["Title"]
        )
    )    

    content.append(Spacer(1,25))

    content.append(
        Paragraph(
        f"<b>Company:</b> {company_name}",
        styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
        f"<b>Industry:</b> {company_industry}",
        styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
        f"<b>Reporting Period:</b> {reporting_period}",
        styles["BodyText"]
        )
    )



    content.append(
        Spacer(1,40)
    )


    content.append(
        Paragraph(
            "Automated Audit Analytics Platform",
            styles["Heading2"]
        )
    )


    content.append(
        Spacer(1,20)
    )


    content.append(
        Paragraph(
            f"Generated: {datetime.now().strftime('%B %Y')}",
            styles["BodyText"]
        )
    )


    content.append(
        PageBreak()
    )



    # =====================================================
    # EXECUTIVE SUMMARY
    # =====================================================


    content.append(
        Paragraph(
            "1. Executive Summary",
            styles["Heading2"]
        )
    )


    content.append(
        Paragraph(
            f"""
            Financial Health Score:
            <b>{score}/100</b>
            <br/>
            Risk Classification:
            <b>{risk_level}</b>
            """,
            styles["BodyText"]
        )
    )


    content.append(
        Spacer(1,20)
    )


    content.append(
        Image(
            risk_chart,
            width=250,
            height=250
        )
    )



    content.append(
        PageBreak()
    )



    # =====================================================
    # FINANCIAL OVERVIEW
    # =====================================================


    content.append(
        Paragraph(
            "2. Financial Overview",
            styles["Heading2"]
        )
    )


    table=Table(
        [
            ["Metric","Value"],

            [
                "Revenue",
                f"${financials['Revenue']:,.0f}"
            ],

            [
                "Net Income",
                f"${financials['Net Income']:,.0f}"
            ],

            [
                "Assets",
                f"${financials['Total Assets']:,.0f}"
            ]

        ]
    )


    table.setStyle(
        TableStyle(
            [
                ("GRID",(0,0),(-1,-1),0.5,None)
            ]
        )
    )


    content.append(table)


    content.append(
        Spacer(1,25)
    )



    # =====================================================
    # RATIO CHART
    # =====================================================


    content.append(
        Paragraph(
            "3. Financial Ratio Analytics",
            styles["Heading2"]
        )
    )


    content.append(
        Image(
            ratio_chart,
            width=400,
            height=250
        )
    )



    # =====================================================
    # BENCHMARKING
    # =====================================================


    if comparison:


        content.append(
            PageBreak()
        )


        content.append(
            Paragraph(
                "4. Industry Benchmark Analysis",
                styles["Heading2"]
            )
        )


        content.append(
            Image(
                benchmark_chart,
                width=400,
                height=250
            )
        )


        content.append(
            Spacer(1,20)
        )



        if benchmark_insights:

            for insight in benchmark_insights:

                content.append(
                    Paragraph(
                        insight,
                        styles["BodyText"]
                    )
                )


                content.append(
                    Spacer(1,10)
                )




    # =====================================================
    # AUDIT OBSERVATIONS
    # =====================================================


    content.append(
        PageBreak()
    )


    content.append(
        Paragraph(
            "5. Audit Observations",
            styles["Heading2"]
        )
    )


    for finding in findings:

        content.append(
            Paragraph(
                "• "+finding,
                styles["BodyText"]
            )
        )

        content.append(
            Spacer(1,8)
        )



    content.append(
        Paragraph(
            "6. Recommendations",
            styles["Heading2"]
        )
    )


    content.append(
        Paragraph(
            """
            Management should continue monitoring liquidity,
            profitability, leverage exposure, and operational
            efficiency. Industry benchmarking should be used
            regularly to identify emerging financial risks.
            """,
            styles["BodyText"]
        )
    )



    doc.build(content)
