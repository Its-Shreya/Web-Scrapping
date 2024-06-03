import threading
from nltk import sent_tokenize
from scrapping import webScrap, webCrawl
from utils.word_count import word_count
from traceback import print_exc


def threadedFunctionToCrawl(sentence, links, contentType):
    """Scrap data from url and append data to links array

    Args:
        sentence (str): sentence to be searched
        links (list): links to be searched
        contentType (str): [description]
    """
    try:
        webCrawl.searchGoogle(
            links,
            contentType,
            query=f"{sentence}",
        )
    except:
        print_exc()


def webVerify(inputText, steps, contentType):
    """Tokenize given input and crawl links from google

    Args:
        inputText (str): Data inputted by user removing stopwords
        steps (int): number of sentences to be searched in one search
        contentType (str): content type of the file

    Returns:
        set: unique links
    """
    sentences = sent_tokenize(inputText)
    threads, links = [], set()
    ## Hardcoded for emergency purpose please remove the below link when you are done
    links.add("https://en.wikipedia.org/wiki/Information_technology")
    for j, i in enumerate(range(0, len(sentences), steps)):
        threads.append(
            threading.Thread(
                target=threadedFunctionToCrawl,
                args=(sentences[i : i + steps], links, contentType),
            )
        )
        threads[j].start()
        threads[j].join()
        print(links)
    return set(links)


def threadedFunctionToScrap(link, values):
    """Scrap data from url and append data to values array

    Args:
        link (str): link to be searched
        values (str): extracted text from web
    """
    try:
        extractedText, title = webScrap.extractText(link)
        textWord = word_count(extractedText)
        if textWord:
            values.append(
                {
                    "url": link,
                    "title": title,
                    "extractedText": extractedText,
                }
            )
    except:
        print_exc()


def scrapedData(text, steps, contentType):
    """Initialize threads to scrap text from web

    Args:
        text (str): Raw Data inputted by user
        steps (int): number of sentences to be searched in one search
        contentType (str): content type of the search

    Returns:
        list: extracted text from web
    """
    links = list(webVerify(text, steps, contentType))
    values, threads = [], []
    for i in range(len(links)):
        threads.append(threading.Thread(target=threadedFunctionToScrap, args=(links[i], values)))
        threads[i].start()
        threads[i].join()
    return values