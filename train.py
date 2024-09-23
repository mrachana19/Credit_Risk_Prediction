
import argparse
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, roc_auc_score
import joblib
import os

def model_training(args):
    # Load the data from the training channel
    train_data = pd.read_csv(args.train)

    # Split into features and target
    X = train_data.drop(['default_status'], axis=1)
    y = train_data['default_status']

    # Initialize and train the model
    model = LogisticRegression(max_iter=200, random_state=42)
    model.fit(X, y)

    # Evaluate the model (for offline evaluation)
    predictions = model.predict(X)
    accuracy = accuracy_score(y, predictions)
    precision = precision_score(y, predictions)
    recall = recall_score(y, predictions)
    auc = roc_auc_score(y, model.predict_proba(X)[:, 1])

    print(f"Training Metrics: Accuracy = {accuracy}, Precision = {precision}, Recall = {recall}, AUC = {auc}")

    # Save the trained model to the specified output directory
    joblib.dump(model, os.path.join(args.model_dir, "model.joblib"))

if __name__ == "__main__":
    # Argument parser for SageMaker-specific arguments
    parser = argparse.ArgumentParser()

    # Sagemaker specific arguments
    parser.add_argument("--train", type=str, default=os.environ.get("SM_CHANNEL_TRAIN"))
    parser.add_argument("--model-dir", type=str, default=os.environ.get("SM_MODEL_DIR"))

    args = parser.parse_args()

    # Train the model
    model_training(args)
