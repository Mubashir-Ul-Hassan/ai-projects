# Import RandomForestClassifier from scikit-learn
from sklearn.ensemble import RandomForestClassifier

# Create the Random Forest model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the Random Forest model
rf_model.fit(X_train, y_train)

# Make predictions using the Random Forest model
y_pred_rf = rf_model.predict(X_test)

# Evaluate the Random Forest model
accuracy_rf = accuracy_score(y_test, y_pred_rf)
conf_matrix_rf = confusion_matrix(y_test, y_pred_rf)

# Compare Random Forest accuracy with Logistic Regression
print(f'Random Forest Accuracy: {accuracy_rf * 100:.2f}%')
print('Random Forest Confusion Matrix:')
print(conf_matrix_rf)
