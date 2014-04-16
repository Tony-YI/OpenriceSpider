# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class OpenriceItem(Item):
	comment_id = Field();
	num_of_recom = Field();
	num_of_view = Field();
	ratio = Field();
	date = Field();
	pass