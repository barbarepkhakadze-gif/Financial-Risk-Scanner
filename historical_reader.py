import pandas as pd
import re


# =====================================================
# EXTRACT YEAR FROM FILE NAME
# =====================================================

def extract_year(filename):

    years = re.findall(
        r"\d{4}",
        filename
    )

    if years:
        return int(years[0])

    return None



# =====================================================
# READ MULTIPLE HISTORICAL STATEMENTS
# =====================================================

def read_historical_files(files):

    historical_data = []


    for file in files:


        year = extract_year(
            file.name
        )


        if year is None:

            continue



        # Read Excel file

        df = pd.read_excel(
            file
        )


        financials = dict(
            zip(
                df["Metric"],
                df["Value"]
            )
        )



        historical_data.append(

            {

                "Year": year,

                "Revenue":
                    financials.get(
                        "Revenue",
                        0
                    ),

                "Net Income":
                    financials.get(
                        "Net Income",
                        0
                    ),

                "Total Assets":
                    financials.get(
                        "Total Assets",
                        0
                    ),

                "Total Debt":
                    financials.get(
                        "Total Debt",
                        0
                    )

            }

        )


    return sorted(
        historical_data,
        key=lambda x: x["Year"]
    )