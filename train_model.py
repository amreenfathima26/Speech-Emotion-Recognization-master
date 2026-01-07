import os
import sys
import numpy as np
import joblib
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from utilities import load_data

def train_and_save_model(data_path="data", model_path="model.pkl"):
    print(f"[*] Loading data from {data_path}...")
    # Load data
    x_train, x_test, y_train, y_test = load_data(data_path=data_path, test_size=0.25)
    
    if len(x_train) == 0:
        print("[!] No data found or data loading failed.")
        print("    Please ensure you have the RAVDESS dataset in the 'data' folder")
        print("    or a compatible structure (Actor_* folders with .wav files).")
        print("    Skipping training. The app will run in Demo Mode.")
        return

    # Initialize the Multi Layer Perceptron Classifier
    model = MLPClassifier(alpha=0.01, batch_size=256, epsilon=1e-08, hidden_layer_sizes=(300,), learning_rate='adaptive', max_iter=500)

    # Train the model
    print("[*] Training model...")
    model.fit(x_train, y_train)

    # Predict for the test set
    y_pred = model.predict(x_test)

    # Calculate the accuracy of our model
    accuracy = accuracy_score(y_true=y_test, y_pred=y_pred)
    print(f"[*] Model Accuracy: {accuracy*100:.2f}%")

    # Save the model
    print(f"[*] Saving model to {model_path}...")
    joblib.dump(model, model_path)
    print("[*] Done!")

if __name__ == "__main__":
    # You can pass the data path as an argument
    path = "data"
    if len(sys.argv) > 1:
        path = sys.argv[1]
    train_and_save_model(data_path=path)
