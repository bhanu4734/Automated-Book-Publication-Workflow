from playwright.sync_api import sync_playwright
import os

def scrape_chapter(url: str) -> str:
    from bs4 import BeautifulSoup
    import requests

    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    content = soup.select_one("#mw-content-text").get_text(separator="\n")
    return content.strip()

def take_screenshot(url: str, filename: str = "chapter.png"):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        page.screenshot(path=filename, full_page=True)
        browser.close()
