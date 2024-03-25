# Real-Time Fraud Detection Model

This project focuses on developing a real-time machine learning model to predict fraudulent transactions effectively. By leveraging a dataset comprising various transactional features such as amount, category, merchant information, location, gender, and timestamps, we aim to identify fraudulent activities as they occur, ensuring prompt action to mitigate potential losses.

## Datasets 

The selected datasets used in this project includes the following columns:
- `amt`: Transaction amount
- `category`: Transaction category
- `merchant`: Merchant information
- `merch_long`: Merchant longitude
- `merch_lat`: Merchant latitude
- `state`: State information
- `gender`: Gender of the transaction initiator
- `new_unix`: Time and date stamp of the transaction

## Model Deployment

The model has been successfully created and deployed using Streamlit. You can access the deployed application on Streamlit Share via the link:
[Streamlit App](https://fraudchecker.streamlit.app/)

## Steps Taken

1. Data Collection: I gathered a comprehensive dataset containing transactional features necessary for fraud detection, including transaction amount, category, merchant details, location, gender, and time and date stamps.

2. Data Preprocessing: Preprocessing steps involved handling missing values, encoding categorical variables, scaling numerical features, and potentially performing feature engineering to enhance model performance.

3. Model Selection: After thorough experimentation, I selected an appropriate machine learning algorithm suitable for real-time fraud detection tasks. The chosen algorithm used was XGBoost which was capable of handling high-dimensional data and exhibiting strong predictive performance.

4. Model Training: The selected model was trained on the preprocessed dataset to learn patterns indicative of fraudulent transactions. We ensured the model was trained on a diverse set of data to generalize well to unseen instances.

5. Model Evaluation: The model's performance was evaluated using relevant evaluation metrics, with a particular focus on achieving 100% accuracy in predicting fraudulent transactions while minimizing false positives.

6. Model Deployment: Upon satisfactory evaluation results, the model was deployed using Streamlit, enabling real-time predictions through an intuitive user interface. The deployed application provides users with immediate insights into potentially fraudulent transactions.

## Future Improvements

- Continuously updating the model with new data to adapt to evolving fraud patterns and maintain high accuracy.
- Incorporating advanced techniques such as anomaly detection or ensemble methods to further enhance model performance.
- Enhancing the user interface of the deployed application to provide more interactive and informative features.


Feel free to contribute to this project by forking the repository, making improvements, and creating pull requests!

