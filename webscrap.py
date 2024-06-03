from requests import Session
from bs4 import BeautifulSoup as bs
import warnings

warnings.filterwarnings("ignore", module="bs4")


def extractText(url):
    """Extract text from given url

    Args:
        url (str): url to be scraped

    Returns:
        tuple: extractedText, title
    """
    s = Session()
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET",
        "Access-Control-Allow-Headers": "Content-Type",
        "Access-Control-Max-Age": "3600",
        "User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36",
    }
    s.headers.update(headers)
    try:
        print(url, "Extrantion started")
        page = s.get(url, timeout=1, headers=headers)
        page.raw.chunked = True
        page.encoding = "utf-8"
        soup = bs(page.text, "lxml")
        title = soup.title.string
        extractedText = soup.get_text()
        print("----------------Successfully Extracted------------------")
        return extractedText, title
    except:
        print("----------------Extract text Failed------------------")
        return None, None