from benchmark import compare_to_benchmark


ratios = {
    "Current Ratio":1.33,
    "Net Margin (%)":13,
    "Return on Assets (%)":8.12,
    "Debt to Assets (%)":37.5
}


result = compare_to_benchmark(
    ratios,
    "Technology"
)


print(result)