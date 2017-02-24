# -*- coding: utf-8 -*-
"""Web Scraper for King County Health Inspection website."""

import requests
import io
from bs4 import BeautifulSoup
import sys
import re

INSPECTION_DOMAIN = 'http://info.kingcounty.gov'
INSPECTION_PATH = '/health/ehs/foodsafety/inspections/Results.aspx'
INSPECTION_PARAMS = {
    'Output': 'W',
    'Business_Name': '',
    'Business_Address': '',
    'Longitude': '',
    'Latitude': '',
    'City': '',
    'Zip_Code': '',
    'Inspection_Type': 'All',
    'Inspection_Start': '',
    'Inspection_End': '',
    'Inspection_Closed_Business': 'A',
    'Violation_Points': '',
    'Violation_Red_Points': '',
    'Violation_Descr': '',
    'Fuzzy_Search': 'N',
    'Sort': 'H'
}

def get_inspection_page(**kwargs):
    """Fetch a set of search results. Accepts keyword arguments for
    the possible query parameters. Builds a dictionary of request query
    parameters from incoming keywords. Make a request to the King County
    server using this query. Return the bytes content of the response and the
    encoding if there is no error. Raise an error if there is a problem with
    the response.
    """
    url = INSPECTION_DOMAIN + INSPECTION_PATH
    params = INSPECTION_PARAMS.copy()
    for key, val in kwargs.items():
        if key in INSPECTION_PARAMS:
            params[key] = val
    el_response = requests.get(url, params=params)
    el_response.raise_for_status()
    return el_response.content, el_response.encoding
