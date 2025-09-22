import re
import pycorenlp
from collections import Counter
import collections
import pandas as pd
import pdfplumber
from playwright.sync_api import sync_playwright, Playwright

# print(dir(playwright))

# print(dir(pycorenlp))

# print(dir(pdfplumber))

# print(dir(collections))

# playwright = sync_playwright().start()

# browser = playwright.chromium.launch()
# page = browser.new_page()
# page2 = browser.new_page()
# page3 = browser.new_page()
# # I could for loop this and make it efficient, i might
# page.goto("https://www.bclaws.gov.bc.ca/civix/document/id/lc/statreg/24022")
# page2.goto("https://www.bclaws.gov.bc.ca/civix/document/id/lc/statreg/96289_01")
# page3.goto("https://www.bclaws.gov.bc.ca/civix/document/id/lc/statreg/96147_01")

# page.pdf(path="data/actOne.pdf")
# page2.pdf(path="data/actTwo.pdf")
# page3.pdf(path="data/actThree.pdf")
# browser.close()

# playwright.stop()

actOne = pdfplumber.open("data/actOne.pdf")

actOne.to_csv()

