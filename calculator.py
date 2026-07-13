def calculate_financial_ratios(financials):
    """
    Calculates key financial ratios from company financial data.
    """

    ratios = {}

    # Extract values
    revenue = financials["Revenue"]
    net_income = financials["Net Income"]
    assets = financials["Total Assets"]
    cash = financials["Cash"]
    inventory = financials["Inventory"]
    current_liabilities = financials["Current Liabilities"]
    debt = financials["Total Debt"]

    # Liquidity
    current_ratio = (
        cash + inventory
    ) / current_liabilities

    # Profitability
    net_margin = (
        net_income / revenue
    ) * 100

    # Efficiency
    roa = (
        net_income / assets
    ) * 100

    # Leverage
    debt_ratio = (
        debt / assets
    ) * 100


    ratios["Current Ratio"] = round(current_ratio, 2)
    ratios["Net Margin (%)"] = round(net_margin, 2)
    ratios["Return on Assets (%)"] = round(roa, 2)
    ratios["Debt to Assets (%)"] = round(debt_ratio, 2)


    return ratios