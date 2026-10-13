\# Credit Card Fraud Detection Using Machine Learning



\## Project Overview



Credit Card Fraud Detection is a machine learning project designed to identify potentially fraudulent credit card transactions based on transaction-related features. The project uses classification algorithms to distinguish between legitimate and fraudulent transactions.



The project includes model training, evaluation, saved model artifacts, and a Flask-based web interface for making predictions.



\## Objectives



\- Detect potentially fraudulent transactions using machine learning.

\- Address class imbalance using Synthetic Minority Over-sampling Technique (SMOTE).

\- Train and evaluate Random Forest and XGBoost classifiers.

\- Analyze model performance using standard classification metrics.

\- Integrate the trained model with a web application for transaction prediction.



\## Technologies Used



\- \*\*Language:\*\* Python

\- \*\*Machine Learning:\*\* Scikit-learn, XGBoost

\- \*\*Imbalanced Data Handling:\*\* imbalanced-learn, SMOTE

\- \*\*Data Processing:\*\* Pandas, NumPy

\- \*\*Web Framework:\*\* Flask

\- \*\*Frontend:\*\* HTML, CSS

\- \*\*Model Storage:\*\* Joblib and XGBoost JSON serialization

\- \*\*Development Environment:\*\* Google Colab, Visual Studio Code



\## Project Structure



```text

credit-card-fraud-detector/

├── models/

│   ├── preprocessor.pkl

│   ├── xgb\_classifier.json

│   ├── fraud\_detection\_model.pkl

│   └── fraud\_detection\_model\_backup.pkl

├── notebooks/

│   └── EDPProjectNEW12Oct.ipynb

├── src/

│   └── predict.py

├── templates/

│   └── index.html

├── app.py

├── requirements.txt

├── .gitignore

└── README.md

```



\## Methodology



1\. \*\*Data Preparation:\*\* Load and prepare transaction data for model training.

2\. \*\*Data Preprocessing:\*\* Transform categorical and numerical features into a suitable format.

3\. \*\*Class Imbalance Handling:\*\* Apply SMOTE to the training data to address the imbalance between legitimate and fraudulent transactions.

4\. \*\*Model Training:\*\* Train and compare Random Forest and XGBoost classifiers.

5\. \*\*Model Evaluation:\*\* Evaluate the classifiers using accuracy, precision, recall, F1-score, and a confusion matrix.

6\. \*\*Model Export:\*\* Save the trained model and preprocessing object for later use.

7\. \*\*Web Integration:\*\* Use Flask to accept transaction details and display the model's prediction.



\## Running the Project Locally



\### 1. Clone the repository



```bash

git clone https://github.com/yuvasai6456/EDP\_WEEK\_10.git

cd EDP\_WEEK\_10

```



\### 2. Create and activate a virtual environment



On Windows:



```cmd

python -m venv .venv

.venv\\Scripts\\activate

```



\### 3. Install dependencies



```bash

pip install -r requirements.txt

```



\### 4. Run the Flask application



```bash

python app.py

```



Open the following address in your browser:



`http://127.0.0.1:5000`



\## Evaluation Metrics



The training notebook evaluates model performance using:



\- Accuracy

\- Precision

\- Recall

\- F1-score

\- Confusion Matrix



Actual metric values should be taken from the completed model evaluation results.



\## Project Workflow



```mermaid

flowchart TD

&#x20;   A\[Transaction Dataset] --> B\[Data Preprocessing]

&#x20;   B --> C\[Train-Test Split]

&#x20;   C --> D\[SMOTE Class Balancing]

&#x20;   D --> E\[Random Forest and XGBoost Training]

&#x20;   E --> F\[Model Evaluation]

&#x20;   F --> G\[Save Trained Model]

&#x20;   G --> H\[Flask Web Application]

&#x20;   H --> I\[Enter Transaction Details]

&#x20;   I --> J\[Fraud Prediction]

&#x20;   J --> K\[Display Result]

```



\---



\### Developed By



\*\*G. Yuva Sai\*\*







