# basic-scraper
A simple web-scraping program, to pull in and parse restaurant health inspection data from King County, Wash., government website, following [this tutorial](https://codefellows.github.io/sea-python-401d5/assignments/tutorials/scraper.html).

Restaurant data taken from [here](http://info.kingcounty.gov/health/ehs/foodsafety/inspections/Results.aspx?Output=W&Business_Name=&Business_Address=&Longitude=&Latitude=&City=&Zip_Code=9809&Inspection_Type=All&Inspection_Start=2/1/2013&Inspection_End=2/1/2015&Inspection_Closed_Business=A&Violation_Points=&Violation_Red_Points=&Violation_Descr=&Fuzzy_Search=N&Sort=B)


###Methods include:
get_inspection_page(**kwargs):
    Fetch a set of search results. Accepts keyword arguments for possible query parameters. Build sa dictionary of request query
    parameters from incoming keywords. Query is used to request data from the King County server. Returns the bytes content of the response and the
    encoding if there is no error. Raises an error if there is a problem withthe response.

load_inspection_page(src):
    Load the inspection page.

parse_source(html, encoding='utf-8'):
    Set up the HTML as DOM nodes for scraping. Takes the response body (or the file read from disk) and parses it using BeautifulSoup. Returns the parsed object for further processing.

extract_data_listings(html):
    Find the container that holds each individual listing.

has_two_tds(elem):
    Take an element as an argument and return True if element is both a <tr> and contains exactly two <td> elements immediately within it.

clean_data(td):
    Clean up the values we get from scraping.

extract_restaurant_metadata(elem):
    Take the listing for a single restaurant, and return a Python dictionary containing the metadata we’ve extracted.

is_inspection_row(elem):
    Determine if row we're looking at is the correct inspection row.

extract_score_data(elem):
    Returns score data.