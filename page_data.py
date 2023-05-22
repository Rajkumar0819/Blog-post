import requests
from bs4 import BeautifulSoup


class PageData:
    def __init__(self):
        self.url = "https://www.engadget.com"
        # gets the individual content for each page
        self.content = []

        # makes a list of all the needed details
        self.final_data = []

    def get_each_page_data(self, data):
        # scraping for data for 3 individual pages
        for i in range(3):
            link = data[i]["link"]
            response = requests.get(f"{self.url}{link}")
            response = response.text
            soup_data = BeautifulSoup(response, "html.parser")

            # getting the body text
            text_data = soup_data.find(name="div", class_="article-text").getText()

            # getting the image link
            image = soup_data.find(name="img", class_="W(100%) H(a)")
            image = image.get("src")

            # getting the subheading of the article title
            subheading = soup_data.find(name="h2", class_="My(0px) Fz(24px) Fw(400) Lh(32px) Fz(20px)!--sm "
                                                          "Lh(24px)!--sm Lh(24px)--xs Fz(18px)--xs "
                                                          "C(engadgetBlack) serif").getText()

            # creating a dictionary with SUBHEADING IMAGE LINK AND BODY TEXT to make a list of dictionary
            values = {
                "id": i+1,
                "subheading": subheading.strip("\n"),
                "body": text_data,
                "image": image
            }
            self.content.append(values)

        for dict1, dict2 in zip(data, self.content):
            merged_dict = {**dict1, **dict2}
            self.final_data.append(merged_dict)

        return self.final_data
