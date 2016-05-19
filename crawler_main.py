import urllib.request
from bs4 import BeautifulSoup, UnicodeDammit


def get_website_source(url):
    """This function returns source (string) of the html page connected with provided url"""
    reader = urllib.request.urlopen(url)
    html_source = str(reader.read())
    reader.close()
    return html_source


def find_urls(html_source):
    """This function searches for a url links in provided html source (string)"""
    link_tag = 'a'
    link_address = 'href'
    hyper_text = 'http'
    result = []

    soup = BeautifulSoup(html_source, 'html.parser')
    for link in soup.find_all(link_tag):
        url = link.get(link_address)
        if url and (url[0:4] == hyper_text) and (not (url in result)):
            result.append(url)
    return result


def crawler(url, word, depth=5):
    """This function searches for desired word (string) on desired number (depth) of next pages,
    starting with provided url"""
    result = {}
    urls = []

    for i in range(depth):
        print("Connecting...")
        print(url)
        html_source = get_website_source(url)
        print("Searching for desired word...")
        result[url] = html_source.count(word)
        if i == depth - 1:
            break
        else:
            print("Designating new URL...")
            urls += find_urls(html_source)
            for element in urls:
                if not (element in result):
                    url = element
                    break
            else:
                print("!!!Searching aborted - no new URL found!!!")
                break
    return result

#wynik = crawler("http://www.onet.pl/", "Polska", 100)