# this page goes to the main en-gadget website page and gets the 3 heading and the redirecting link for the page
import requests
from bs4 import BeautifulSoup


class MainPage:

    # initialise
    def __init__(self):
        url = "https://www.engadget.com"

        response = requests.get(f"{url}/")
        response = response.text

        soup_data = BeautifulSoup(response, "html.parser")

        self.data_page1 = soup_data.select(selector="div div h2 a",
                                           class_="C(engadgetSteelGray)  Fw(400) Td(n) Bdbw(1px):h Bdbc(lightgrey):h "
                                                  "Bdbs(s):h Fz(30px) Lh(35px) Fz(22px)--lg Lh(25px)--lg Fz(24px)--md "
                                                  "Lh(30px)--md Fz(22px)--sm Lh(25px)--sm Fw(500)!--sm serif")
        self.web_data = []

    # gets the heading and the link for each content
    def get_links_texts(self):
        for i in range(3):
            heading = self.data_page1[i].getText()
            html_link = self.data_page1[i].get("href")
            value = {
                "heading": heading,
                "link": html_link
            }
            self.web_data.append(value)

        return self.web_data
