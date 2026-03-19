import pandas as pd

def monthly_summary(clean_file):
    df = pd.read_excel(clean_file)

    summary = df.groupby("月份").agg({
        "折后金额_原币":"sum",
        "成本金额":"sum",
        "毛利":"sum",
        "往来单位名称":"nunique"
})

    summary = summary.rename(columns={
        "折后金额_原币":"销售额",
        "往来单位名称":"客户数"
})
    return df,summary
    
