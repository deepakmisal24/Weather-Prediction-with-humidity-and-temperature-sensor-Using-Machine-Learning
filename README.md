# 🌦 Weather Prediction and Forecasting System

This project collects **temperature** and **humidity** readings from a **DHT11 sensor** connected to a NodeMCU board, stores the data in a CSV file, trains a **machine learning model** (RandomForestRegressor), and predicts future weather conditions such as **Sunny**, **Cloudy**, or **Rainy**.

---

## **📂 Project Structure**

```
.
├── reading-from-env.ino # Arduino code to read data from DHT11 sensor
├── store-data.py # Python script to log sensor data into a CSV file (data-temperature-humidity.py)
├── data-temperature-humidity.csv # Sensor data for training and predictions
└── weather.py # Python script to train model and predict future weather
```

---

## **⚙️ How It Works**

### Workflow:
1. **Arduino** (`reading-from-env.ino`)
   - Reads **humidity** and **temperature** using the DHT11 sensor.
   - Sends data through the **serial port** in CSV format.

2. **Python Data Logger** (`store-data.py`)
   - Listens to Arduino via USB serial connection.
   - Stores incoming readings with timestamps in `data-temperature-humidity.csv`.

3. **Machine Learning Model** (`weather.py`)
   - Trains a **RandomForestRegressor** on historical data.
   - Predicts future **humidity** and **temperature** for any given day.
   - Classifies weather as:
     - **Sunny**
     - **Cloudy**
     - **Rainy**

---

## **📊 Example Dataset**

Example of `data-temperature-humidity.csv`:

| timestamp           | humidity | temperature |
|---------------------|----------|-------------|
| 2025-09-01 10:00:00 | 55.4     | 24.3        |
| 2025-09-02 10:02:00 | 56.1     | 24.5        |
| 2025-09-03 10:04:00 | 54.9     | 23.8        |

---

## **🛠 Hardware Requirements**
- NodeMCU board (Your preference e.g., Arduino Uno, NodeMCU, ESP8266)
- DHT11 temperature and humidity sensor
- USB to type-B cable
- Breadboard and jumper wires

---

## **🚀 Getting Started**
- Step 1: Upload Arduino Code
  - Open `reading-from-env.ino` in Arduino IDE.
  - Select your Arduino board and COM port.
  - Upload the sketch to the Arduino.
- Step 2: Start Data Logging
  - Run the Python script `store-data.py` to read data from Arduino and save it to CSV file `data-temperature-humidity.csv`:

- Step 3: Train and Predict Weather
  - Run the weather prediction script `weather.py`:
  - Output:
    ```
    Mean Squared Error: 0.35
    R2 Score: 0.94
    
    Prediction for Day 20
    Predicted Humidity: 79.75 %
    Predicted Temperature: 20.71 °C
    Predicted Weather Condition: Cloudy
    ```

---
## **🌤 Weather Classification Rules**

| condition   | humidity (%) | temperature (°C) |
|-------------|--------------|------------------|
| Rainy       | ≥ 80         | < 25             |
| Cloudy      | 60 - 79      | 20 - 30          |
| Sunny       | < 60         | ≥ 25             |

---

## **🔗 Project Flow Diagram**
```
[NodeMCU + DHT11 Sensor]
          |
          |  (Serial Output: timestamp,humidity,temperature)
          v
[store-data.py] ---> [data-temperature-humidity.csv] ---> [weather.py]
                                                              |
                                                              v
                                                     [Predicted Weather]
                                                  (Sunny / Cloudy / Rainy)
```
---

## **🤖 Future Improvements**

- Add more features like:
  - Wind speed
  - Rainfall
  - Pressure
- Replace rule-based weather classification with RandomForestClassifier.
- Deploy predictions as a web API using Flask or FastAPI.

---

## 👨‍🎓 Developed By:
**Deepak Misal**
🔗 [LinkedIn Profile](https://www.linkedin.com/in/deepakmisal24/)  
**Adeeb Inamdar**
🔗 [LinkedIn Profile](https://www.linkedin.com/in/adeeb-m-inamdar-35531b2a2/)  
**Samarth Bhutnal**
🔗 [LinkedIn Profile](https://www.linkedin.com/in/samarth-bhutnal-523446334/)  
**Nikit Ganganagoudar**
🔗 [LinkedIn Profile](https://www.linkedin.com/in/nikit-ganganagoudar-23607033a/)  

---
