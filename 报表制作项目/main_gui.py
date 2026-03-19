from tkinter import*
from tkinter import filedialog,messagebox
from data_clean import clean_data
from analysis import monthly_summary
from chart import create_charts
from report_export import export_report

def run():
    file_path = filedialog.askopenfilename(
        filetypes=[("Excel files","*.xlsx")]
    )

    if not file_path:
        return

    try:

        clean_file = clean_data(file_path,"clean_data")

        df,summary = monthly_summary(clean_file)

        charts = create_charts(summary)

        output = export_report(df,summary,charts)

        messagebox.showinfo("完成",f"报表已生成:{output}")

    except Exception as e:

        messagebox.showerror("错误",str(e))

root = Tk()
root.title("ERP销售报表生成器")
root.geometry("360x220")

Label(
    root,
    text="ERP销售报表自动生成工具",
    font=("Arial",14)
).pack(pady=40)

Button(
    root,
    text="选择ERP Excel生成报表",
    command=run,
    width=25,
    height=2
).pack()

root.mainloop()
        
