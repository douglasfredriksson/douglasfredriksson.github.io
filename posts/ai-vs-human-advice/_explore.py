# %% 1. Load the data
import pandas as pd

df = pd.read_csv("data/haiid_dataset.csv", dtype={"job_title": "string"})
print(df.shape)  # (rows, columns)

# %% 2. First look at a few rows
df.head()

# %% 3. Column types and missing values
df.info()

# %% 4. How many rows does each participant have?
df.groupby("participant_id").size().describe()

# %% 5. Who is in the data? Participants per task, region and stated accuracy
df.groupby(["task_name", "geographic_region", "perceived_accuracy"])["participant_id"].nunique()

# %% 6. Between or within subjects?
# Result: all 1125 participants saw exactly 1 advice source -> between-subjects (matches paper)
df.groupby("participant_id")["advice_source"].nunique().value_counts()
