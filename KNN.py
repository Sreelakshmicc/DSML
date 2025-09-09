import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier

data = pd.read_csv('Dataset.csv')  

X = data[['Height', 'Weight']]
y = data['T-Shirt Size']

le = LabelEncoder()
y_encoded = le.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.3, random_state=1
)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", metrics.accuracy_score(y_test, y_pred))


print("Enter the sample data:")
h = int(input("Height in cm: "))
w = int(input("Weight in kg: "))
sample = pd.DataFrame([[h, w]], columns=['Height', 'Weight'])

pred = model.predict(sample)
pred_label = le.inverse_transform(pred)
print("Predicted T-shirt size:", pred_label[0])

