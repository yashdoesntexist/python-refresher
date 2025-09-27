import csv
from pycorenlp import StanfordCoreNLP
from collections import Counter
from playwright.sync_api import sync_playwright, Playwright
from PyPDF2 import PdfReader
import json


playwright = sync_playwright().start()

browser = playwright.chromium.launch()
page = browser.new_page()
page2 = browser.new_page()
page3 = browser.new_page()
# I could for loop this and make it efficient, i might
page.goto("https://www.bclaws.gov.bc.ca/civix/document/id/lc/statreg/24022")
page2.goto("https://www.bclaws.gov.bc.ca/civix/document/id/lc/statreg/96289_01")
page3.goto("https://www.bclaws.gov.bc.ca/civix/document/id/lc/statreg/96147_01")

page.pdf(path="data/actOne.pdf")
page2.pdf(path="data/actTwo.pdf")
page3.pdf(path="data/actThree.pdf")
browser.close()

playwright.stop()


nlp = StanfordCoreNLP("http://localhost:9000") # adjust according to where your corenlp is running 

actFiles = ["actOne.pdf", "actTwo.pdf", "actThree.pdf"]

def extractFiles(pdf_path):
    reader = PdfReader(pdf_path)
    full_text = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            full_text += text + "\n"

    output = nlp.annotate(full_text, properties={
        'annotators': 'tokenize,ssplit,pos,lemma',
        'outputFormat': 'json'
    })
    if isinstance(output, str):
        output = json.loads(output)

    lemmas = []
    for sentence in output['sentences']:
        for token in sentence['tokens']:
            lemma = token['lemma'].lower()
            if lemma.isalpha():  
                lemmas.append(lemma)
    return Counter(lemmas)



actCounts = {}
allWords = set()

for act in actFiles:
    path = f"data/{act}"
    c = extractFiles(path)
    actCounts[act] = c
    allWords.update(c.keys())


allWords = sorted(allWords)
rows = []

for word in allWords:
    total = sum(actCounts[act].get(word, 0) for act in actFiles)
    row = [word, total] + [actCounts[act].get(word, 0) for act in actFiles]
    rows.append(row)


totals_row = ["TOTAL"]
totals_row.append(sum(r[1] for r in rows))
for act in actFiles:
    totals_row.append(sum(actCounts[act].values()))


with open("word_frequencies.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    header = ["Word", "Total"] + actFiles
    writer.writerow(header)
    writer.writerows(rows)
    writer.writerow(totals_row)

print("Success!")