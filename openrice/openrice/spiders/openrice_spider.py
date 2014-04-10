from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector

class OpenriceSpider(Spider):
	name = "openrice";
	allowed_domains = "openrice.com";
	num_of_recom = 0;
	locate = 0;
	comment_id = 2352369;
	num_of_com = 100;

	start_urls = ["http://www.openrice.com/restaurant/commentdetail.htm?commentid=2352369"];
	
	def __init__(self):
		for count in range(1, self.num_of_com):
			self.start_urls.append("http://www.openrice.com/restaurant/commentdetail.htm?commentid=" + str(self.comment_id + count));
		#print self.start_urls;

	def parse(self,response):
		local_comment_id = response.url[len(response.url) - 7:len(response.url)];
		local_keyword = "<span class=\"recom_" + local_comment_id + " \">"; 
		try:
			locate = response.body.index(local_keyword);
		except:
			num_of_recom = 0;
			print "comment_id:" + local_comment_id + ", num_of_recom:" + str(num_of_recom);
			return ;
		
		sub_str = response.body[locate + len(local_keyword):];
		sub_str = sub_str[:sub_str.index("</span>")];
		num_of_recom = int(sub_str);
		print "comment_id:" + local_comment_id + ", num_of_recom:" + str(num_of_recom);