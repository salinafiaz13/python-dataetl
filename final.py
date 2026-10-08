# This ETL project analyzes NYPD Arrest Data to find the
# most common arrest offenses and boroughs.

import pandas as pd
import matplotlib.pyplot as plt

# EXTRACT
# Read the CSV file into a DataFrame

file_name = "final/nypd_arrest_data.csv"
df = pd.read_csv(file_name)

print("Data successfully loaded.")

# TRANSFORM
# Remove rows with missing offense descriptions
clean_df = df[df["OFNS_DESC"].notna()]

# Find top 10 most common arrest offenses
top_offenses = clean_df["OFNS_DESC"].value_counts().head(10)

# Find arrests by borough
borough_counts = clean_df["ARREST_BORO"].value_counts()

# Find borough with most arrests
most_common_borough = borough_counts.idxmax()

# Convert borough code into full borough name
if most_common_borough == "M":
    borough_name = "Manhattan"
elif most_common_borough == "B":
    borough_name = "Bronx"
elif most_common_borough == "K":
    borough_name = "Brooklyn"
elif most_common_borough == "Q":
    borough_name = "Queens"
elif most_common_borough == "S":
    borough_name = "Staten Island"
else:
    borough_name = "Unknown"
# LOAD
# Save top offenses to CSV
top_offenses.to_csv("top_10_offenses.csv")

# Save borough counts to CSV
borough_counts.to_csv("borough_arrests.csv")

# Create summary text
summary_text = f"""
NYPD Arrest Data ETL Summary

Top 10 Most Common Arrest Offenses:
{top_offenses}

Borough With Most Arrests:
{borough_name}

Total Arrests by Borough:
{borough_counts}
"""

# Write summary text file
with open("arrest_summary.txt", "w", encoding="utf-8") as file:
    file.write(summary_text)

# Create bar chart with matplotlib
plt.figure(figsize=(12, 6))
top_offenses.plot(kind="bar")
plt.title("Top 10 Most Common NYPD Arrest Offenses")
plt.xlabel("Offense Type")
plt.ylabel("Number of Arrests")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("top_10_offenses.png")
plt.close()

# Print confirmation for the user
print("Top offenses saved to top_10_offenses.csv")
print("Borough data saved to borough_arrests.csv")
print("Summary saved to arrest_summary.txt")
print("Bar chart saved to top_10_offenses.png")
print(f"The borough with the most arrests was {borough_name}")