import pandas as pd
import os

clean_dir = "clean_data"
if not os.path.exists(clean_dir):
    os.makedirs(clean_dir)

def clean_data(file_path,output_folder):

    df = pd.read_excel(file_path,header=13)

    needed_columns = [
        "单据日期",
        "往来单位名称",
        "商品名称",
        "折后金额_原币",
        "成本金额",
        "毛利",
        "毛利率(%)"
    ]

    df = df[needed_columns]

    df = df.reset_index(drop=True)

    df["单据日期"]=pd.to_datetime(df["单据日期"])
    df["月份"]=df["单据日期"].dt.month

    output_file = "clean_data/clean_data.xlsx"
    df.to_excel(output_file,index=False)
    return output_file

    
        

    
