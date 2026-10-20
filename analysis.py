import pandas as pd

# Step 1: Read the cleaned dataset
df = pd.read_csv("cleaned_accident_prediction_india.csv")

print("Smart City Traffic Accident Analysis")
print("-----------------------------------")

# Step 2: Display dataset information
print("Total accidents:", len(df))
print("Total columns:", len(df.columns))

# Step 3: Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Step 4: Check duplicate records  
print("\nDuplicate Rows:", df.duplicated().sum())

# Step 5: Analyze accident severity
print("\nAccidents by Severity:")n
severity = df["Accident Severity"].value_counts()
print(severity)

# Step 6: Analyze accidents by state
print("\nAccidents by State:")
state_counts = df["State Name"].value_counts()
print(state_counts)

# Step 7: Analyze accidents by year
print("\nAccidents by Year:")
year_counts = df["Year"].value_counts().sort_index()
print(year_counts)

# Step 8: Analyze weather conditions
print("\nAccidents by Weather:")
weather_counts = df["Weather Conditions"].value_counts()
print(weather_counts)

# Step 9: Save analysis results to CSV
results = []

columns_to_analyze = [
    "State Name",
    "Year",
    "Month",
    "Accident Severity",
    "Weather Conditions",
    "Road Type",
    "Road Condition",
    "Lighting Conditions",
    "Vehicle Type Involved",
    "Alcohol Involvement"
]

for column in columns_to_analyze:
    counts = df[column].fillna("Unknown").astype(str).value_counts()

    for category, count in counts.items():
        results.append({
            "Analysis": column,
            "Category": category,
            "Accident_Count": int(count),
            "Percentage": round(count / len(df) * 100, 2)
        })

result_df = pd.DataFrame(results)

result_df.to_csv(
    "smart_city_data_analysis_results.csv",
    index=False
)

print("\nAnalysis completed successfully!")
print("Output saved to smart_city_data_analysis_results.csv")
