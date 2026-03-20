import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def get_summary(df, plot=False):
    summary = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "missing_values": df.isnull().sum().sum()
    }
    print(f"--- Dataset Summary ---")
    print(f"Rows: {summary['rows']}, Columns: {summary['columns']}")
    print(f"Total Missing Values: {summary['missing_values']}")
    
    if plot:
        num_cols = df.select_dtypes(include=['number']).columns
        if len(num_cols) > 0:
            df[num_cols].hist(figsize=(10, 5))
            plt.tight_layout()
            plt.show()
    return summary