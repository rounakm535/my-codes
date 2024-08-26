import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load your data into a DataFrame
# Replace 'your_data.csv' with the actual path to your data file
df = pd.read_csv('your_data.csv')

# Splitting the data
X = df.iloc[:, :-1]  # Features (all columns except the last one)
y = df['species']    # Target variable (assuming 'species' is the target column)

train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.3, random_state=2)

# Initializing and training the Decision Tree Classifier
tree_classifier = DecisionTreeClassifier(random_state=2)
tree_classifier.fit(train_X, train_y)

# Predicting on the test set
y_pred = tree_classifier.predict(test_X)

# Calculating the accuracy score
accuracy = accuracy_score(test_y, y_pred)
print("Accuracy score:", f"{accuracy * 100:.2f}%")

# Saving the model
joblib.dump(tree_classifier, 'decision_tree_model.pkl')