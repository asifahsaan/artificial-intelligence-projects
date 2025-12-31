# AI Fake News Detector

## Project Description
This project is an AI-based Fake News Detection system developed as a semester project for BS Computer Science. The system uses Machine Learning and Natural Language Processing techniques to classify news articles as FAKE or REAL.

## Objective
The objective of this project is to analyze textual news data and automatically detect fake news using artificial intelligence.

## Dataset
The dataset is taken from Kaggle:
Fake and Real News Dataset

It contains two files:
- Fake.csv (fake news articles)
- True.csv (real news articles)

## Methodology
1. Load and merge fake and real news datasets
2. Preprocess text data
3. Convert text into numerical features using TF-IDF
4. Train a Naive Bayes classifier
5. Evaluate model accuracy

## Algorithm Used
- TF-IDF Vectorization
- Multinomial Naive Bayes Classifier

## Tools & Technologies
- Python
- Pandas
- Scikit-learn
- Kaggle Dataset

## Result
The model predicts whether a news article is fake or real with reasonable accuracy suitable for a semester-level AI project.

## Future Enhancements
- Use deep learning models
- Add a web interface
- Improve accuracy with larger datasets
