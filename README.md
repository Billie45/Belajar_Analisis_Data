# Bike Sharing Dashboard 
This dashboard displays bike sharing data analysis, including rental trends by weekday, weekend, holiday, and casual versus registered users. The dashboard was created using Streamlit and visualizes the analysis data.

## Installation
To set up and run the dashboard locally, follow these steps:

1. Clone this repository to your local machine:
```
git clone https://github.com/Billie45/Belajar_Analisis_data.git
```
2. Navigate to the project directory:
```
cd submission
```
3. Install the required packages listed in the requirements.txt file:
```
pip install -r requirements.txt
```
4. Run the dashboard using Streamlit:
```
streamlit run ./dashboard/dashboard.py
```
5. Access the dashboard using web browser at:
```
http://localhost:8501
```

## Directory Structure
```
submission/
├── dashboard/
│   └── dashboard.py  
│   └── clean_day.py 
│   └── clean_hour.py 
├── data/
│   ├── day.csv        
│   └── hour.csv       
├── README.md                
├── requirements.txt        
└── notebook.ipynb   
└── url.txt
```

## Requirements
Ensure you have Python 3.x installed, with this libraries:

- pandas
- seaborn
- streamlit
- matplotlib
- numpy

All dependencies are listed in the requirements.txt file and can be installed using the command mentioned above.

## Usage
**1. Data Wrangling:**

The data wrangling steps are available in the notebook.ipynb file. These steps include gathering, assessing, and cleaning the bike sharing dataset for analysis.

**2. Exploratory Data Analysis (EDA):**

Explore and analyze the bike rental data using the notebook.ipynb. This analysis show of the rental patterns, such as differences between weekdays, weekends, holidays, and user types (casual vs. registered).

**3. Visualization:**

Run the Streamlit dashboard for interactive visual exploration of the data. This give visual about weekday vs. weekend, holiday effects, and a comparison between casual and registered users.

## License
This project is licensed under the MIT License.
