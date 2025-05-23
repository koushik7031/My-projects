# 🌐 Web Page Classification Using Machine Learning

This project focuses on classifying web pages into various categories such as Business, Sports, Technology, etc., using Natural Language Processing (NLP) and Machine Learning (ML). It is a complete end-to-end ML pipeline involving data cleaning, feature extraction, model training, evaluation, and visualization.

---

## 📌 Problem Statement

Automatically classify the category of a web page based on its content. This helps in organizing, filtering, and recommending content at scale.

---

## 📂 Dataset

- The dataset consists of raw HTML content of web pages and their associated category labels.
- Categories include: Business, Education, Sports, Technology, and more.

---

## 🧠 Techniques & Tools Used

- **Libraries**: Python, Scikit-learn, Pandas, NumPy, BeautifulSoup, Matplotlib, Seaborn
- **NLP**: Text extraction, cleaning, tokenization, stopword removal
- **Feature Engineering**: TF-IDF vectorization
- **Modeling**: Logistic Regression, Support Vector Machines (SVM), Naive Bayes
- **Evaluation**: Accuracy, Confusion Matrix, Precision, Recall, F1-Score
- **Visualization**: Matplotlib, Seaborn

---

## 🔍 Project Workflow

1. **Data Cleaning**  
   - Clean up the data using regex 
   - Lowercased, removed punctuation, numbers, and stopwords  

2. **Feature Extraction**  
   - Transformed cleaned text using `TfidfVectorizer`  

3. **Model Training**  
   - Trained multiple ML models  
   - Tuned hyperparameters using GridSearchCV  

4. **Model Evaluation**  
   - Evaluated performance using accuracy, precision, recall, and F1-score  
   - Visualized confusion matrix  

5. **Result**  
   - Best-performing model achieved **XX% accuracy** on the test set (replace with actual)

---

📈 Results

- The Linear Regression model provided the best overall classification accuracy.  
- TF-IDF effectively captured meaningful word importance.  
- Significant differences observed between categories in misclassification rates
