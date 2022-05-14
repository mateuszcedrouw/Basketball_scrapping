import scrapy

limit_100 = False
if limit_100:
    lim = 101
else:
    lim = -1

# The data fields are defined
class Player(scrapy.Item):
    name                  = scrapy.Field()
    games                 = scrapy.Field()
    points                = scrapy.Field()
    total_rebounds        = scrapy.Field()
    assists               = scrapy.Field()
    physical              = scrapy.Field()


# Second spider fetches actual information about the players, by visiting each player's site
# Here, the limiter is utilized in order for the spider to only visit 100 pages if it is required
class LinksSpider(scrapy.Spider):
    name = 'player_info'
    allowed_domains = ['basketball-reference.com/']
    try:
        with open("player_links.csv", "rt") as f:
            start_urls = [url.strip() for url in f.readlines()][1:lim]
    except:
        start_urls = []

    def parse(self, response):
        p = Player()

        name_xpath          = '//h1/span/text()'
        games_xpath         = '//div[span[@data-tip="Games"]]/p[1]/text()'
        points_xpath        = '//*[@data-tip="Points"]/following-sibling::p[1]/text()'
        totalRebounds_xpath = '//*[@data-tip="Total Rebounds"]/following-sibling::p[1]/text()'
        assists             = '//*[@data-tip="Assists"]/following-sibling::p[1]/text()'
        physical            = '/html/body/div[3]/div[2]/div[1]/div[2]/p[4]/text()'

        p['name']                  = response.xpath(name_xpath).getall()
        p['games']                 = response.xpath(games_xpath).getall()
        p['points']                = response.xpath(points_xpath).getall()
        p['total_rebounds']        = response.xpath(totalRebounds_xpath).getall()
        p['assists']               = response.xpath(assists).getall()
        p['physical']              = response.xpath(physical).getall()

        yield p
