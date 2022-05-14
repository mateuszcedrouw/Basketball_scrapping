import scrapy

# The data fields are defined
class Link(scrapy.Item):
    link = scrapy.Field()

# First spider retrieves links to sites with particular players
class LinkListsSpider(scrapy.Spider):
    name = 'player_links'
    allowed_domains = ['basketball-reference.com/']
    start_urls = ['https://www.basketball-reference.com/leagues/NBA_2022_per_game.html']

    #The spider looks for links with the structure "/player/(any string of characters)"
    def parse(self, response):
        xpath = '//a[re:test(@href, "/players/.*")]//@href'
        selection = response.xpath(xpath)
        for s in selection:
            l = Link()
            l['link'] = 'https://www.basketball-reference.com' + s.get()
            yield l