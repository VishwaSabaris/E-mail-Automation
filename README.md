# E-mail-Automation
Hackathon Data Scraper & Email Automation System


Project Overview

  This project is designed to automatically collect hackathon information from various online platforms and organize the data in a structured format. The goal is to help students and developers stay updated with upcoming hackathons without manually searching multiple websites.
The system scrapes hackathon details, stores them in a dataset, and prepares the data for automated email notifications.


Project Goal

   The main objective of this project is to build an AI-powered hackathon notification system that automatically discovers hackathons and notifies interested users through email.

Phase 1 – Data Scraping (Current Stage)

   In the first phase of this project, the focus is on web scraping and data collection.

   The system automatically extracts hackathon details such as:

   Hackathon Name

   Platform / Source Website

   Registration Deadline

   Event Date

   Hackathon Link

The collected data is stored in a structured format for further automation and processing.

Technologies Used

   Python

   Playwright (Web Scraping)

   Pandas / Excel Processing

   AWS Ubuntu Server

   Cron Jobs (Scheduling)

Project Structure
AI-Agent/
│
├── data/
│   └── hackathons_master.xlsx
│
├── scraper/
│   ├── devpost.py
│   └── unstop.py
│
├── utils/
│   └── helper functions
│
├── run_all.py
│
└── venv/
How the System Works

The scraper collects hackathon information from supported platforms.

Extracted data is processed and cleaned.

The data is saved in a master dataset.

The script can run automatically using scheduled tasks.

This creates a continuously updated dataset of hackathons.

Future Development (Phase 2)

The next phase of this project will focus on automation and notification delivery.

Planned features include:

  Integrating n8n automation workflows

  Automatically sending hackathon updates through email notifications

  Connecting Google Sheets as a dynamic database

  Scheduling automated workflows

  Building an AI-based filtering system to recommend relevant hackathons

  The final goal is to create a fully automated hackathon discovery and notification system.

Planned Architecture
Web Scrapers
     ↓
Data Processing
     ↓
Google Sheets Database
     ↓
n8n Automation
     ↓
Email Notification System
Why This Project

Students often miss hackathons because information is scattered across multiple platforms. This system aims to solve that problem by automatically discovering and sharing hackathon opportunities.

Author
Vishwa Sabaris V
