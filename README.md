# NY Uber Trips and Weather Data Analysis

This repository contains a comprehensive analysis combining Uber trip data and weather conditions in New York City from April to September 2014. The analysis aims to identify insights into Uber usage patterns in relation to daily weather conditions, utilizing Python, SQL, and Tableau.

## 📂 Project Structure

```
NY-UberTrips-Weather-Analysis
├── data/
│   ├── uber-raw-data-apr14.csv
│   ├── uber-raw-data-may14.csv
│   ├── uber-raw-data-jun14.csv
│   └── weather-data.csv
├── sql/
│   ├── data_preparation.sql
│   └── data_quality_checks.sql
├── tableau/
│   └── UberWeatherDashboard.twbx
├── qa/
│   └── Quality_Assurance_Document.pdf
└── scripts/
    └── data_cleaning.py
```

## 🚀 Project Overview

This project:
- Combines multiple Uber datasets with New York JFK daily weather data.
- Utilizes a relational database (MySQL/MSSQL) to create structured working tables.
- Provides insights into how weather conditions impact Uber usage.
- Presents insights effectively through a Tableau dashboard.

## 🔧 Tools and Technologies Used

- **Python**: Data cleaning, manipulation, and preliminary analysis
- **SQL (MySQL/MSSQL)**: Data structuring, joining, and quality assurance
- **Tableau**: Data visualization and dashboard creation

## 📊 Tableau Dashboard

The final Tableau dashboard (`UberWeatherDashboard.twbx`) presents:
- Daily and monthly patterns of Uber trips
- Correlation between weather conditions (rain, temperature, etc.) and Uber usage
- Interactive elements for exploring trends and details

## ✅ Quality Assurance

A detailed QA document (`Quality_Assurance_Document.pdf`) ensures:
- Data completeness
- Consistency between raw and processed data
- Verification steps clearly documented

## 🛠️ Setup and Usage

### Step 1: Clone Repository

```bash
git clone https://github.com/Jingfei-li/NY-UberTrips-Weather-Analysism.git
cd NY-UberTrips-Weather-Analysis
```
### Step 2: Data Cleaning (Python)

Run the Python script to perform any additional cleaning:

```bash
python scripts/data_cleaning.py
```

### Step 3: Working Table (SQL)

1. Import CSV files into your SQL database.
2. Run `data_preparation.sql` to create and populate working tables.



### Step 4: Tableau Dashboard

- Open `UberWeatherDashboard.twbx` in Tableau.
- Explore interactive visualizations.


## 📜 License

This project is licensed under the MIT License.
