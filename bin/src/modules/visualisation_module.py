# imports
from collections import Counter, defaultdict
import matplotlib.pyplot as plt
import modules.support as sup
import inspect as ip
import pandas as pd

# work with data to generate a visualisation
def generate_visualisations(trace: bool, search: str, df: pd.DataFrame):
    sup.traceability_handling_prints(trace, ip.currentframe().f_code.co_name)

    # Plot the top authors with text counts
    top_authors = df.groupby('Author')['Text_Count'].sum().nlargest(5)
    plt.figure(figsize=(10, 6))
    top_authors.plot(kind='bar')
    plt.title(f"Top 5 Authors by Text: '{search}' Count")
    plt.xlabel('Author')
    plt.ylabel('Text Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()