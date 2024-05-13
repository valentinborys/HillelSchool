from pathlib import Path
import pandas as pd

file1_path = Path("file1.csv")
file2_path = Path("file2.csv")

df1 = pd.read_csv(file1_path)
df2 = pd.read_csv(file2_path)

df = pd.concat([df1, df2])

df_no_duplicates = df.drop_duplicates()

output_file_path = Path("../Task 1/Answer_1.csv")

df_no_duplicates.to_csv(output_file_path, index=False)
