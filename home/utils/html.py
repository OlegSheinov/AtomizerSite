from bs4 import BeautifulSoup


def to_html(value):
    soup = BeautifulSoup(value, 'html.parser')
    for tag in soup.find_all('p'):
        if not tag.string:
            tag.string = "\n"
        tag.unwrap()
    return str(soup)
