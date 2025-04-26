import csv
import datetime
import os

class DatasetAccessLogger:
    def __init__(self, dataset_path, log_file="access_log.csv"):
        self.dataset_path = dataset_path
        self.log_file = log_file
        self.initialize_log()
    
    def initialize_log(self):
        if not os.path.exists(self.log_file):
            with open(self.log_file, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["timestamp", "user_id", "access_type", "data_accessed"])
    
    def log_access(self, user_id, access_type, data_accessed):
        timestamp = datetime.datetime.now().isoformat()
        with open(self.log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, user_id, access_type, data_accessed])
    
    def read_dataset(self, user_id):
        try:
            with open(self.dataset_path, 'r') as f:
                data = f.read()
            self.log_access(user_id, "read", self.dataset_path)
            return data
        except FileNotFoundError:
            self.log_access(user_id, "failed_read", self.dataset_path)
            return None
    
    def write_dataset(self, user_id, content):
        try:
            with open(self.dataset_path, 'w') as f:
                f.write(content)
            self.log_access(user_id, "write", self.dataset_path)
            return True
        except Exception as e:
            self.log_access(user_id, "failed_write", self.dataset_path)
            return False
    
    def get_access_logs(self):
        try:
            with open(self.log_file, 'r') as f:
                return list(csv.DictReader(f))
        except FileNotFoundError:
            return []

# Example usage:
# Create a sample dataset
with open('sample_data.csv', 'w') as f:
    f.write("id,name,salary\n1,Alice,50000\n2,Bob,60000")

# Initialize the logger
logger = DatasetAccessLogger('sample_data.csv')

# Simulate user access
print("Alice reads the dataset:")
print(logger.read_dataset("alice123"))

print("\nBob tries to write to the dataset:")
print("Success:", logger.write_dataset("bob456", "new,data,here"))

print("\nAccess logs:")
for log in logger.get_access_logs():
    print(log)
