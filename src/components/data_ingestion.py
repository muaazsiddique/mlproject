# src/components/data_ingestion.py
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from src.logger import logger
from src.exception import CustomException

class DataIngestion:
    def __init__(self, artifacts_dir: str = 'artifacts'):
        """
        Initializes the DataIngestion class with the dataset path and artifacts directory.
        Args:
            artifacts_dir (str): Directory where train/test data will be saved.
        """
        self.file_path = r'E:\mlproject\notebook\stud.csv'  # Define file path directly
        self.artifacts_dir = artifacts_dir
        self.train_data_path = os.path.join(self.artifacts_dir, 'train.csv')
        self.test_data_path = os.path.join(self.artifacts_dir, 'test.csv')

    def load_data(self):
        """
        Loads the dataset from the given file path.
        """
        try:
            logger.info(f"Reading dataset from: {self.file_path}")
            df = pd.read_csv(self.file_path)  # Use direct file path
            logger.info(f"Dataset loaded successfully with {df.shape[0]} rows and {df.shape[1]} columns")
            return df
        except Exception as e:
            raise CustomException(f"Error loading dataset from {self.file_path}: {str(e)}")

    def save_data(self, df):
        """
        Saves the training and test datasets into the specified artifacts directory.
        """
        try:
            # Ensure the artifacts directory exists
            os.makedirs(self.artifacts_dir, exist_ok=True)
            
            # Split the data into train and test sets
            logger.info("Splitting data into train and test sets")
            X = df.drop(columns=['math score'])  # Assuming 'total_score' is the target column
            y = df['math score']
            
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Saving the data to CSV files
            train_data = pd.concat([X_train, y_train], axis=1)
            test_data = pd.concat([X_test, y_test], axis=1)

            train_data.to_csv(self.train_data_path, index=False)
            test_data.to_csv(self.test_data_path, index=False)

            logger.info(f"Train and Test data saved at {self.artifacts_dir}")
        except Exception as e:
            raise CustomException(f"Error saving data: {str(e)}")

    def initiate_data_ingestion(self):
        """
        Handles the data ingestion process: loading and saving data.
        """
        try:
            # Load data
            df = self.load_data()

            # Save train and test data
            self.save_data(df)

            logger.info("Data ingestion completed successfully")
        except CustomException as e:
            logger.error(f"Data ingestion failed: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    data_ingestion = DataIngestion()
    data_ingestion.initiate_data_ingestion()
