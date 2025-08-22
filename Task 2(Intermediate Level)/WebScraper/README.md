# Web Scraper

A robust and versatile web scraping tool built in Python that allows you to extract data from websites and save it in multiple formats.

## Features

- Scrape data from any website using CSS selectors
- Save data in both JSON and CSV formats
- Built-in error logging system
- Respectful scraping with automated delays
- Organized data storage structure
- User-agent handling to avoid blocking
- Session management for efficient requests

## Directory Structure

```
WebScraper/
├── webscraper.py      # Main scraper implementation
├── csv_data/          # Storage for CSV output files
├── json_data/         # Storage for JSON output files
└── logs/              # Error logs directory
```

## Requirements

- Python 3.x
- requests
- beautifulsoup4
- json
- csv

## Usage

```python
from webscraper import WebScraper

# Initialize the scraper
scraper = WebScraper()

# Define your selectors
selectors = {
    'titles': 'h1.title',
    'content': 'div.content'
}

# Scrape a website
data = scraper.scrape_website('https://example.com', selectors)

# Save data (timestamp will be automatically added)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
scraper.save_to_json(data, f"scrape_{timestamp}")
scraper.save_to_csv(data, f"scrape_{timestamp}")
```

## Features Explained

1. **Automated Directory Creation**: The scraper automatically creates necessary directories for data storage.

2. **Error Logging**: All errors are automatically logged with timestamps in the `logs` directory.

3. **Rate Limiting**: Built-in delay between requests to be respectful to websites.

4. **Data Export**: Support for both JSON and CSV export formats.

5. **Session Management**: Uses session objects for efficient request handling.

## Best Practices

- Always check the website's robots.txt before scraping
- Use appropriate delays between requests
- Handle your data responsibly
- Keep your selectors up to date

## Error Handling

The scraper includes comprehensive error handling:
- Network request errors
- Parsing errors
- File saving errors

All errors are logged in `logs/error_log.txt` with timestamps for easy debugging.

## Note

Make sure to respect the website's terms of service and robots.txt when using this scraper. Web scraping should be done responsibly and ethically.
