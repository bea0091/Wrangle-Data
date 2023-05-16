import pandas as pd

# set display options to show all rows
pd.set_option('display.max_rows', None)

# Read JSON file into pandas DataFrame
df = pd.read_json('session.json', lines=True)

# Group the data by the source IP
grouped_data = df.groupby(['source_ip'])['protocol'].agg([('attack_count', 'count')])

# Sort the results by the number of times each source IP was attacked and select the top 5
sorted_data = grouped_data.reset_index().sort_values('attack_count', ascending=False).head(5)

# Print the sorted results
print(sorted_data[['source_ip', 'attack_count']])

