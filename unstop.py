import os
import time
import sys
from playwright.sync_api import sync_playwright

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.excel_writer import append_data_to_master

def run_programming_scraper():
    print("Starting Unstop scraper...")
    scraped_data = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://unstop.com", timeout=60000)
        time.sleep(5)

        base_api_url = "https://unstop.com/api/public/opportunity/search-result"
        params = {
            "opportunity": "hackathons",
            "oppstatus": "open",
            "category": "Programming",
            "payment": "unpaid",
            "per_page": 20
        }

        page_num = 1

        while True:
            params["page"] = str(page_num)
            response = context.request.get(base_api_url, params=params)

            if response.status != 200:
                break

            data = response.json()
            items = data.get("data", {}).get("data", [])

            if not items:
                break

            for item in items:
                title = item.get("title", "N/A")
                deadline = item.get("regn_close_date", "N/A")
                seo_url = item.get("seo_url", "")

                if seo_url.startswith("http"):
                    link = seo_url
                else:
                    link = f"https://unstop.com{seo_url}"

                scraped_data.append((title, deadline, link))

            page_num += 1
            time.sleep(1)

        browser.close()

    return append_data_to_master("Unstop", scraped_data, "Unstop")

if __name__ == "__main__":
    count = run_programming_scraper()
    print(f"Added {count} new Unstop hackathons.")
