
import requests
from bs4 import BeautifulSoup
import json

URL = "https://quotes.toscrape.com/"


def scrape_quotes():
    try:
        response = requests.get(
            URL,
            timeout=10,
            headers={"User-Agent": "Mozilla/5.0"}
        )
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        quote_elements = soup.select(".quote")

        quotes = []

        for item in quote_elements:
            text = item.select_one(".text").get_text(strip=True)
            author = item.select_one(".author").get_text(strip=True)
            tags = [
                tag.get_text(strip=True)
                for tag in item.select(".tags .tag")
            ]

            quotes.append({
                "quote": text,
                "author": author,
                "tags": tags
            })

        with open("quotes.json", "w", encoding="utf-8") as file:
            json.dump(quotes, file, indent=4, ensure_ascii=False)

        print("Total quotes scraped:", len(quotes))
        print("Data saved to quotes.json")

        for quote in quotes[:3]:
            print("\nQuote:", quote["quote"])
            print("Author:", quote["author"])
            print("Tags:", ", ".join(quote["tags"]))

    except requests.exceptions.RequestException as error:
        print("Network error:", error)
    except (ValueError, OSError) as error:
        print("File or data error:", error)


if __name__ == "__main__":
    scrape_quotes()
