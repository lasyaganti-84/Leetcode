import requests
from bs4 import BeautifulSoup
import re

def get_faculty_emails(initial_url):
    # Function to construct full URL
    def construct_full_url(base_url, link):
        if link.startswith('http'):
            return link
        else:
            return base_url.rstrip('/') + '/' + link.lstrip('/')

    # Send GET request to the initial page
    response = requests.get(initial_url)
    response.raise_for_status()  # Check if the request was successful
    initial_page_content = response.text

    # Parse the initial page content
    soup = BeautifulSoup(initial_page_content, 'html.parser')

    # Find all faculty links
    faculty_links = soup.find_all('a', href=True)
    
    # Filter out non-faculty links (assuming they follow a specific pattern)
    faculty_links = [link['href'] for link in faculty_links if 'faculty' in link['href']]

    # List to store the emails
    emails = []

    # Iterate over each faculty link
    for link in faculty_links:
        try:
            full_url = construct_full_url(initial_url, link)
            # Send GET request to the faculty page
            faculty_response = requests.get(full_url)
            faculty_response.raise_for_status()
            faculty_page_content = faculty_response.text

            # Parse the faculty page content
            faculty_soup = BeautifulSoup(faculty_page_content, 'html.parser')

            # Extract email using regex
            email = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', faculty_page_content)

            # Add email to the list if found
            if email:
                emails.append(email[0])
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {full_url}: {e}")

    return emails

# Example usage
initial_url = 'https://www.law.ufl.edu/uflaw-faculty/faculty-and-staff-directory/tenured-and-tenure-track-faculty'  # Replace with the actual URL
emails = get_faculty_emails(initial_url)
for email in emails:
    print(email)
