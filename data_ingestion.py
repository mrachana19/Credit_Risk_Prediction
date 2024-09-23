
import boto3
import json
import pandas as pd

# AWS configuration
aws_region = 'us-west-2'  # Replace with your preferred AWS region
stream_name = 'credit-risk-assessment-stream'  # Replace with your desired stream name

# Initialize Kinesis client
kinesis_client = boto3.client('kinesis', region_name=aws_region)

def create_kinesis_stream(stream_name):
    """
    Create a Kinesis stream if it doesn't exist.
    """
    try:
        response = kinesis_client.create_stream(
            StreamName=stream_name,
            ShardCount=1
        )
        print(f"Stream {stream_name} created successfully.")
    except kinesis_client.exceptions.ResourceInUseException:
        print(f"Stream {stream_name} already exists.")
    except Exception as e:
        print(f"Error creating stream: {e}")

def put_record_to_stream(stream_name, data):
    """
    Put data into the Kinesis stream.
    """
    try:
        response = kinesis_client.put_record(
            StreamName=stream_name,
            Data=json.dumps(data),
            PartitionKey=str(data['customer_id'])  # Use customer_id or any unique field as the partition key
        )
        print("Record added to stream:", response)
    except Exception as e:
        print(f"Error putting record to stream: {e}")

def ingest_data_from_csv(csv_file_path):
    """
    Read data from a CSV file and ingest it into the Kinesis stream.
    """
    try:
        # Read the CSV file
        df = pd.read_csv(csv_file_path)
        
        # Iterate over each row in the DataFrame and send to Kinesis
        for index, row in df.iterrows():
            record = row.to_dict()  # Convert each row to a dictionary
            put_record_to_stream(stream_name, record)
    except Exception as e:
        print(f"Error reading or processing CSV file: {e}")

if __name__ == "__main__":
    # Create the Kinesis stream
    create_kinesis_stream(stream_name)
    
    # Path to your CSV file (replace with the correct path)
    csv_file_path = 'data/credit_risk_data.csv'  # Make sure this path is correct and accessible
    
    # Ingest data from the CSV file
    ingest_data_from_csv(csv_file_path)
