"""Recovered 2020 Rev transcript scraper used to assemble Biden text corpora.

This is preserved as historical source. Rev's site structure and Selenium APIs
have changed since this was written, so it should not be expected to run today
without adaptation.
"""

import os
import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options


URLS = [
    "https://www.rev.com/blog/transcripts/joe-biden-interview-transcript-response-to-sexual-assault-allegations",
    "https://www.rev.com/blog/transcripts/joe-biden-hillary-clinton-virtual-town-hall-transcript-on-womens-issues",
    "https://www.rev.com/blog/transcripts/joe-biden-virtual-town-hall-transcript-april-15",
    "https://www.rev.com/blog/transcripts/transcript-bernie-sanders-endorses-joe-biden-in-livestream-meeting",
    "https://www.rev.com/blog/transcripts/joe-biden-virtual-town-hall-transcript-april-8",
    "https://www.rev.com/blog/transcripts/transcript-joe-biden-speech-to-afl-cio-union-members-on-coronavirus",
    "https://www.rev.com/blog/transcripts/joe-biden-virtual-news-briefing-on-coronavirus-april-2",
    "https://www.rev.com/blog/transcripts/joe-biden-coronavirus-online-news-conference-transcript",
    "https://www.rev.com/blog/transcripts/joe-biden-youtube-speech-transcript-on-coronavirus-march-23",
    "https://www.rev.com/blog/transcripts/joe-biden-speech-transcript-on-primary-night-coronavirus-economy-primaries",
    "https://www.rev.com/blog/transcripts/joe-biden-speech-transcript-on-coronavirus-march-12-2020",
    "https://www.rev.com/blog/transcripts/joe-biden-speech-transcript-after-wins-in-missouri-michigan-primaries",
    "https://www.rev.com/blog/transcripts/joe-biden-detroit-michigan-rally-transcript-with-cory-booker-kamala-harris-more",
    "https://www.rev.com/blog/transcripts/super-tuesday-speech-transcripts-biden-sanders-warren-bloomberg-speeches-to-supporters",
    "https://www.rev.com/blog/transcripts/transcript-buttigieg-klobuchar-and-orourke-endorse-biden-in-dallas-rally",
    "https://www.rev.com/blog/transcripts/joe-biden-houston-rally-speech-transcript-before-super-tuesday",
    "https://www.rev.com/blog/transcripts/joe-biden-town-hall-protecting-essential-workers",
    "https://www.rev.com/blog/transcripts/joe-biden-victory-speech-transcript-biden-wins-south-carolina-democratic-primary",
    "https://www.rev.com/blog/transcripts/transcript-joe-biden-mistakenly-says-hes-a-united-states-senate-candidate-in-south-carolina-speech",
    "https://www.rev.com/blog/transcripts/joe-biden-reno-nevada-town-hall-campaign-transcript-february-17-2020",
    "https://www.rev.com/blog/transcripts/joe-biden-press-conference-transcript-biden-fires-back-at-trump-over-ukraine-allegations",
    "https://www.rev.com/blog/transcripts/joe-biden-iowa-trump-rebuke-speech-transcript-august-7",
    "https://www.rev.com/blog/transcripts/march-democratic-debate-transcript-joe-biden-bernie-sanders",
    "https://www.rev.com/blog/transcripts/south-carolina-democratic-debate-transcript-february-democratic-debate",
    "https://www.rev.com/blog/transcripts/democratic-debate-transcript-las-vegas-nevada-debate",
    "https://www.rev.com/blog/transcripts/new-hampshire-democratic-debate-transcript",
    "https://www.rev.com/blog/transcripts/january-iowa-democratic-debate-transcript",
    "https://www.rev.com/blog/transcripts/december-democratic-debate-transcript-sixth-debate-from-los-angeles",
    "https://www.rev.com/blog/transcripts/november-democratic-debate-transcript-atlanta-debate-transcript",
    "https://www.rev.com/blog/transcripts/october-democratic-debate-transcript-4th-debate-from-ohio",
    "https://www.rev.com/blog/transcripts/democratic-debate-transcript-houston-september-12-2019",
    "https://www.rev.com/blog/transcripts/transcript-of-july-democratic-debate-2nd-round-night-2-full-transcript-july-31-2019",
    "https://www.rev.com/blog/transcripts/transcript-of-the-kamala-harris-and-joe-biden-heated-exchange",
]


def make_filename(url):
    return url.rstrip("/").split("/")[-1]


def extract_biden_paragraphs(driver):
    text = ""
    for paragraph in driver.find_elements_by_css_selector("p"):
        content = paragraph.get_attribute("textContent")
        if "Joe Biden:" in content:
            text += content
    return text


def strip_time(text):
    output = ""
    for part in text.split("Joe Biden:"):
        if ")" in part:
            chunks = part.split(")")
            del chunks[0]
            output += "".join(chunks) + "\n"
    return output


def strip_bracketed_annotations(text, marker):
    output = ""
    for part in text.split(marker):
        if "]" not in part:
            continue
        chunks = part.split("]")
        chunks = [chunk for chunk in chunks if ":" not in chunk]
        output += "".join(chunks) + "\n"
    return output


def write_text(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)


def crawl():
    options = Options()
    driver = webdriver.Firefox(options=options)
    try:
        for url in URLS:
            driver.get(url)
            time.sleep(1)
            original = extract_biden_paragraphs(driver)
            cleaned = strip_time(original)
            cleaned = strip_bracketed_annotations(cleaned, "[inaudible ")
            cleaned = strip_bracketed_annotations(cleaned, "[crosstalk ")
            name = make_filename(url)
            write_text(f"_transcripts/_original/{name}.txt", original)
            write_text(f"_transcripts/_stripped/{name}.txt", cleaned)
    finally:
        driver.quit()


def compile_corpus(source_dir="_transcripts/_original", output_file="joe-compiled.txt"):
    with open(output_file, "w", encoding="utf-8") as output:
        for name in sorted(os.listdir(source_dir)):
            path = os.path.join(source_dir, name)
            if os.path.isfile(path):
                with open(path, "r", encoding="utf-8") as source:
                    output.write(source.read())


if __name__ == "__main__":
    compile_corpus()