import re
import pycorenlp
from collections import Counter
import collections
import pandas as pd
from playwright.sync_api import sync_playwright, Playwright
from PyPDF2 import PdfReader

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

reader = PdfReader("data/actOne.pdf")
reader2 = PdfReader("data/actOne.pdf")
reader3 = PdfReader("data/actOne.pdf")

numOfPages = len(reader.pages)


page = reader.pages[0]

text = page.extract_text()

# print(text)

for i in range(numOfPages):
    temp = reader.pages[i].extract_text()
    print(temp)

