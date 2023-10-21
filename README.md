Checkpoint Objective
Write a Pandas program to create and display a DataFrame from the following dictionary data with index labels.

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],

'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],

'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],

'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

Instructions
Print the three first rows using the head() method.
Delete rows with Nan values.
Extract the 'name' and 'score' columns from the DataFrame.
Write a Pandas program to append a new row 'k' to the DataFrame with these values (name: "Suresh", score: 15.5, attempts: 1, qualify: "yes").
Write a Pandas program to delete the 'attempts' column from the DataFrame.
Add a new column "Success": if the score is higher than 10 we will have 1, else we will have 0.
After executing the final DataFrame, export it into a CSV file named "my_data".
Time to practice, take your time!
