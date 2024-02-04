import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Re-read the modified CSV to ensure the previous deletions are accounted for
file_path = 'table_crs.csv'
data = pd.read_csv(file_path, encoding='utf-8')

# Rename 'All programs' to 'General'
data.replace('All programs', 'General', inplace=True)

# Filter rows where the 'Program' column is 'General'
general_data = data[data['Program'] == 'General']

# Convert 'Date' column to datetime objects for plotting
general_data['Date'] = pd.to_datetime(general_data['Date'])

# Sort data by date to ensure the plot is in the correct order
general_data.sort_values('Date', inplace=True)

# Set the date as the index
general_data.set_index('Date', inplace=True)

# Create the plot
plt.figure(figsize=(10, 5))
plt.plot(general_data.index, general_data['CRS'], marker='o', linestyle='-', color='dodgerblue')

# Beautify the x-labels
plt.gcf().autofmt_xdate()
myFmt = mdates.DateFormatter('%Y-%m-%d')
plt.gca().xaxis.set_major_formatter(myFmt)

# Set titles and labels
plt.title('CRS for General', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Score', fontsize=12)

# Improve the aesthetics with grid
plt.grid(True)

# Save the plot as a .png file
plt.savefig('crs_general.png', format='png', dpi=300)

# Show the plot
plt.show()

# Provide the path for download
visualization_path = 'crs_general.png'
visualization_path
