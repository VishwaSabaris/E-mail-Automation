import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from scraper.devpost import scrape_and_append_devpost
from scraper.unstop import run_programming_scraper

def main():
    print("========================================")
    print("STARTING MASTER HACKATHON AUTOMATION")
    print("========================================")

    devpost_new = scrape_and_append_devpost()
    unstop_new = run_programming_scraper()

    print("\n========================================")
    print("SCRAPING SUMMARY")
    print("========================================")
    print(f"New Devpost items added: {devpost_new}")
    print(f"New Unstop items added:  {unstop_new}")
    print(f"Total new items:         {devpost_new + unstop_new}")
    print("Master file: data/hackathons_master.xlsx")
    print("========================================")

if __name__ == "__main__":
    main()
