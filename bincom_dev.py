from bs4 import BeautifulSoup

# Define the file path
file_path = 'chat_bot/bincom_dev/bincom.html'

# Load the HTML content from the file
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the table in the HTML
table = soup.find('table')

# Initialize an empty dictionary to store the table content
table_dict = {}

# Iterate over the rows in the table body
for row in table.find('tbody').find_all('tr'):
    tds = row.find_all('td')
    day = tds[0].text.strip()
    colors = [color.strip() for color in tds[1].text.split(',')]
    
    # Add the day and colors to the dictionary
    table_dict[day] = colors

# Print the resulting dictionary
if __name__ == "__main__":
    print(table_dict)