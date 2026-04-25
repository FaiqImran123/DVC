import os
import pandas as pd

# Step 1: Create folder if it doesn't exist
folder_name = "data"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Step 2: Create sample DataFrame
data = {
    "id": [1, 2, 3, 4],
    "name": ["Ali", "Sara", "Ahmed", "Ayesha"],
    "score": [85, 90, 78, 92]
}

df = pd.DataFrame(data)

# Step 3: Save to CSV inside data folder
file_path = os.path.join(folder_name, "sample_data.csv")
df.to_csv(file_path, index=False)

print("Data saved successfully at:", file_path)