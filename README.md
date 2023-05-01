# NBA Stats Web Scraper

This is a Python script that scrapes NBA stats data from the official NBA stats website and stores the results in an Excel file with separate sheets for player and team data.

## How to Use

To run this script, you will need to have Python 3 installed on your computer. You will also need to install the `requests`, `beautifulsoup4`, and `pandas` libraries.

To install these libraries, run the following command in your terminal:

```bash
pip install requests beautifulsoup4 pandas
```

After installing the required libraries, you can run the script with the following command:

```bash
python main.py
```

The script will scrape the data from the NBA stats website and store the results in an Excel file called `nba_stats.xlsx` in the same directory as the script.

## How it Works

The script uses the `requests` library to make an HTTP GET request to the NBA stats website, and then uses the `beautifulsoup4` library to parse the HTML content of the response.

The script then searches the HTML for specific elements that contain the data we are interested in, using the `find` and `find_all` methods of the `beautifulsoup4` library.

Once the data has been extracted from the HTML, it is stored in a list of dictionaries, with each dictionary representing a single row of data.

Finally, the data is loaded into two separate Pandas dataframes for player and team data, and then saved to an Excel file using the `pandas` library.
