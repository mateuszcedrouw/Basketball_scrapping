## Scrapy:

Enter the directory of the project through your terminal, making sure to delete the
preexisting CSV files. Run the first spider by typing in the command &quot;scrapy crawl player_links -o
player_links.csv&quot; then you can enter the code of the second spider, and change the value of
&quot;limit_100&quot; to you liking (if true then only 100 pages are scraped). Then run the second spider by
running &quot;scrapy crawl player_info -o player_info.csv&quot; in your terminal. The resulting file is
player_info.csv and its name can be modified by changing the last words of the second command.

## Beautiful Soup:

Running the Beautiful Soup Scrapper is easy. Just enter the provided scrapper (file), and run
it – you do not have to change anything in the code to run it. However, you might be willing to
change the final path where to download the scrapper data. Remember to turn to &quot;limit_100&quot; value
to false to scrap all of the players (otherwise you will scrap the data for only first 100 pages).

## Selenium:

While running the scrapper which is based on the Selenium, you have to remember to
change the settings of local options. Firstly, you should change the path which is defined via #mypath
to provide your local file path where you would like to store the data. Secondly, you have to change
the #gecko_path path and set it to your local one, which indicates the place (path) in your computer
to the geckodriver program in your PC. And like before, remember to turn to &quot;limit_100&quot; value to
false to scrap all of the players (otherwise you will scrap the data for only first 100 pages).
