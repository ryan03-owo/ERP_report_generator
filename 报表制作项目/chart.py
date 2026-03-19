import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False 
import os

def create_charts(summary):
    chart_dir = "charts"
    if not os.path.exists(chart_dir):
        os.makedirs(chart_dir)

    chart_files = []

    plt.figure()
    summary["销售额"].plot(kind="bar")
    plt.title("月销售额柱状图")
    plt.xlabel("月份")
    plt.ylabel("销售额")
    file1 = os.path.join(chart_dir,"sales_chart.png")
    plt.savefig(file1)
    plt.close()
    chart_files.append(file1)

    plt.figure()
    summary["毛利"].plot(kind="line",marker="o")
    plt.title("月毛利折线图")
    plt.xlabel("月份")
    plt.ylabel("毛利")
    file2 = os.path.join(chart_dir,"profit_chart.png")
    plt.savefig(file2)
    plt.close()
    chart_files.append(file2)

    return chart_files
    
