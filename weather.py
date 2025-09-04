import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("data-temperature-humidity.csv")

# Convert timestamp to datetime and create day index
data['timestamp'] = pd.to_datetime(data['timestamp'])
data['day_index'] = (data['timestamp'] - data['timestamp'].min()).dt.days + 1

# Features (X) -> just the day index
X = data[['day_index']]

# Targets (y) -> humidity and temperature
y = data[['humidity', 'temperature']]

# Split into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train RandomForestRegressor
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Predict on test data
predictions = model.predict(X_test)

# Evaluation
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)
print("Mean Squared Error:", mse)
print("R2 Score:", r2)

# Plot actual vs predicted for temperature
plt.figure(figsize=(8,5))
plt.scatter(y_test['temperature'], predictions[:,1], alpha=0.7, color='orange')
plt.xlabel("Actual Temperature")
plt.ylabel("Predicted Temperature")
plt.title("Actual vs Predicted Temperature")
plt.show()

# Plot actual vs predicted for humidity
plt.figure(figsize=(8,5))
plt.scatter(y_test['humidity'], predictions[:,0], alpha=0.7, color='green')
plt.xlabel("Actual Humidity")
plt.ylabel("Predicted Humidity")
plt.title("Actual vs Predicted Humidity")
plt.show()

def predict_weather(day):
    
    future_day = pd.DataFrame({'day_index': [day]})
    prediction = model.predict(future_day)[0]
    humidity, temperature = prediction[0], prediction[1]

    # Classify weather condition based on thresholds
    if humidity >= 80 and temperature < 25:
        condition = "Rainy"
    elif 60 <= humidity < 80 and 20 <= temperature <= 30:
        condition = "Cloudy"
    else:
        condition = "Sunny"

    return {
        "Day": day,
        "Predicted Humidity": round(humidity, 2),
        "Predicted Temperature": round(temperature, 2),
        "Weather Condition": condition
    }
N = 20  # Change this to the day you want to predict
result = predict_weather(N)

print("\nPrediction for Day", N)
print("Predicted Humidity:", result['Predicted Humidity'], "%")
print("Predicted Temperature:", result['Predicted Temperature'], "°C")
print("Predicted Weather Condition:", result['Weather Condition'])