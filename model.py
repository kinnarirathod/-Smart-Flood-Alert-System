# %%
import requests
import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pickle
import matplotlib.pyplot as plt

# --- Configuration ---
LATITUDE = 23.2156
LONGITUDE = 72.6369
START_DATE = "2019-07-01"
END_DATE = "2025-07-01"

# --- Step 1: Fetch Rainfall Data from NASA POWER API ---
def fetch_rainfall_nasa_power(lat, lon, start_date, end_date):
    start_fmt = datetime.strptime(start_date, "%Y-%m-%d").strftime("%Y%m%d")
    end_fmt = datetime.strptime(end_date, "%Y-%m-%d").strftime("%Y%m%d")

    url = (
        f"https://power.larc.nasa.gov/api/temporal/daily/point?"
        f"parameters=PRECTOTCORR&start={start_fmt}&end={end_fmt}"
        f"&latitude={lat}&longitude={lon}&format=JSON&community=RE"
    )
    
    print(f"Fetching data from NASA POWER API...")
    res = requests.get(url)
    data = res.json()

    daily_data = data['properties']['parameter']['PRECTOTCORR']
    df = pd.DataFrame(list(daily_data.items()), columns=['date', 'rainfall_mm'])
    df['date'] = pd.to_datetime(df['date'])
    df['rainfall_mm'] = df['rainfall_mm'].astype(float)
    return df

rainfall_df = fetch_rainfall_nasa_power(LATITUDE, LONGITUDE, START_DATE, END_DATE)

# --- Step 2: Feature Engineering ---
rainfall_df['rainfall_yesterday'] = rainfall_df['rainfall_mm'].shift(1)
rainfall_df['rainfall_2day_total'] = rainfall_df['rainfall_mm'] + rainfall_df['rainfall_yesterday']
rainfall_df.dropna(inplace=True)

# --- Step 3: Dynamic Thresholds Using Percentiles ---
day1_threshold = rainfall_df['rainfall_mm'].quantile(0.995)
day2_threshold = rainfall_df['rainfall_2day_total'].quantile(0.995)

print(f"\n🚨 Flood Thresholds:\n1-day ≥ {day1_threshold:.2f} mm\n2-day total ≥ {day2_threshold:.2f} mm")

# --- Step 4: Create Flood Label ---
rainfall_df['flood'] = (
    (rainfall_df['rainfall_mm'] >= day1_threshold) &
    (rainfall_df['rainfall_2day_total'] >= day2_threshold)
).astype(int)

# --- Step 5: Train/Test Split ---
X = rainfall_df[['rainfall_mm', 'rainfall_2day_total']]
y = rainfall_df['flood'].astype(int)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- Step 6: Train Model ---
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model
with open("model_nasa.pkl", "wb") as f:
    pickle.dump(model, f)

# --- Step 7: Evaluation ---
y_pred = model.predict(X_test)
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# --- Step 8: Predictions ---
rainfall_df['predicted_flood'] = model.predict(X)
print("\nRecent Predictions:")
print(rainfall_df[['date', 'rainfall_mm', 'rainfall_2day_total', 'predicted_flood']].tail(10))

# --- Manual Prediction ---
with open("model_nasa.pkl", "rb") as f:
    model = pickle.load(f)
    print("\nExample Prediction (80 mm today, 130 mm total):", model.predict([[80, 130]]))

# --- Stats ---
print("\nFlood class distribution:")
print(rainfall_df['flood'].value_counts())

print("\nMax 1-day rainfall:", rainfall_df['rainfall_mm'].max())
print("Max 2-day total rainfall:", rainfall_df['rainfall_2day_total'].max())

# --- Optional Histogram ---
plt.hist(rainfall_df['rainfall_mm'], bins=50, color='skyblue', edgecolor='black')
plt.title("Histogram of 1-day Rainfall (mm)")
plt.xlabel("Rainfall (mm)")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# %%
rainfall_df.to_csv("new.csv")
# %%
print(rainfall_df[rainfall_df['flood']==1])