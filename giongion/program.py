import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Replace 'your_file.xls' with the path to your .xls file
df = pd.read_excel('giongion/GridExport_June_20_2025_16_36_57.xlsx')

# print(df.columns)

import pandas as pd
import matplotlib.pyplot as plt

# Replace 'your_file.xls' with the path to your .xls file
df = pd.read_excel('giongion/GridExport_June_20_2025_16_36_57.xlsx')
# Remove the specified column if it exists
if 'Employees Health & Safety Team\n(0FY, FY0).1' in df.columns:
    df = df.drop(columns=['Employees Health & Safety Team\n(0FY, FY0).1'])

col = ["Revenue\n(EUR)", "ESG Score\n(0FY, FY0)", "ROE", "Net Profit Margin"]

# col1 = col[1]
# col2 = col[3]
# correlation = df[[col1, col2]].corr().iloc[0, 1]

# print(f"Correlation between '{col1}' and '{col2}': {correlation}")

# # Plot scatter chart
# plt.figure(figsize=(8, 6))
# plt.scatter(df[col1], df[col2])
# plt.xlabel(col1)
# plt.ylabel(col2)
# plt.title(f"Scatter plot of {col1} vs {col2}\nCorrelation: {correlation:.2f}")
# plt.grid(True)
# plt.tight_layout()
# plt.show()

corr_matrix = df.corr(numeric_only=True)
# corr_matrix.to_excel('giongion/correlation_matrix.xlsx')
strong_pairs = []
for col1 in corr_matrix.columns:
    for col2 in corr_matrix.columns:
        if col1 != col2:
            corr_value = corr_matrix.loc[col1, col2]
            if abs(corr_value) > 0.5:
                pair = tuple(sorted([col1, col2]))
                if pair not in strong_pairs:
                    strong_pairs.append(pair)
                    print(f"{col1} & {col2}: {corr_value:.2f}")
                    
strong_corr_df = pd.DataFrame(strong_pairs, columns=['Column 1', 'Column 2'])
strong_corr_df['Correlation'] = strong_corr_df.apply(lambda row: corr_matrix.loc[row['Column 1'], row['Column 2']], axis=1)
strong_corr_df.to_excel('giongion/strong_correlations.xlsx', index=False)
print("Strong correlation pairs exported to giongion/strong_correlations.xlsx")

# # Plot the heatmap for all correlations
# plt.figure(figsize=(10, 8))
# sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
# plt.title("Correlation Heatmap")
# plt.tight_layout()
# plt.show()

