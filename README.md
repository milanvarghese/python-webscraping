Malayalam News Scraper

This repository contains Python scripts for scraping Malayalam news articles from different websites. It utilizes two different scraping techniques: one using BeautifulSoup4 and the other using Selenium.
Contents

    Prerequisites
    Installation
    Usage
    License

Prerequisites

Before using the scripts in this repository, make sure you have the following installed:

    Python (version 3.6 or above)
    pip package manager

Installation

    1. Clone the repository to your local machine or download the ZIP file.
    git clone https://github.com/your-username/your-repo.git
    
    2. Change into the project directory.
    cd your-repo
    
    3. Install the required Python packages.
    pip install -r requirements.txt
    
   
   
Usage
BeautifulSoup4 Scraper

The script scraper-1 - BeautifulSoup4.py uses BeautifulSoup4 to scrape Malayalam news articles from a specific URL. Here's how to use it:

    4. Open the script scraper-1 - BeautifulSoup4.py in a text editor.

    5. Modify the url variable to the desired URL of the news article you want to scrape.
    url = "https://www.example.com/news-article"
    
    6. Save the changes to the script.
    7. Run the script using the following command:
    python scraper-1 - BeautifulSoup4.py
    
    8. The scraped news article text will be displayed on the console output.

Selenium Scraper

The script scraper-2 - Selenium.py uses Selenium and BeautifulSoup4 to scrape Malayalam news articles from a specific URL. Here's how to use it:

    9. Download the appropriate version of the ChromeDriver for your operating system from the official website.: https://sites.google.com/chromium.org/driver/

    10. Extract the downloaded ChromeDriver executable to a location on your machine.

    11. Open the script scraper-2 - Selenium.py in a text editor.

    12. Modify the url variable to the desired URL of the news article you want to scrape.
    url = "https://www.example.com/news-article"
    
    13. Save the changes to the script.
    14. Modify the chromedriver_path variable to the path of the ChromeDriver executable you extracted in step 2.
    chromedriver_path = "path/to/chromedriver"
    
    15. Save the changes to the script.
    16. Run the script using the following command:
    python scraper-2 - Selenium.py
    
    17. The scraped news article text will be saved to a file named article.txt in the current directory.
    
License
This project is licensed under the MIT License. Feel free to modify and use the code as per your needs.
