from flask import Flask, render_template
from main_page import MainPage
from page_data import PageData

main_page_obj = MainPage()
link_and_heading = main_page_obj.get_links_texts()

# creating an object for individual page content Scraping
page_data_obj = PageData()
final_data = page_data_obj.get_each_page_data(link_and_heading)


app = Flask(__name__)


@app.route("/")
def home_page():
    # this will have the heading and the link to the page
    return render_template("index.html", final_data=final_data)


@app.route("/blog/<int:index>")
def get_blog(index):
    for each_data in final_data:
        if index == each_data["id"]:
            return render_template("blog_page.html", value=index, final_data=final_data)


if __name__ == "__main__":
    app.run(debug=True)
