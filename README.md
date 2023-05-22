# Engadget Tech News Blog
This project is a Flask-based web application that automatically scrapes web data from the tech news page "engadget.com" and creates a simple blog site. The application selects the top 3 news articles from the page and retrieves their respective links and headings. It then scrapes each individual article page to obtain its content, images, and other data. The scraped data is presented on the web application, allowing users to browse and read the latest tech news articles.

## Project Output
The web application provides the following functionality:

### Homepage: Displays the headings and links to the top 3 tech news articles scraped from Engadget.
![image](https://github.com/Rajkumar0819/Web-Scraped-blog-post/assets/113299030/d6f68ff6-cb89-45fc-8f37-28f8f982bfe1)

### Article Pages: Clicking on any article on the homepage will open a separate page displaying its full content, including images and other relevant data.
![image](https://github.com/Rajkumar0819/Web-Scraped-blog-post/assets/113299030/1472158e-3544-4af2-8fda-37e91b5b1864)

### Usage
#### Follow these steps to use the Engadget Tech News Blog:
1. Install the required dependencies:
pip install -r requirements.txt

2. Customize Web Scraping:
Edit main_page.py to select the top 3 news articles from "engadget.com" and retrieve their links and headings.
Modify page_data.py to scrape the content, images, and other data for each article page.

3. Run the Flask server:
python server.py

4. Access the web application:
Open your web browser and visit: http://127.0.0.1:5000
