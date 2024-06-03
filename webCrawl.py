from utils.globals import userAgent
from utils.isValidLink import isValidLink
from utils.purifyText import purifyTextBeforeGoogle
from googlesearch import search
from traceback import print_exc
import requests
from ScrapeSearchEngine.SearchEngine import Google, Bing, Yahoo, Ecosia



def searchGoogle(links, contentType, query):
    """Google search the given text

    Args:
        links (list): list of links to be searched
        contentType (str): content type of the search
        query (str): search query
    """
    try:
        if contentType == "research":
            query = " 'site:google scholar' " + query

        # wrap query with double quote
        query = purifyTextBeforeGoogle(query)
        linkText, crawledLinks = Google(query, userAgent)
        if crawledLinks != [] and linkText == crawledLinks:
            # then seacrh with Bing
            linkText, crawledLinks = Bing(query, userAgent)
            if crawledLinks != [] and linkText == crawledLinks:
                # then search with Duckduckgo
                linkText, crawledLinks = Yahoo(query, userAgent)

        for link in crawledLinks:
            if isValidLink(link, contentType):
                links.add(link)

    except:
        print_exc()
