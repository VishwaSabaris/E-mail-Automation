import os
import time
import sys
from playwright.sync_api import sync_playwright

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.excel_writer import append_data_to_master

def scrape_and_append_devpost():
    target_url = "https://devpost.com/hackathons?challenge_type[]=online&order_by=recently-added&status[]=upcoming"
    print("Starting Devpost scraper...")

    scraped_data = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = context.new_page()
        page.set_default_timeout(60000)

        try:
            page.goto(target_url)
            page.wait_for_selector(".hackathon-tile", state="visible")

            prev_count = 0
            retries = 0

            while retries < 15:
                page.keyboard.press("End")
                page.mouse.wheel(0, 15000)
                time.sleep(3)

                curr_count = page.locator(".hackathon-tile").count()
                if curr_count > prev_count:
                    prev_count = curr_count
                    retries = 0
                else:
                    retries += 1

            tiles = page.locator(".hackathon-tile").all()

            for tile in tiles:
                try:
                    raw_link = tile.get_attribute("href")
                    if not raw_link:
                        link_el = tile.locator("a").first
                        if link_el.count() > 0:
                            raw_link = link_el.get_attribute("href")

                    if not raw_link:
                        continue

                    reg_link = raw_link if raw_link.startswith("http") else f"https://devpost.com{raw_link}"

                    title_el = tile.locator(".content h3")
                    title = title_el.inner_text().strip() if title_el.count() > 0 else "Unknown Title"

                    deadline = "N/A"
                    if tile.locator(".submission-period").count() > 0:
                        deadline = tile.locator(".submission-period").inner_text().strip()
                    elif tile.locator(".time-left").count() > 0:
                        deadline = tile.locator(".time-left").inner_text().strip()
                    elif tile.locator(".status-label").count() > 0:
                        deadline = tile.locator(".status-label").inner_text().strip()

                    scraped_data.append((title, deadline, reg_link))
                except:
                    continue
        finally:
            browser.close()

    return append_data_to_master("Devpost", scraped_data, "Devpost")

if __name__ == "__main__":
    count = scrape_and_append_devpost()
    print(f"Added {count} new Devpost hackathons.")
