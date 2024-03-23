# Sentiment Analysis of Real time Flipkart Product Reviews

<p align="center">
    <img width="800" src="https://github.com/HannahIgboke/Sentiment-Analysis-of-Real-time-Flipkart-Product-Reviews/blob/main/Files/Flipkart.jpg" alt="Flipkart">
</p>


[Flipkart Private Limited](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.flipkart.com/&ved=2ahUKEwjU_pnGqIiFAxWnRUEAHekzBeEQ-TAoAHoECFcQAQ&usg=AOvVaw0v_i-rdbD-oVZOBoKBuRP8) is an Indian e-commerce company headquartered in Bangalore. The company initially focused on online book sales before expanding into other product categories, including consumer electronics, fashion, home essentials, groceries, and lifestyle products. Flipkart has grown rapidly over the years, making strategic mergers and acquisitions and maximizing data to understand and create a personalized user experience.

A team of Data Engineers has scraped real-time data from the Flipkart website. The dataset consists of 8,518 reviews for the "YONEX MAVIS 350 Nylon Shuttle" product from Flipkart. Each review includes features such as Reviewer Name, Rating, Review Title, Review Text, Place of Review, Date of Review, Up Votes, and Down Votes.


# Objectives
The objective of this project is to classify customer reviews as either positive or negative and and identify the best model fit for this sentiment analysis and further understand the pain points of customers who write negative reviews. In view of this, the specific objectives and workflow for this project is as follows:


1. Data Loading and Exploratory Data Analysis
  
2. Data Preprocessing: text Cleaning, normalization and numerical Feature Extraction

3. Model Training

4. Model Evaluation of the trained models using the F1-Score metric.

5. Develop a Flask web application for sentiment analysis of user-provided reviews.

6. Model Deployment: Deploy the trained sentiment classification model along with the Flask app on an AWS EC2 instance.

7. Testing and Monitoring: Test the deployed application and monitor its performance for any issues or errors.


A detailed view of the exploratory data analysis, data preprocessing, model training and evaluation are contained in my notebook [here](https://github.com/HannahIgboke/Sentiment-Analysis-of-Real-time-Flipkart-Product-Reviews/blob/main/Files/Product%20review%20classifier.ipynb).

The files for the web application developmentg can be found [here](https://github.com/HannahIgboke/Sentiment-Analysis-of-Real-time-Flipkart-Product-Reviews/tree/main/Files).


# Tech Stack used🛠

- Python
- Flask
- HTML
- CSS

The end product of this project is an interactive web application that takes in three inputs from the user - reviewer name, product purchased and the review on the product. This can be seen below:

<p align="center">
    <img width="800" src="https://github.com/HannahIgboke/Sentiment-Analysis-of-Real-time-Flipkart-Product-Reviews/blob/main/Files/Welcome.JPG" alt="Welcome">
</p>


When the user clicks predict, the web application having been connected to the model built, classifies their review and outputs the results of the sentiment analysis such as below:

<p align="center">
    <img width="800" src="https://github.com/HannahIgboke/Sentiment-Analysis-of-Real-time-Flipkart-Product-Reviews/blob/main/Files/sentiment%20page.JPG" alt="Sentiment analysis">
</p>


🔗You can try out the product review sentiment analyser web app I created [here](http://54.83.112.9:5000/).


# Conclusion

In this project I successfully built a product review classifier for Flipkart leveraging various libraries and models like Bag of Words, Random Forest, Logsitic Regression, etc and creating a pipleine for efficienct hyper parameter tuning to obtain the best possible model. I further integrated the trained sentiment classification model into the Flask app for real-time inference and deployed the app on an AWS EC2 instance to make it accessible over the internet.








