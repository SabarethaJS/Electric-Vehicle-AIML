Electric Vehicle Type Classification using Machine Learning

Introduction

This project is developed as a part of my AICTE Internship on Artificial Intelligence and Machine Learning (AIML) under the theme *Electric Vehicles (EVs)*.
The goal of this project is to apply machine learning techniques to analyze electric vehicle data and build a predictive model that can classify the types of electric vehicles based on several key parameters.
This project highlights the importance of data-driven approaches in understanding EV performance, specifications, and market trends.

Problem Statement

The growing demand for sustainable transportation has accelerated the adoption of electric vehicles. However, classifying electric vehicles accurately based on their specifications, model type, range, and battery capacity is essential for both manufacturers and researchers.
This project aims to build a simple yet efficient machine learning model that can classify different types of electric vehicles using structured data from a publicly available dataset.

 Objective

* To explore how AI and ML can be implemented in the field of electric vehicles.
* To classify electric vehicles based on their specifications and performance parameters.
* To preprocess and analyze EV-related data to understand relationships between features such as model year, range, and battery capacity.
* To visualize patterns and correlations that could assist in the improvement of EV technology and design.


 Importance of the Project

Electric vehicles are a major step toward reducing pollution and dependency on fossil fuels.
Machine learning enables automation in vehicle analysis, helps predict performance, and assists industries in decision-making.
This project acts as a small-scale model for understanding how AI-powered classification systems can be integrated into real-world electric mobility analytics.

Dataset Description

The dataset used in this project has been downloaded from Kaggle. It contains detailed information about electric vehicles including:

* Vehicle ID
* Manufacturer (Make)
* Model Name
* Model Year
* Electric Vehicle Type (Battery Electric or Plug-in Hybrid)
* Electric Range
* Base MSRP (Manufacturer Suggested Retail Price)
* Legislative District and Vehicle Location
* Clean Alternative Fuel Vehicle Eligibility

The dataset is uploaded in this GitHub repository for easy access during model training and testing.

Methodology

The overall workflow of this project is divided into multiple stages:

1. **Dataset Collection:**

   * The dataset was collected from Kaggle’s “Electric Vehicle Population Data” repository.

2. **Data Upload and Storage:**

   * The dataset file was uploaded to this GitHub repository for version control and reproducibility.

3. **Data Understanding:**

   * The dataset structure and attributes were studied to understand feature relationships and their significance.

4. **Preprocessing (Week 2):**

   * The dataset will be cleaned, null values will be handled, and categorical data will be encoded.

5. **Model Building (Week 2):**

   * A classification algorithm (like Logistic Regression, Decision Tree, or Random Forest) will be implemented to classify EVs.

6. **Model Evaluation (Week 2):**

   * Model accuracy and performance metrics such as precision, recall, and F1-score will be analyzed.

Week 1 Activities Completed

* Selected the theme: *Electric Vehicles*.
* Finalized the project title: **Electric Vehicle Type Classification using Machine Learning.**
* Downloaded the dataset from Kaggle.
* Uploaded the dataset to the GitHub repository.
* Understood dataset attributes and identified features for classification.
* Created README documentation to describe the project objective and workflow.

Tools and Technologies Used

| Category             | Tools/Technologies                        |
| -------------------- | ----------------------------------------- |
| Programming Language | Python                                    |
| Development Platform | Jupyter Notebook                          |
| Libraries            | Pandas, NumPy, Matplotlib, Scikit-learn   |
| Version Control      | Git and GitHub                            |
| Dataset Source       | Kaggle (Electric Vehicle Population Data) |

Expected Outcomes

* To develop a machine learning model capable of classifying electric vehicle types.
* To understand key features that influence electric vehicle categorization.
* To visualize relationships between vehicle specifications and type classifications.
* To contribute to the growing research in sustainable mobility and intelligent vehicle systems.


 Applications

* EV manufacturing analytics and optimization.
* Government policy planning for EV incentives.
* Market trend analysis and forecasting.
* Academic and industrial research on electric vehicle datasets.

 Conclusion

This project provides a foundation for integrating AI and ML in the field of electric vehicles.
By analyzing real-world EV datasets, the project aims to demonstrate how predictive modeling can support the design, classification, and enhancement of EV systems.
This work will also enhance understanding of data preprocessing, model selection, and evaluation in practical AIML applications.


 Week 2: Machine Learning Model Training

Objective

The goal of this week’s task is to train a **Machine Learning model** that can analyze and classify electric vehicles based on various attributes such as make, model, range, and price. This helps in understanding how data-driven insights can be applied in the electric vehicle domain.

Steps Performed

1. Data Loading:

   * Uploaded and read the dataset `Electric_Vehicle_Population_Data.csv` using `pandas`.
   * Performed initial exploration of data to understand column types and value distribution.

2. Data Preprocessing:

   * Handled missing values and removed unnecessary columns.
   * Encoded categorical data such as *Make* and *Model* using `LabelEncoder`.
   * Normalized numeric columns like *Electric Range* and *Base MSRP (Price)* for better model accuracy.

3. Feature Selection:

   * Selected relevant columns for training:

     ```
     [Make, Model, Electric Range, Base MSRP]
     ```
   * Target variable:

     ```
     Electric Vehicle Type (BEV or PHEV)
     ```

4. Model Training:

   * Split dataset into **Training (80%)** and **Testing (20%)** sets using `train_test_split`.
   * Trained a **Random Forest Classifier** to predict the type of electric vehicle.

5. Model Evaluation:

   * Calculated **Accuracy**, **Confusion Matrix**, and **Classification Report**.
   * Displayed results to measure how well the model performs on unseen data.

6. **Prediction:**

   * Tested the model by predicting the vehicle type for a **new sample input** (for example, Tesla Model 3).
   * Displayed the prediction as either:

     
     0 → BEV (Battery Electric Vehicle)
     1 → PHEV (Plug-in Hybrid Electric Vehicle)
   
 Results

* The trained machine learning model achieved an **accuracy of 99%** on the test dataset.
* The model successfully predicted the type of electric vehicle based on its specifications.

 Tools & Technologies Used

* **Python**
* **Google Colab**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Matplotlib / Seaborn (optional for visualization)**

 Conclusion

This week’s task demonstrated how to build and train a machine learning model using real-world electric vehicle data.
By preprocessing data, training a classification model, and evaluating accuracy, we gained insights into how ML can help in analyzing and categorizing EVs efficiently.

