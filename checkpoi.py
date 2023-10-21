import pandas as pd
import numpy as np

# Create the DataFrame
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels)

# Print the first three rows using the head() method
print("First three rows:")
print(df.head(3))

# Delete rows with NaN values
df = df.dropna()

#Extract the 'name' and 'score' columns
name_score_df = df[['name', 'score']]

#Append a new row 'k' to the DataFrame
new_row = {'name': "Suresh", 'score': 15.5, 'attempts': 1, 'qualify': "yes"}
df = df._append(new_row, ignore_index=True)

#Delete the 'attempts' column
df = df.drop(columns=['attempts'])

#Add a new column "Success"
df['Success'] = np.where(df['score'] > 10, 1, 0)

#Export the DataFrame to a CSV file named "my_data"
df.to_csv("my_data.csv", index=False)

# Display the final DataFrame
print("\nFinal DataFrame:")
print(df)
