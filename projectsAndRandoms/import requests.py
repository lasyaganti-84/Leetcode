import requests
from bs4 import BeautifulSoup
import re

# URL of the webpage
url = 'https://anthro.ufl.edu/people/faculty/'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all email addresses using regular expressions
email_pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')


# Extract email addresses
emails = set()
for tag in soup.find_all('a', href=True):
    email_matches = email_pattern.findall(tag['href'])
    for email in email_matches:
        emails.add(email)

# Print the extracted emails
for email in emails:
    print(email)
