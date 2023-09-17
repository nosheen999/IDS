import requests
from bs4 import BeautifulSoup
import re

# Define the birthdate and URLs for 'timeanddate' and 'britannica' websites
t_birthdate = 'July/18'
b_birthdate = 'July-18'
timeanddate_url = f'https://www.timeanddate.com/on-this-day/{t_birthdate}'
britannica_url = f'https://www.britannica.com/on-this-day/{b_birthdate}'


# Function to scrape 'timeanddate' website and return names
def scrape_timeanddate(url):
    response = requests.get(timeanddate_url, headers={"User-Agent": 'Mozilla/5.0'})
    soup = BeautifulSoup(response.content, "html.parser")
    div_event = soup.find("div", {"class": "otd-life__block"})

    ul_event = div_event.find("ul", {"class": "list--big"})
    names = []
    li_event = ul_event.find_all("li")
    for li in li_event:
        heading = li.find("h3", {"class": "otd-title"}).text.strip()
        heading = re.sub(r'\d', '', heading)
        print(heading)
        names.append(heading)
    return names


# scrape_timeanddate()
# Function to scrape 'britannica' website and return events
def scrape_britannica(url):
    page = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(page.content, "html.parser")
    events_container = soup.find("div", {"class": "border-top py-30"})

    if events_container:
        event_divs = events_container.find_all("div", {"class": "card-body font-serif"})
        events = [event_div.text.strip() for event_div in event_divs]
        return events
    else:
        return ["Information not found on britannica"]


# Scrape data from both websites
timeanddate_data = scrape_timeanddate(timeanddate_url)
britannica_data = scrape_britannica(britannica_url)

# Write data to a text file
with open('Same_Birthdays_Events.txt', 'w', encoding='utf-8') as timeanddate_file:
    timeanddate_file.write(
        "My birth date is 18 july and persons with my Shared Birthdays are as follows(timeanddate):\n")
    for names in timeanddate_data:
        timeanddate_file.write(f"- {names}\n")
    timeanddate_file.write("\n\nMy birth date is 18 july and events occur on my birth date is follows (britannica):\n")
    for event in britannica_data:
        timeanddate_file.write(f"- {event}\n")

print("Scraping and writing to files complete.")
