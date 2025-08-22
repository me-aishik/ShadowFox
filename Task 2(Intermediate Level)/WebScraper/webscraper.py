import requests
from bs4 import BeautifulSoup
import json
import csv
from datetime import datetime
import os
import time

class WebScraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.session = requests.Session()
        self.create_data_directory()

    def create_data_directory(self):
        """Create directories for storing scraped data"""
        directories = ['json_data', 'csv_data', 'logs']
        for directory in directories:
            if not os.path.exists(directory):
                os.makedirs(directory)

    def log_error(self, error_message):
        """Log errors to a file"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {error_message}\n"
        with open('logs/error_log.txt', 'a', encoding='utf-8') as f:
            f.write(log_entry)

    def scrape_website(self, url, selectors):
        """
        Scrape data from a website using provided CSS selectors
        
        Args:
            url (str): The URL to scrape
            selectors (dict): Dictionary of CSS selectors for different elements
        """
        try:
            # Add delay to be respectful to the website
            time.sleep(2)
            
            # Make the request
            response = self.session.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Dictionary to store scraped data
            data = {
                'url': url,
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'data': {}
            }
            
            # Extract data using provided selectors
            for key, selector in selectors.items():
                elements = soup.select(selector)
                data['data'][key] = [elem.text.strip() for elem in elements]
            
            return data
            
        except requests.exceptions.RequestException as e:
            error_msg = f"Failed to fetch {url}: {str(e)}"
            self.log_error(error_msg)
            return None
            
        except Exception as e:
            error_msg = f"Error scraping {url}: {str(e)}"
            self.log_error(error_msg)
            return None

    def save_to_json(self, data, filename):
        """Save scraped data to JSON file"""
        try:
            filepath = f"json_data/{filename}.json"
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            print(f"Data saved to {filepath}")
        except Exception as e:
            self.log_error(f"Error saving JSON: {str(e)}")

    def save_to_csv(self, data, filename):
        """Save scraped data to CSV file"""
        try:
            filepath = f"csv_data/{filename}.csv"
            
            # Flatten the data structure
            flattened_data = []
            for item in data['data'].values():
                if isinstance(item, list):
                    flattened_data.extend(item)
            
            # Write to CSV
            with open(filepath, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['Content'])  # Header
                for item in flattened_data:
                    writer.writerow([item])
            print(f"Data saved to {filepath}")
        except Exception as e:
            self.log_error(f"Error saving CSV: {str(e)}")

def main():
    # Initialize the scraper
    scraper = WebScraper()
    
    # Example usage
    # Define selectors for different elements you want to scrape
    selectors = {
        'headings': 'h1, h2, h3',  # Selects all h1, h2, and h3 tags
        'paragraphs': 'p',         # Selects all paragraph tags
        'links': 'a',              # Selects all links
    }
    
    # List of URLs to scrape (you can modify this)
    urls = [
        'https://shadowfox.in'
    ]
    
    # Scrape each URL
    all_data = []
    for url in urls:
        print(f"Scraping {url}...")
        data = scraper.scrape_website(url, selectors)
        if data:
            all_data.append(data)
            
            # Save individual URL data
            filename = f"scrape_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            scraper.save_to_json(data, filename)
            scraper.save_to_csv(data, filename)
    
    # Save all data combined
    if all_data:
        combined_filename = f"combined_scrape_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        scraper.save_to_json({'urls': all_data}, combined_filename)

if __name__ == "__main__":
    main()
