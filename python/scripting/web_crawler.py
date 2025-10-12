import pprint
import requests
from bs4 import BeautifulSoup

url_page1 = "https://news.ycombinator.com/news"
url_default = "https://news.ycombinator.com/"


def get_response(url):
    res = requests.get(url)
    return res


def create_soup(res_text):
    return BeautifulSoup(res_text, "html.parser")


def create_personal_hn(links, subtext):
    hn = []
    for index, item in enumerate(links):
        title = links[index].getText()
        href = links[index].get("href", None)
        vote = subtext[index].select(".score")
        if len(vote):
            points = int(vote[0].getText().replace(" points", ""))
            if points >= 100:
                hn.append({"title": title, "link": href, "votes": points})
    return sort_stories_by_votes(hn)


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k["votes"], reverse=True)


def main():
    try:
        res = get_response(url_page1)

        if res.status_code == 200:
            soup = create_soup(res.text)
            link_page = soup.select(".morelink")

            if len(link_page):
                url = url_default + str(link_page[0].get("href"))
                new_soup = create_soup(get_response(url).text)
                soup.append(new_soup)

            links = soup.select(".titlelink")
            subtext = soup.select(".subtext")

        else:
            print(f"{res.url}  has responded {res}")

        my_hn = create_personal_hn(links, subtext)
        pprint.pprint(my_hn)
    except ConnectionError as err:
        print(ConnectionError.with_traceback)


if __name__ == "__main__":
    main()
