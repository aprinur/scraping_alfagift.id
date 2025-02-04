# Alfagift Scraper

If you need data of product from alfagift.com, I can't help because I won't give the fish for free, but instead I will show you how to use the fishing rod.
But if you still want the data without running the program, you can contact me.

<br>

## So, what program is this?
This is a program to collect information of product like title, brand, price, image_url and description from alfagift.com. The result will deliver as an Excel and CSV file

<br>

## How's the program works
This program use Selenium to get the html and navigate through pages, along with Beautiful Soup to parse the data and pandas to export the data as an Excel and CSV file into your Downloads folder

<br>

## How to run this program on your device?
1. First of all, you need [Python](https://www.python.org/), some IDE installed in your device and a [chromedriver](https://developer.chrome.com/docs/chromedriver/downloads) that match your chrome's version in your PATH environment variable
2. After download the file, open your IDE, open the project and create a virtual environment (recommended)
3. Install dependencies from requirements.txt
   ```
   pip install requirements.txt
   ```
4. Open file main.py and search for line number 86, add a number after colon to limit the amount of pages to scrape, or leave it empty to scrape all the category
   ```
   for category_url in category_urls[:]:
   ```
5. Next, search for line number 101 and do the same to limit the amount of products to scrape, or leave it empty to scrape all the product information
   ```
   for product_url in product_urls[:]:
   ```
6. Finally, change the filename in line number 108 to your desired name
7. Run main.py
