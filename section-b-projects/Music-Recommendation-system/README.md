**Project Title**

**Music Recommendation and Popularity Prediction System Using Spotify Dataset**

This project focuses on analyzing musical attributes from a large Spotify dataset to understand music trends and predict song popularity using machine learning techniques. The project also classifies songs based on emotional and acoustic features, which helps in building a foundation for intelligent music recommendation systems.

**Student Name(s)**

**Muhammad Hashir , Muhammad Talha Tabish , Umair Yousaf , Zohaib hassan**   
*(70137237, 70138652,70137484,70138058.)*

This project is developed as part of an academic requirement and demonstrates the application of data science and machine learning concepts to real-world music data.

**Problem Statement**

With the rapid growth of online music streaming platforms, users are exposed to millions of songs, making it difficult to discover music that matches their preferences and mood. Traditional music recommendation approaches often rely on basic popularity metrics and fail to consider detailed audio features such as mood, energy, and acoustic properties. The problem addressed in this project is the lack of effective analysis that links musical features with song popularity. This project aims to solve this problem by analyzing Spotify audio features and using machine learning models to predict song popularity and classify songs based on mood and acousticness.

**Dataset Source (with link)**

The dataset used in this project is the **Spotify Music Dataset**, which contains detailed audio features and metadata for over 155,000 songs. The dataset includes attributes such as valence, energy, danceability, acousticness, tempo, loudness, and popularity. It covers music released across multiple decades, making it suitable for trend analysis and machine learning applications.

**Dataset Link:**  
**https://www.kaggle.com/datasets/mohamedjamyl/music-recommendation-system-datasets/data?select=Music+Recommendation+System+using+Spotify+Dataset.csv**

**Model / Technique Used**

This project treats song popularity prediction as a **regression problem**. Multiple machine learning models are used to analyze and compare performance. These include Decision Tree Regressor, Gradient Boosting Regressor, and XGBoost Regressor. Feature engineering techniques are applied to classify songs based on valence (mood) and acousticness. Exploratory Data Analysis is also performed using visualization techniques to understand feature distributions and correlations. Among the tested models, ensemble-based techniques, especially XGBoost, show superior performance in predicting song popularity.

**How to Run the Project**

To run this project, first open Google Colab or any Python-supported IDE such as Jupyter Notebook. Upload the Spotify dataset CSV file to the working directory. Install the required Python libraries, including Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, and XGBoost. Execute the notebook cells in sequence, starting from data loading and preprocessing, followed by exploratory data analysis, feature engineering, model training, and evaluation. Ensure that the dataset file path is correctly specified before running the code. The output results, graphs, and model performance metrics will be displayed after successful execution.

**Results (Metrics and Screenshots)**

The performance of the machine learning models is evaluated using standard regression metrics such as R-squared score, Root Mean Square Error (RMSE), and Mean Absolute Error (MAE). The results show that the XGBoost Regressor achieves the highest accuracy with better R-squared values and lower error rates compared to Gradient Boosting and Decision Tree models. Visualization results such as correlation heatmaps, scatter plots, box plots, and popularity distribution graphs further support the analysis. Screenshots of these outputs, including graphs and metric results, can be included in the final report to demonstrate model performance and data insights.

**References (if any)**

Spotify Music Dataset – Kaggle  
Scikit-learn Documentation  
XGBoost Documentation  
Python Data Science Libraries Documentation

