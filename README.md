## Netflix Scraper and Ratings Enrichment

#### Project Description

This Python project scrapes data from Netflix profiles, extracting information about both movies and TV shows. Leveraging the power of web scraping libraries like BeautifulSoup and HTTP requests via the requests module, it collects essential details such as title, release date, genre, description, and content rating.

To enhance the collected data, the project integrates with the Open Movie Database (OMDb) API, fetching IMDb ratings, language, country, awards, and other metadata for each title. This enriches the dataset, providing users with a comprehensive view of the content available on Netflix.

The processed data is organized into pandas DataFrames, where duplicates are removed, and text preprocessing is performed to ensure data consistency. Finally, the enriched dataset is exported to an Excel file for further analysis or visualization.
![MyNetflixDashboard](https://user-images.githubusercontent.com/59096353/219475079-996fd09b-8e13-4680-ae93-69ca6e31ab44.png)

# Getting Started
To get started with this project, you will need to have Python installed on your computer. You will also need to create an OMDb API key, which you can get by signing up at http://www.omdbapi.com/.

To use this repository, you will need to have Python installed and set up with your API key. Once this is done, you can download the NetflixProject.py script and replace the placeholder "XXXXXXXX" with your information. To run the script, navigate to the directory where the script is saved and execute it from the command line. The script will prompt you to log in to your Netflix account and then scrape your account data to get the titles of the movies and TV shows you've watched.

#### Usage
After running the script, a CSV file named netflix_ratings.csv will be generated. This file contains information about the movies and TV shows on your Netflix profile, along with their IMDb ratings. You can view this file in Excel or use a Tableau dashboard to interact with and visualize your data. The link to my dashboard is provided below. Simply click the link to access the dashboard:

My Netflix Dashboard Link: https://public.tableau.com/app/profile/behnaz.fakhar.firouzeh/viz/BehnazNetflixData/Dashboard1"

#### Acknowledgments
The Python Requests library for making HTTP requests

The Beautiful Soup library for web scraping

The OMDb API for movie and TV show data

