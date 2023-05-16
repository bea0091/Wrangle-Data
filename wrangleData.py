import pandas as pd

# set display options to show all rows
pd.set_option('display.max_rows', None)

# Read JSON file into pandas DataFrame
df = pd.read_json('session.json', lines=True)

# Group the data by attacker country, IP, OS, and port
grouped_data = df.groupby(['source_ip', 'destination_ip', 'honeypot', 'source_port', 'destination_port'])['protocol'].count()

# Sort the results by the number of times each attacker IP/port combination was attacked
sorted_data = grouped_data.reset_index().sort_values('protocol', ascending=False)

# Add a new column to display the count of attacks for each IP/port combination
sorted_data['attack_count'] = sorted_data['protocol']

# Print the sorted results
print(sorted_data[['source_ip', 'destination_ip', 'honeypot', 'source_port', 'destination_port', 'attack_count']])

