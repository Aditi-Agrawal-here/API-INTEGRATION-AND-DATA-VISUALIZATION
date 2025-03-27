# API-INTEGRATION-AND-DATA-VISUALIZATION

*COMPANY* : CODTECH IT SOLUTIONS

*NAME* : ADITI AGRAWAL

*INTERN ID* : CT08OCS

*DOMAIN* : PYTHON PROGRAMMING

*DURATION* : 4 WEEKS

*MENTOR* : NEELA SANTOSH


## API Integration and Data Visualization – OpenWeatherMap

About This Project:

This project focuses on fetching real-time weather data from the OpenWeatherMap API and visualizing it using Python, Pandas, Matplotlib, and Seaborn. The script retrieves weather details such as temperature, humidity, and wind speed for multiple cities, processes the data, and generates bar charts for better insights.


Key Features:
1) Fetches real-time weather data using OpenWeatherMap API.
2) Processes JSON responses and stores the data in a structured CSV file.
3) Visualizes weather trends using Matplotlib & Seaborn.
4) Includes error handling for failed API requests.


How It Works:
1) Fetch Data: The script sends an API request to OpenWeatherMap for multiple cities.
2) Extract Information: It parses JSON data to extract temperature, humidity, and wind speed.
3) Save to CSV: The extracted data is stored in weather_data.csv.
4) Visualize Data: Seaborn generates bar charts comparing the weather conditions of different cities.


Technologies Used:
1) Python
2) Urllib (for API requests)
3) JSON (for data parsing)
4) Pandas (for structured data handling)
5) Matplotlib & Seaborn (for visualization)


Installation and Usage:
1) Clone the repository
   git clone https://github.com/Aditi-Agrawal-here/API-INTEGRATION-AND-DATA-VISUALIZATION
   cd API-INTEGRATION-AND-DATA-VISUALIZATION
2) Install the required libraries
   pip install matplotlib seaborn pandas
3) Run the script
   python openweathermap.py
4) Check the output
   weather_data.csv (stores the fetched weather data).
   Graphs visualizing temperature, humidity, and wind speed.


Output Files:

weather_data.csv – Stores the fetched weather data in tabular format. 

[weather_data.csv](https://github.com/user-attachments/files/18931215/weather_data.csv)

Generated Graphs 
1) Temperature
    ![Image](https://github.com/user-attachments/assets/fd31e2bf-fb4d-49c0-9750-6bae1c80d966)
3) Humidity
    ![Image](https://github.com/user-attachments/assets/4d982d16-b2ed-4c60-8db0-5ae111194dfc)
4) Wind speed
    ![Image](https://github.com/user-attachments/assets/7497c183-c300-4a90-bf93-7e896f0babde)


Challenges Faced and Learnings:
1) Handling API Responses – Extracting relevant weather details from JSON data.
2) Visualization Techniques – Choosing the best graphs for weather comparisons.
3) Error Handling – Managing API failures and invalid city names.
4) Library Dependencies – Ensuring proper installation of required libraries.

Conclusion:

This project provided a hands-on experience with API integration, data processing, and data visualization. Working with OpenWeatherMap API allowed me to understand real-world data handling and how to present insights visually in an effective way.

